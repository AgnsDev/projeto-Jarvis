import speech_recognition as sr
import pyttsx3

# Iniciar mecanismo de fala
engine = pyttsx3.init()
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# Ouvir comando
def ouvir_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Ouvindo...")
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {comando}")
        return comando.lower()
    except:
        falar("Desculpe, não entendi.")
        return ""

# Função principal
def iniciar_jarvis():
    falar("Olá, sou o Jarvis. Como posso ajudar?")
    while True:
        comando = ouvir_comando()
        if "sair" in comando:
            falar("Até logo!")
            break
        elif "abrir navegador" in comando:
            falar("Abrindo o navegador")
            import webbrowser
            webbrowser.open("https://www.google.com")
        else:
            falar("Comando não reconhecido.")

iniciar_jarvis()
