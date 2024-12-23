import speech_recognition as sr
import os
import time
from gtts import gTTS
from playsound import playsound
import webbrowser
import wave


def speak(text):
    audio_path = "response.mp3"

    # Mevcut dosyayı sil (eğer varsa)
    if os.path.exists(audio_path):
        os.remove(audio_path)

    # Yeni dosya oluştur ve sesli yanıtı kaydet
    tts = gTTS(text=text, lang='tr')
    tts.save(audio_path)

    # Dosyayı oynat
    playsound(audio_path)

def save_audio(audio_data, filename="recorded_audio.wav"):
    """
    Verilen audio verisini .wav dosyasına kaydeder.
    """
    with wave.open(filename, "wb") as wav_file:
        wav_file.setnchannels(1)  # Mono kanal
        wav_file.setsampwidth(audio_data.sample_width)
        wav_file.setframerate(audio_data.sample_rate)
        wav_file.writeframes(audio_data.frame_data)

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Sizi dinliyorum...")
        # Çevredeki gürültüyü azalt
        recognizer.adjust_for_ambient_noise(source)
        try:
            # Ses kaydını al
            audio = recognizer.listen(source)

            # Ses kaydını kaydet
            save_audio(audio)

            # Google Speech Recognition ile sesi metne çevir
            command = recognizer.recognize_google(audio, language='tr-TR')
            return command

        except sr.UnknownValueError:
            print("Ses anlaşılamadı. Lütfen tekrar edin.")
            speak("Anlaşılamadı, lütfen tekrar edin.")
            return ""
        except sr.RequestError:
            print("Servis hatası. Lütfen internet bağlantınızı kontrol edin.")
            speak("Servis hatası.")
            return ""
        except Exception as e:
            print(f"Bir hata oluştu: {e}")
            speak("Bir hata oluştu. Lütfen tekrar deneyin.")
            return ""

# Asistanı çalıştır
while True:
    komut = listen()
    if "çıkış" in komut.lower():
        speak("Asistan kapatılıyor.")
        exit()

    if "İnternete gir" in komut:
        speak("Hemen açılıyor")
        os.system("start chrome.exe")

    if "yazı yazacağım" in komut:
        os.system("start notepad.exe")
        speak("Yazı yazma penceresi açılıyor.")

    if "model roket nedir" in komut:
        speak("Model roket kısa mesafelere uçabilen bir modeldir.")

    if "alıştırma yapacağım" in komut:
        speak("Nerede?")
        time.sleep(2)

    if "yardım" in komut:
        speak("Çıkış, internete gir, yazı yazacağım, model roket nedir gibi komutları kullanabilirsiniz.")

    if "Fatih" in komut:
        speak("Selam ota60")

    if "kapat" in komut:
        speak("Tamam, iyi günler Ota60!")
        a = input("İşlem yapılmasını ister misiniz? (Evet/Hayır): ")
        if a.lower() == "evet":
            os.system("shutdown /s /f /t 0")
        else:
            continue

    if "adın ne" in komut:
        speak("Benim adım Fatih!")

    if "nasılsın" in komut or "napıyosun" in komut or "napıyorsun" in komut:
        speak("İyiyim!")

    if "video izleyeceğim" in komut:
        speak("YouTube açılıyor.")
        os.system("start chrome.exe https://www.youtube.com")

    if "arama yap" in komut:
        speak("Ne aramak istersiniz?")
        arama = listen()
        if arama:
            speak(f"{arama} için arama yapılıyor.")
            # Google'da arama yap
            webbrowser.open(f"https://www.google.com/search?q={arama}")
        else:
            speak("Bir şey anlayamadım, lütfen tekrar deneyin")


    if "ilahi aç" in komut:
        speak("Hemen açılıyor")
        os.system("start chrome.exe https://www.youtube.com/watch?v=lLfjr9V3B5E")
