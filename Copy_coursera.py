import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    compara_a = 0
    for item in range(len(as_a)):
        compara_a += abs(as_a[item] - as_b[item])
    compara_a = compara_a / 6

    return compara_a


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    lista_sentencas = separa_sentencas(texto)
    sentencas = '.'.join(lista_sentencas)
    lista_frases = separa_frases(sentencas)
    n_t_frases = sum([len(separa_frases(frase)) for frase in lista_sentencas])
    frases = ''.join(lista_frases)
    lista_palavras = separa_palavras(frases)
    palavras = ''.join(lista_palavras)

    # Tamanho médio

    s_tamanho_p = len(palavras)
    numero_total_p = len(lista_palavras)
    tamanho_medio = s_tamanho_p / numero_total_p

    # Type-Token
    n_p_diferentes = n_palavras_diferentes(lista_palavras)
    type_token = n_p_diferentes / numero_total_p

    # Razão Hapax Legomana

    n_p_unicas = n_palavras_unicas(lista_palavras)
    hapax_legomana = n_p_unicas / numero_total_p

    # Tamanho médio de sentença
    s_n_caracteres = len(sentencas)
    n_sentencas = len(lista_sentencas)
    t_medio_sentenca = s_n_caracteres / n_sentencas

    # Complexidade de sentença
    complexidade_s = n_t_frases / n_sentencas

    # Tamanho médio de frase
    s_n_caracter_frase = len(frases)
    t_medio_frase = s_n_caracter_frase / n_t_frases

    assinatura = [tamanho_medio, type_token, hapax_legomana, t_medio_sentenca, complexidade_s, t_medio_frase]
    return assinatura


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_textos = textos
    a_infectada = ass_cp
    maior_pro = 0
    ass_comparadas = 0
    for i, texto in enumerate(lista_textos):
        assinatura = calcula_assinatura(texto)
        c_assinatura = compara_assinatura(assinatura, a_infectada)
        if i == 0:
            ass_comparadas = c_assinatura
            maior_pro = i
        if ass_comparadas >= c_assinatura:
            ass_comparadas = c_assinatura
            maior_pro = i
    maior_pro += 1
    print(f"O autor do texto {maior_pro} está infectado com COH-PIAH")
    return maior_pro

