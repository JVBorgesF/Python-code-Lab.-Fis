def media(valores):
    valores_numericos = [float(valor) for valor in valores]

    diferencas = [valores_numericos[i + 1] - valores_numericos[i] for i in range(len(valores_numericos) - 1)]

    media_diferencas = sum(diferencas) / len(diferencas)

    soma_quadrados_diferencas = sum((dif - media_diferencas) ** 2 for dif in diferencas)

    variancia_diferencas = soma_quadrados_diferencas / len(diferencas)
    desvio_padrao_diferencas = variancia_diferencas ** 0.5

    return media_diferencas, desvio_padrao_diferencas


def encontra_maximos_minimos(tempo, posicao):
    instantes_maximos = []
    instantes_minimos = []

    for i in range(1, len(posicao) - 1):
        if posicao[i - 1] < posicao[i] > posicao[i + 1] and posicao[i + 1] < posicao[i + 2]:
            instantes_maximos.append(tempo[i])
        elif posicao[i - 1] > posicao[i] < posicao[i + 1] and posicao[i + 1] > posicao[i + 2]:
            instantes_minimos.append(tempo[i])

    return instantes_maximos, instantes_minimos

tempo = input().split()[287:605]
posicao = input().split()[287:605]

maximos, minimos = encontra_maximos_minimos(tempo, posicao)
m_M, d_M = media(maximos)

m_m, d_m = media(minimos)

m, d = (m_m + m_M)/2, (d_m + d_M)/2

print('%f %f'%(m,d))

