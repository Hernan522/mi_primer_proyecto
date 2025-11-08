# calculadora.py
# Autor: David Pinto
# Calculadora básica con manejo de errores

def pedir_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada no válida. Ingresa un número.")

def main():
    numero_1 = pedir_numero("Primer número: ")
    numero_2 = pedir_numero("Segundo número: ")
    operacion = input("Operación (+, -, *, /): ").strip()

    if operacion == '+':
        print("Resultado:", numero_1 + numero_2)
    elif operacion == '-':
        print("Resultado:", numero_1 - numero_2)
    elif operacion == '*':
        print("Resultado:", numero_1 * numero_2)
    elif operacion == '/':
        if numero_2 != 0:
            print("Resultado:", numero_1 / numero_2)
        else:
            print("Error: no se puede dividir por cero.")
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    main()
