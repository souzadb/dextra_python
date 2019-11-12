################################################
# Aqui estão as regras de negócios dos Lanches #
################################################

import regras_promocoes as rp

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
    'Promocoes': {
        'MUITA CARNE': 'Desativada',
        'MUITO QUEIJO': 'Desativada',
        'LIGHT': 'Desativada'
    },
    'Valor Total': 0
}

def listar_todos_lanches():
    return lista_lanches

def listar_lanche_unico(id_lanche):
    if id_lanche in lista_lanches:
        return lista_lanches[id_lanche]
    else:
        return {'Erro': 'Lanche não cadastrado'}

def listar_todos_ingredientes():
    return lista_ingredientes

def retorna_ingredientes_valor_lanche(id_lanche):
    if id_lanche in lista_lanches:
        retorno = {}
            
        lista_ingredientes_lanche = {'ingredientes': [lista_ingredientes[i]['nome'] for i in lista_lanches[id_lanche]['ingredientes']]}
        valor_lanche = {'valor': sum([lista_ingredientes[i]['valor'] for i in lista_lanches[id_lanche]['ingredientes']])}

        retorno.update(lista_ingredientes_lanche)
        retorno.update(valor_lanche)

        return retorno
    else:
        return {'Erro': 'Lanche não cadastrado'}

def prepara_lanche_para_pedido(id_lanche, args):
    if id_lanche in lista_lanches:            

        if args['ingredientes'] == None:
            ingredientes_lanches = lista_lanches[id_lanche]['ingredientes']
        else:
            ingredientes_lanches = args['ingredientes']

        valor_lanche = sum([lista_ingredientes[i]['valor'] for i in ingredientes_lanches])
        
        valor_lanche_desconto = rp.promocao_descontos_lanche(ingredientes_lanches, pedido, valor_lanche, lista_ingredientes)
        
        pedido['Lanches'].append({
            'id': id_lanche,
            'nome': lista_lanches[id_lanche]['nome'],
            'valor': valor_lanche_desconto,
            'ingredientes': ingredientes_lanches
            })

        return {'Pedido Adicionado': {id_lanche: lista_lanches[id_lanche]['nome']}}            
    else:
        return {'Erro': 'Lanche não cadastrado'}

def lista_promocoes():
    return pedido['Promocoes']

def lista_pedido():
    valor_total = 0

    if pedido['Lanches']:
        for pedido_lista in pedido['Lanches']:
            valor_total += pedido_lista['valor']
        pedido['Valor Total'] = valor_total

    return pedido