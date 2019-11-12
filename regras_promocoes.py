##################################################
# Aqui estão as regras de negócios das Promoções #
##################################################

def promocao_descontos_lanche(ingredientes_lanches, pedido, valor_lanche, lista_ingredientes):
    desconto = 0

    if ingredientes_lanches.count('203') >= 3:
        desconto += int(ingredientes_lanches.count('203') / 3) * lista_ingredientes['203']['valor']
        pedido['Promocoes'].update({'MUITA CARNE': 'Parabéns, seu desconto de CARNE foi ativado!'})

    if ingredientes_lanches.count('205') >= 3:
        desconto += int(ingredientes_lanches.count('205') / 3) * lista_ingredientes['205']['valor']
        pedido['Promocoes'].update({'MUITO QUEIJO': 'Parabéns, seu desconto de QUEIJO foi ativado!'})

    if '201' in ingredientes_lanches and '202' not in ingredientes_lanches:
        valor_lanche * 0.9
        pedido['Promocoes'].update({'LIGHT': 'Parabéns, seu desconto LIGHT foi ativado!'})

    return valor_lanche - desconto
