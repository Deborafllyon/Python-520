#21 decisão II IF  ## 22 Depuração forma ex progr e acompanhar linha a linha forma de monitorar e encontrar erro
# Operadores relacionais >maior < menor >= e <= menor igual
# verificar se user é de maior no prog abaixo
#
# Bloco de instrução aula 23
# else:           
#  if(idade>150):  
#      print("A sua idade não pode ser superior a 150 anos!")
# else:
#      if(idade<18):
#          print('Voce precisa ter mais do que 18 anos!')    
 
 
 
idade = int(input("Informe sua idade:"))

if(idade<=0):
    print("A sua idade não pode ser 0 ou menor que 0!")
           
elif(idade>150):  
    print("A sua idade não pode ser superior a 150 anos!")
elif(idade<18):
    print('Voce precisa ter mais do que 18 anos!')    