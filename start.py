from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

lista_lanches = {
    '101': {'nome': 'X-Bacon', 'ingredientes': ['206', '202', '203']},
    '102': {'nome': 'X-Burguer', 'ingredientes': ['206', '203', '205']},
    '103': {'nome': 'X-Egg', 'ingredientes': ['206', '204', '203', '205']},
    '104': {'nome': 'X-Egg Bacon', 'ingredientes': ['206', '201', '204', '202', '203', '205']},
}

lista_ingredientes = {
    '201': {'nome': 'Alface', 'valor': 0.4},
    '202': {'nome': 'Bacon', 'valor': 2},
    '203': {'nome': 'Hambúrguer de Carne', 'valor': 3},
    '204': {'nome': 'Ovo', 'valor': 0.8},
    '205': {'nome': 'Queijo', 'valor': 1.50},
    '206': {'nome': 'Pão com Gergelim', 'valor': 1}
}

pedido = {
    'Lanches': [],
    'Promocoes': {'Promocao': 'Nenhuma promoção participante'},
    'Valor Total': 0
}

class Lanches(Resource):
    def get(self):
        return lista_lanches

class Lanche(Resource):
    def get(self, id_lanche):
        if id_lanche in lista_lanches:
            return lista_lanches[id_lanche]
        else:
            return {'Erro': 'Lanche não cadastrado'}

class Ingredientes(Resource):
    def get(self):
        return lista_ingredientes

class IngredientesDoLanche(Resource):
    def get(self, id_lanche):
        retorno = {}
        
        lista_ingredientes_lanche = {'ingredientes': [lista_ingredientes[i]['nome'] for i in lista_lanches[id_lanche]['ingredientes']]}
        valor_lanche = {'valor': sum([lista_ingredientes[i]['valor'] for i in lista_lanches[id_lanche]['ingredientes']])}

        retorno.update(lista_ingredientes_lanche)
        retorno.update(valor_lanche)

        return retorno

class AdicionarLancheCarrinho(Resource):
    def put(self, id_lanche):

        parser.add_argument('ingredientes', action='append')
        args = parser.parse_args()

        if id_lanche in lista_lanches:            

            if args['ingredientes'] == None:
                ingredientes_lanches = lista_lanches[id_lanche]['ingredientes']
            else:
                ingredientes_lanches = args['ingredientes']

            valor_lanche = sum([lista_ingredientes[i]['valor'] for i in ingredientes_lanches])

            pedido['Lanches'].append({
                'id': id_lanche,
                'nome': lista_lanches[id_lanche]['nome'],
                'valor': valor_lanche,
                'ingredientes': ingredientes_lanches
                })

            return {'Pedido Adicionado': {id_lanche: lista_lanches[id_lanche]['nome']}}            
        else:
            return {'Erro': 'Lanche não cadastrado'}

class Promocoes(Resource):
    def get(self):
        return pedido['Promocoes']

class Pedido(Resource):
    def get(self):
        valor_total = 0

        if pedido['Lanches']:
            for pedido_lista in pedido['Lanches']:
                valor_total += pedido_lista['valor']
            pedido['Valor Total'] = valor_total

        return pedido

api.add_resource(Lanches, '/api/lanche')
api.add_resource(Lanche, '/api/lanche/<id_lanche>')
api.add_resource(Ingredientes, '/api/ingrediente')
api.add_resource(IngredientesDoLanche, '/api/ingrediente/de/<id_lanche>')
api.add_resource(Promocoes, '/api/promocao')
api.add_resource(Pedido, '/api/pedido')
api.add_resource(AdicionarLancheCarrinho, '/api/pedido/<id_lanche>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')