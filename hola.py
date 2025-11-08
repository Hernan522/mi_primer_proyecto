# hola.py
# Autor: David Pinto
# Descripción: Programa que solicita el nombre del usuario y muestra un saludo personalizado.

def main():
    """Función principal del programa"""
    nombre = input("¿Cómo te llamas? ").strip()

    # Validar que el usuario sí escriba algo
    if nombre == "":
        print("No escribiste tu nombre 😅. Inténtalo de nuevo.")
    else:
        print(f"¡Hola, {nombre}! Bienvenido a tu primer proyecto con Git y Python.")

if __name__ == "__main__":
    main()

