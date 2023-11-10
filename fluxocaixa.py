def adicionar_receita(saldo, valor):
  saldo += valor
  return saldo


def adicionar_despesa(saldo, valor):
  saldo -= valor
  return saldo


def main():
  saldo = 0

  while True:
    print("Opções:")
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
      valor = float(input("Informe o valor da receita: "))
      saldo = adicionar_receita(saldo, valor)
    elif opcao == "2":
      valor = float(input("Informe o valor da despesa: "))
      saldo = adicionar_despesa(saldo, valor)
    elif opcao == "3":
      print("Saldo final:", saldo)
      break
    else:
      print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
  main()
