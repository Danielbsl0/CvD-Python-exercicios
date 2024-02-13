def notas(*nt, sit=False):
    """

    :param nt: As notas dos alunos
    :param sit: (opcional) Mostrará a situação do aluno, de acordo com a média do mesmo
    :return: dicionário com várias informaçãoes sobre a situação da turma
    """
    ok = True
    boletim = dict()
    boletim['total'] = len(nt)
    boletim['maior'] = max(nt)
    boletim['menor'] = min(nt)
    boletim['media'] = sum(nt)/len(nt)
    if sit == True:
        if boletim['media'] >= 6 and boletim['media'] < 8:
            boletim['situação'] = 'RAZOÁVEL'
        elif boletim['media'] >=8:
            boletim['situação'] = 'BOA'
        else:
            boletim['situação'] = 'RUIM'
    return boletim


resp = notas(4.5, 6.0, 8.0, 9.0, 10, 0, sit=True)
print(resp)
help(notas)
