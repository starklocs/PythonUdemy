sinal_vermelho = True
nenhum_carro_direita = False
nenhum_carro_esquerda = False
pode_atravessar_rua = sinal_vermelho or not nenhum_carro_direita or not nenhum_carro_esquerda
print(pode_atravessar_rua)