# calculadora.py
# Autor: David Pinto
# Descripción: Calculadora básica que realiza operaciones aritméticas con validación de errores.

def pedir_numero(mensaje):
    """Pide un número al usuario y valida que sea correcto."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("⚠️  Entrada no válida. Por favor, ingresa un número.")

def calcular():
    """Realiza una operación aritmética según la elección del usuario."""
    numero_1 = pedir_numero("Primer número: ")
    numero_2 = pedir_numero("Segundo número: ")
    operacion = input("Operación (+, -, *, /): ").strip()

    if operacion == '+':
        resultado = numero_1 + numero_2
    elif operacion == '-':
        resultado = numero_1 - numero_2
    elif operacion == '*':
        resultado = numero_1 * numero_2
    elif operacion == '/':
        if numero_2 != 0:
            resultado = numero_1 / numero_2
        else:
            print("🚫 No se puede dividir por cero.")
            return
    else:
        print("❌ Operación no válida.")
        return

    print(f"✅ Resultado: {resultado}")

def main():
    """Bucle principal que permite al usuario realizar múltiples cálculos."""
    while True:
        calcular()
        continuar = input("¿Deseas realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print("👋 Gracias por usar la calculadora. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
