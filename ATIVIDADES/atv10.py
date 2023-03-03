nOvos = int(input())
nPessoas = int(input())

ovosPorPessoa = nOvos // nPessoas
sobraram = nOvos % nPessoas

print("Ovos Por Pessoa: ", ovosPorPessoa)
print("Ovos Que Sobraram: ", sobraram)