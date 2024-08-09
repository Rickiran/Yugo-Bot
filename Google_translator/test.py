from langdetect import detect
from deep_translator import GoogleTranslator
import googletrans
# Texto de ejemplo
text_ = "Hola, ¿cómo estás?"

# Detectar el idioma del texto
detected_lang = detect(text_)
print("Idioma detectado:", detected_lang)  # Esto debería imprimir 'es' para español

# Crear un objeto GoogleTranslator para traducir al inglés
translator = GoogleTranslator(source=detected_lang, target='en')

# Traducir el texto
translation = translator.translate(text_)
print("Texto traducido:", translation)


language = googletrans.LANGUAGES
print(language)

