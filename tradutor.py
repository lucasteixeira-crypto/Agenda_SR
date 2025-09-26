import time
import pyperclip
from deep_translator import GoogleTranslator

# Defina os idiomas
LANG_SOURCE = "auto"   # Detecta automaticamente o idioma copiado
LANG_TARGET = "en"     # Tradução de destino (ex: português)

def traduzir(texto):
    try:
        return GoogleTranslator(source=LANG_SOURCE, target=LANG_TARGET).translate(texto)
    except Exception as e:
        print("Erro na tradução:", e)
        return texto

def monitorar_clipboard():
    ultimo_texto = ""
    print("Tradutor automático iniciado. Copie qualquer texto para traduzir...\n")
    while True:
        texto_atual = pyperclip.paste()
        if texto_atual != ultimo_texto and texto_atual.strip() != "":
            ultimo_texto = texto_atual
            traduzido = traduzir(texto_atual)
            pyperclip.copy(traduzido)
            print(f"\nTexto copiado: {texto_atual}")
            print(f"Texto traduzido: {traduzido}")
        time.sleep(0.5)  # Checa a cada meio segundo

if __name__ == "__main__":
    monitorar_clipboard()
