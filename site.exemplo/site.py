def greet():
    name = input("Seu nome? ")
    print(f"Olá, {name}!")


def add_numbers():
    try:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
    except ValueError:
        print("Entrada inválida. Use números.")
        return
    print(f"Soma: {a + b}")


def reverse_text():
    s = input("Texto: ")
    print("Invertido:", s[::-1])


def main():
    while True:
        print("\nEscolha uma opção:")
        print("1) Saudar")
        print("2) Somar dois números")
        print("3) Inverter texto")
        print("4) Sair")
        choice = input("> ").strip()
        if choice == "1":
            greet()
        elif choice == "2":
            add_numbers()
        elif choice == "3":
            reverse_text()
        elif choice == "4":
            print("Tchau!")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == '__main__':
    main()
