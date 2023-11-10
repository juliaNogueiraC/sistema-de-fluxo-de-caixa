fluxo_caixa= []
print("---------------")
print("Fluxo de Caixa")
print("---------------")
print("1 - Caixa - add receita")
print("2 - Caixa - add despesa")
print("\n# p sair #\n")

'''
while True:
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        receita = float(input("Digite o valor da receita: "))
        fluxo_caixa.append(receita)
        print("Receita adicionada com sucesso!")
    elif opcao == 2:
        despesa = float(input("Digite o valor da despesa: "))
        fluxo_caixa.append(despesa)

    '''''

def addTransacao():
  nome = input("Digite o nome da transação: ")
  valor = float(input("Digite o valor da transação: "))
  fluxo_caixa.append({
    "nome": nome, 
    "valor":valor
     })

while True:
  opcao = int(input("Escolha uma opção: "))
  if opcao == 1:
    addTransacao()
  if opcao == 2:
    addTransacao()
  else:
    print("Opção inválida!")
    break

# nota fiscal
total = 0
for fc in fluxo_caixa:
  print("nome:", fc['nome'], ",valor: R$", fc['valor'])
  total = total + fc['valor']

print("saldo total", total)
