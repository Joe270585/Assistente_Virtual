import queue
import sounddevice as sd
import vosk
import sys
import json
import pyttsx3
import webbrowser
import wikipedia

# Inicializar TTS
engine = pyttsx3.init()

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# Inicializar modelo Vosk
try:
    model = vosk.Model(lang="pt")
except:
    print("Erro: Modelo de voz em português não encontrado.")
    sys.exit(1)

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def ouvir():
    rec = vosk.KaldiRecognizer(model, 16000)
    with sd.RawInputStream(samplerate=16000, blocksize = 8000, dtype='int16',
                           channels=1, callback=callback):
        falar("Estou ouvindo...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                texto = result.get("text", "")
                if texto:
                    return texto.lower()

def processar_comando(comando):
    if "wikipedia" in comando:
        falar("O que você deseja pesquisar na Wikipedia?")
        termo = ouvir()
        try:
            resumo = wikipedia.summary(termo, sentences=2, auto_suggest=False)
            falar(resumo)
        except:
            falar("Não encontrei resultados para sua pesquisa.")

    elif "youtube" in comando:
        falar("Abrindo YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "farmácia" in comando:
        falar("Abrindo mapa de farmácias próximas")
        webbrowser.open("https://www.google.com/maps/search/farmacia+perto+de+mim")

    elif "sair" in comando or "encerrar" in comando:
        falar("Até logo!")
        sys.exit(0)
    else:
        falar("Desculpe, não entendi o comando.")

def main():
    falar("Assistente Virtual iniciado. Diga um comando.")
    while True:
        comando = ouvir()
        if comando:
            print(f"Você disse: {comando}")
            processar_comando(comando)

if __name__ == "__main__":
    main()
