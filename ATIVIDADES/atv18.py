'''altura = 1.75
int_altura = int(altura)
print("Tenho mais de %i metro(s) de altura" % int_altura)'''
def maiorPalindromo(s): 
    maiorPal = ""
    tam = len(s) 
  
    # Iterando para todas as posições 
    # da string 
    for i in range(tam): 
        # Definindo o tamanho 
        # do palindrômio 
        for j in range(i + 1, tam + 1): 
  
            # Obtendo o fragmento da string 
            # entre a posição i e j 
            fragmento = s[i:j] 
  
            # Verificando se o fragmento 
            # é um palindrômio 
            if (fragmento == fragmento[::-1]): 
  
                # Se for maior, atualiza 
                if len(fragmento) > len(maiorPal): 
                    maiorPal = fragmento 
  
    return maiorPal 
  
# Driver Code 
s = "abaxyzzyxf"
print(maiorPalindromo(s))