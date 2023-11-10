'''
teste = input("digite um nome:")
idade = int (input(("sua idadade:")))
print ("se nome é ", teste)
print ("sua idade é", idade)
print(type(idade))

------------------------------------

valor1 = int(input("digite um numero:"))
valor2 = int(input("digite outro numero:"))

if valor1 > valor2:
  print("o maior numero é", valor1)
else:
  print("o maior numero é", valor2)

------------------------------------
idade = int(input(("digite sua idade:")))
if idade >= 18:
  print("voce pode tirar carteira de motorista")
if idade < 18:
  print("voce nao pode tirar carteira de motorista")

  ------------------------------------
salario = float(input("digite seu salario:"))
if salario <= 1250:
  print("seu novo salario é", salario + (salario * 0.15))
else:
  print("seu novo salario é", salario + (salario * 0.10))


  ------------------------------------
  

salario = float(input("digite seu salario:"))

if salario <= 3000:
  print("voce é junior")
elif salario > 3000 and salario <= 6000:
  print("voce é pleno")
elif salario > 6000 and salario <= 15000:
  print("voce é senior")
else:
  print("voce é master")

  ------------------------------------



lista = []
for i in range (0,5):
  lista.append(int(input("digite um numero:")))
print(lista)
print(lista[0])

---------------------------------
metodos

lista = []
lista.append("oi") # adciona valores a lista, item
lista.insert(0 , "oi") # adciona valores a lista, segundo a posição, posisção e item
lista.pop(0) # remove valores da lista, segundo a posição, , nehum parametro ou posição
lista.remove("oi") # remove valores da lista, segundo a posição,
lista.sort() # ordena a lista, nehum parametro
lista.reverse() # inverte a lista, nehum parametro
lista.index(1) # busca a posição de um item na lista, segundo a posição, , item
lista.count(item) # conta quantas vezes um item aparece na lista, segundo a posição, , item
lista.clear() # limpa a lista, nehum parametro
lista.copy() # copia a lista, nehum parametro
lista.extend(lista2) # adciona valores a lista, segundo a posição, , lista2
lista.sort(reverse=True) # ordena a lista, segundo a posição, , reverse=True
lista.remove(item) # remove valores da lista, segundo a posição, , item  
min(lista)
max(lista)
print(lista)

---------------------

# inserir notas de 3 alunos 
f
notas = []
for x in range(3):
  cod = int(input("seu cod de aluno:"))
  nota = float(input("nota do aluno:"))
  resultado = [cod, nota]
  
  notas.append(resultado)
 # notas.append([cod,nota])
print(notas)


-------------------------------
def adcionarNotas(nota1, nota2, nota3):
  notas = []
  for x in range(3):
    cod = int(input("seu cod de aluno:"))
    nota = float(input("nota do aluno:"))
    resultado = [cod, nota]

    notas.append(resultado)

  print(notas)

adcionarNotas(0, 0, 0)
--------------------

def remover_aluno_por_codigo(lista_notas, codigo):
  for aluno in lista_notas:
      if aluno[0] == codigo:
          lista_notas.remove(aluno)
          return True  # Retorna True se o aluno for removido com sucesso.
  return False  # Retorna False se o código do aluno não for encontrado na lista.

notas = []  # Sua lista de notas
--------------------------------------

# Adicione alguns alunos à lista (exemplo)
notas = []  # Sua lista de notas
for x in range(3):
  cod = int(input("Seu código de aluno: "))
  nota = float(input("Nota do aluno: "))
  resultado = [cod, nota]
  notas.append(resultado)

print("Lista de notas antes da remoção:")
print(notas)

codigo_para_excluir = int(input("Informe o código do aluno a ser removido: "))
if remover_aluno_por_codigo(notas, codigo_para_excluir):
  print("Aluno removido com sucesso.")
else:
  print("Aluno não encontrado na lista.")

print("Lista de notas após a remoção:")
print(notas)
-------------------------------
notas = []
contador = 1

while contador <= 5:
  cod = int(input("Seu código de aluno: "))
  nota = float(input("Nota do aluno: "))
  resultado = [cod, nota]
  notas.append(resultado)
  contador += 1
print("qtd notas:", len(notas))

 '''
import os  # Import os for the os.system('cls') function
#
# Código para limpar a tela
mensagens = []
nome = input("Nome:")

while True:
    # Limpando o terminal
    # os.system('cls')
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['text'])
    print("_________________")

    # Obtendo texto
    texto = input("Mensagem:")
    if texto == "fim":
        break

    # Adicionando texto à lista
    mensagens.append({"nome": nome, "text": texto})
