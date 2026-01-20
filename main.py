import sys
from assistant import WritingAssistant

def print_separator():
    print("-" * 60)

def main():
    print("Iniciando Asistente de Escritura Automática (Python 3.13)...")
    
    try:
        assistant = WritingAssistant()
    except ValueError as e:
        print(f"\nERROR CRÍTICO: {e}")
        print("Asegúrate de haber creado el archivo .env con tu OPENAI_API_KEY.")
        sys.exit(1)

    while True:
        print_separator()
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Corregir Gramática y Estilo")
        print("2. Autocompletar Frase/Idea")
        print("3. Generar Texto desde Cero (Artículo/Email)")
        print("4. Salir")
        
        option = input("\nSelecciona una opción (1-4): ")

        if option == '1':
            text = input("\nIngresa el texto a corregir:\n> ")
            if text:
                print("\nProcesando...")
                result = assistant.correct_grammar(text)
                print(f"\n[Resultado]:\n{result}")
                
        elif option == '2':
            text = input("\nIngresa el inicio de la frase:\n> ")
            if text:
                print("\nGenerando sugerencias...")
                result = assistant.autocomplete_sentence(text)
                print(f"\n[Sugerencia]:\n{text} {result}")

        elif option == '3':
            topic = input("\n¿Sobre qué tema quieres escribir?: ")
            ctype = input("¿Qué tipo de texto? (ej. email, poema, artículo): ")
            if topic:
                print("\nEscribiendo (esto puede tardar unos segundos)...")
                result = assistant.generate_content(topic, ctype)
                print(f"\n[Texto Generado]:\n{result}")
                
                save = input("\n¿Deseas guardar este texto? (s/n): ")
                if save.lower() == 's':
                    assistant.save_draft(result)

        elif option == '4':
            print("\n¡Gracias por usar el Asistente de Escritura! Hasta luego.")
            break
        
        else:
            print("\nOpción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()