import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_messages(mensagens):
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['text'])
    print("_________________")

def main():
    mensagens = []
    nome = input("Nome:")

    while True:
        clear_screen()
        display_messages(mensagens)

        texto = input("Mensagem:")
        if texto == "fim":
            break

        mensagens.append({"nome": nome, "text": texto})

if __name__ == "__main__":
    main()
