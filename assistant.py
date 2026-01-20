import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

class WritingAssistant:
    def __init__(self):
        # Inicializa el cliente de OpenAI buscando la API KEY en el entorno
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("Error: No se encontró la variable OPENAI_API_KEY en el archivo .env")
        
        self.client = OpenAI(api_key=api_key)
        # Usamos gpt-3.5-turbo por ser rápido y económico, o gpt-4 si tienes acceso
        self.model = "gpt-3.5-turbo"

    def _get_completion(self, system_role: str, user_prompt: str) -> str:
        """Método auxiliar privado para realizar la llamada a la API."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_role},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7, # Creatividad balanceada
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Ocurrió un error al comunicarse con OpenAI: {str(e)}"

    def correct_grammar(self, text: str) -> str:
        """Corrige gramática y estilo del texto proporcionado."""
        role = "Eres un editor experto. Tu trabajo es corregir la gramática, ortografía y mejorar el estilo del texto manteniendo el tono original."
        return self._get_completion(role, text)

    def autocomplete_sentence(self, text: str) -> str:
        """Sugiere una continuación para una oración o párrafo incompleto."""
        role = "Eres un asistente de escritura creativa. Completa la oración o párrafo del usuario de manera coherente y fluida."
        return self._get_completion(role, text)

    def generate_content(self, topic: str, content_type: str = "artículo") -> str:
        """Genera texto completo basado en un tema."""
        role = f"Eres un escritor profesional. Debes redactar un {content_type} breve y bien estructurado sobre el tema que te den."
        prompt = f"Escribe sobre: {topic}"
        return self._get_completion(role, prompt)

    def save_draft(self, content: str, filename: str = "borrador.txt"):
        """Simulación de guardado en base de datos o sistema de archivos local."""
        # Simulación requerida por el proyecto
        print(f"\n[SISTEMA] Conectando con el gestor de archivos...")
        print(f"[SISTEMA] Guardando contenido en '{filename}'...")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print("[SISTEMA] ¡Guardado exitoso!")