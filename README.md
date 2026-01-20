# Proyecto: Asistente de Escritura Automática

Este proyecto es una aplicación de consola desarrollada en Python 3.13 que utiliza la inteligencia artificial de OpenAI para asistir a los usuarios en tareas de redacción.

## Funcionalidades
1. **Corrección de Gramática y Estilo:** Mejora textos existentes.
2. **Autocompletado:** Sugiere continuaciones coherentes para oraciones incompletas.
3. **Generación de Contenido:** Crea textos completos (emails, artículos, etc.) a partir de un tema.
4. **Simulación de Guardado:** Guarda los resultados generados en un archivo de texto local.

## Requisitos Previos
* Python 3.13 instalado.
* Una API Key válida de OpenAI.

## Instrucciones de Instalación y Ejecución

Sigue estos pasos para ejecutar el proyecto:

### 1. Crear entorno virtual
Abre tu terminal en la carpeta del proyecto y ejecuta:

```bash
# En Windows
python -m venv venv
.\venv\Scripts\activate

# En Mac/Linux
python3 -m venv venv
source venv/bin/activate
```
### 2. Instalar dependencias
Instala las librerías listadas en requirements.txt:
    pip install -r requirements.txt

### 3. Configurar API Key
1) Crea un archivo llamado .env en la raíz del proyecto.
2) Agrega tu clave de OpenAI en el archivo con el siguiente formato:
    OPENAI_API_KEY=sk-tu-clave-secreta-aqui

### 4. Ejecutar el Asistente
Inicia la aplicación con el siguiente comando:
    python main.py

### 5. LISTO!!!