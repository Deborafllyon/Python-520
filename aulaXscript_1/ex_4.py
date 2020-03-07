# Potenciação e radiciação 
# underline usado na linha do IDLE indica que vc tera o ultimo valor.
# Ope de igualdade igual é ou (==)   / diferente é (!=).
# (x==y) x é igual a y.  / x é diferente a y (x!=y).
# aula 20 usando Decisões (SE)
#  if (True) é execultado se false nao execulta 4 posições único bloco
# else + if ==> elif true + true  

ação = int(input("Digite '1' para Sim e '2' para Não:" ))

if(ação==1):
    print("Você disse que sim!")
else:
    if(ação==2):
        print("Você disse que não!")
    else:
        print("O número digitado não é '1' e nem '2'!!!")    