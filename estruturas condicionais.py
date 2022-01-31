# ESTRUTURAS CONDICIONAIS

#  if <condição>:
#      <bloco_de_codigo1>
#  else:
#      <bloco_de_codigo2>


#  if True:
#      print("Seja bem-vindo!")


#  if False:
#      print("Seja bem-vindo!")


#  nome = input("Digite seu nome: ")
#  idade = int(input("Digite sua idade: "))
###############################   if   #################################
# if (expressão_for_verdadeira):
#    executar_bloco_de_codigo()
###############################   else   ###############################
#if (expressao_for_verdadeira):
#    executar_primeiro_bloco_de_codigo()
#else:
#    executar_segundo_bloco_de_codigo()
###############################   elif   ###############################
#if (expressao_for_verdadeira):
#    executar_primeiro_bloco_de_codigo()
#elseif (segunda_expressao_for_verdadeira):
#    executar_segundo_bloco_de_codigo()

# if/else
a = int(input("informe um número entre 0 e 100:    "))
if a >= 50:
    print("O número", a, "é maior ou igual a 50")
else:
    print("O número", a, "é menor que 50")

# if/elif/else
b = int(input("Informe um número entre 0 e 100:  "))
if b > 50:
    print("O número", b, "é maior que 50.")
elif b == 50:
    print("O número informado é igual a 50.")
else:
    print("O número", b, "é menor que 50.")

# == É utilizado para comparar duas váriaveis ou expressões.

c = 10
if c == 10:
    print("Verdadeiro")
else:
    print("Falso")

# != É utilizado para fazer a verificação de diferença entre dois termos

d = 10
if d != 10:
    print("Verdadeiro")
else:num = 1
if num == 1:
    print("Cadastrar produto.")
elif num == 2:
    print("Remover produto.")
elif num == 3:
    print("Listar produtos")
else:
    print("Opção inválida.")

    print("Falso")


# < É utilizado para verificar se o primeiro termo é menor que o segundo

e = 10
f = 20
if e < f:
    print("Verdadeiro")
else:
    print("Falso")

# <= É utilizado para comparar o primeiro e segundo termo se menor ou igual

g = 10
h = 10
if g <= h:
    print("Verdadeiro")
else:
    print("Falso")

# > É utilizado para verificar se o primeiro termo é maior que o segundo
i = 10
j = 20
if i > j:
    print("Verdadeiro")
else:
    print("Falso")

# >= É utilizado para dizer se o primeiro termo é maior ou igual ao segundo termo
l = 10
m = 10
if l >= m:
    print("Verdadeiro")
else:
    print("Falso")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print(f"Olá, {nome}!")
    print("Seja bem vindo ao nosso sistema. ")
    if len(nome)>5:
        print("Seu nome é muito longo.")
    else:
        print("Seu nome é muito curto.")
else:
    print(f"Olá, {nome}!")
    print("Acesso negado.")
lista = []
num = 1
if num == 1 :
    print("Cadastrar produto")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("digite o preço do produto: "))
    if quantidade > 0:
        print("Produto cadastrado com sucesso.")
        lista.append([nome, quantidade, preco])
    else:
        print("Quantidade inválida.")
elif num == 2:
    print("Remover produto")
elif num == 3:
    print("Listar produtos")
else:
    print("Opção inválida.")

print(lista)