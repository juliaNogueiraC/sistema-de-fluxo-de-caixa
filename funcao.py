def minha_funcao(valor1, valor2):
  return valor1 + valor2

while True:
  valor1 = int(input("Digite o primeiro valor: "))
  valor2 = int(input("Digite o segundo valor: "))
  
  
  
  resposta = minha_funcao(valor1, valor2)
  print(valor1, valor2, "sua soma é", resposta)