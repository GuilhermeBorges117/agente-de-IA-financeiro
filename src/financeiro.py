def calcular_saldo(transacoes):
    saldo = 0
    for t in transacoes:
        valor = float(t['valor'])
        if t['tipo'] == 'entrada':
            saldo += valor
        else:
            saldo -= valor
    return saldo


def total_gastos(transacoes):
    return sum(float(t['valor']) for t in transacoes if t['tipo'] == 'saida')


def gastos_por_categoria(transacoes):
    categorias = {}
    for t in transacoes:
        if t['tipo'] == 'saida':
            cat = t['categoria']
            valor = float(t['valor'])
            categorias[cat] = categorias.get(cat, 0) + valor
    return categorias
