def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) mostrar ou não o cálculo de fatorial
    :return: Mostrar o fatorial do número inserido
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(f'{c} ', end=' ')
            print('X ' if c > 1 else '= ', end=' ')
    return f


help(fatorial)

        