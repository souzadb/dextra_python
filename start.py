from flask import Flask
from flask_restful import Resource, Api, reqparse
from waitress import serve

import regras_lanches as rl

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()


class Lanches(Resource):
    def get(self):
        return rl.listar_todos_lanches()

class Lanche(Resource):
    def get(self, id_lanche):
        return rl.listar_lanche_unico(id_lanche)

class Ingredientes(Resource):
    def get(self):
        return rl.listar_todos_ingredientes()

class IngredientesDoLanche(Resource):
    def get(self, id_lanche):
        return rl.retorna_ingredientes_valor_lanche(id_lanche)

class AdicionarLancheCarrinho(Resource):
    def put(self, id_lanche):
        parser.add_argument('ingredientes', action='append')
        args = parser.parse_args()
        return rl.prepara_lanche_para_pedido(id_lanche, args)

class Promocoes(Resource):
    def get(self):
        return rl.lista_promocoes()

class Pedido(Resource):
    def get(self):
        return rl.lista_pedido()

api.add_resource(Lanches, '/api/lanche')
api.add_resource(Lanche, '/api/lanche/<id_lanche>')
api.add_resource(Ingredientes, '/api/ingrediente')
api.add_resource(IngredientesDoLanche, '/api/ingrediente/de/<id_lanche>')
api.add_resource(Promocoes, '/api/promocao')
api.add_resource(Pedido, '/api/pedido')
api.add_resource(AdicionarLancheCarrinho, '/api/pedido/<id_lanche>')


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port='8080')
    serve(app, host='0.0.0.0', port=8080)