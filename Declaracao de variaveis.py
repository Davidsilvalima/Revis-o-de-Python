nome   = "João"    # string
idade  = 18        # int
altura = 1.73      # float
# print(nome)
# print(idade)
# print(altura)

type(nome)
type(idade)
type(altura)

#  x = 10
#  x = 10.5
#  print(x)

# Recebendo dados do usuário
# nome = input("digite seu nome")

#numeros
x = 10      #int
y = 10.5    #float
z = 10+1j   #complex

#print(type(x))
#print(type(y))
#print(type(z))

#strings

nome = "UserPython"
print(nome[0])      #selecionou a primeira letra
print(nome[:2])     #selecionou as letras us, seleciona o numero total -1
print(nome[4:])     #selecionou da letra na posição 4 "P" até o final "Python"
print(nome[:])      #Selecionou tudo "UserPython"
print(len(nome))    #contou o numero de letras

a = "Python World"
print("Python" in a)       #retorna "True"
print("JavaScript" in a)   #retorna "False"

print(nome not in "UserPython UserPython") #retorna "False"
print(nome in "UserPython UserPython")

nome = "João"
print(nome.lower())   #retorna letras do nome minúsculas
print(nome.upper())   #retorna letras do nome maiúsculas

ling = "               Python                  "
print(ling.strip())  #imprime o nome sem espaços

nome = "joão carlos da silva"
print(nome.strip().title()) #a tag title imprime os nomes com as primeiras letras maiúsculas
print(nome.index("j"))      #diz em qual posição se encontra a letra, "0", neste caso.

######################################################################################
# Operadores de comparação
#          ==     igual
#          !=     diferente
#          >=     maior ou igual
#          <=     menor ou igual
#           >     maior
#           <     menor
#         and     retorna verdadeiro caso as comparações sejam iguais "e e"
#          or     retorna verdadeiro caso um dos comparadores sejam verdadeiro "ou"
######################################################################################

###################################Tabela verdade#####################################
#     Tabela 'and'               Tabela 'or'
#       VV = V                       VV = V
#       VF = F                       VF = V
#       FV = F                       FV = V
#       FF = F                       FF = F
######################################################################################

