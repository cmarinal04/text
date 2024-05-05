import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play

def convert_ogg_to_wav(ogg_file, wav_file):
    audio = AudioSegment.from_ogg(ogg_file)
    audio.export(wav_file, format="wav")

def convert_speech_to_text(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        # Ajusta los niveles de audio para un mejor rendimiento
        recognizer.adjust_for_ambient_noise(source)
        
        print("Convirtiendo audio a texto. Esto puede tomar un momento...")

        # Escucha el audio y realiza el reconocimiento de voz
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="es-ES")
            return text
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print(f"Error en la solicitud al servicio de reconocimiento de voz de Google; {e}")

if __name__ == "__main__":
    # Ruta del archivo de audio en formato Ogg
    ogg_audio_path = 'audio_yerson.ogg'
    
    # Ruta donde se guardará el archivo convertido a formato WAV
    wav_audio_path = 'audio_convertido.wav'

    # Convierte el archivo Ogg a formato WAV
    convert_ogg_to_wav(ogg_audio_path, wav_audio_path)

    # Convierte el audio a texto
    text_from_audio = convert_speech_to_text(wav_audio_path)

    # Imprime el texto obtenido
    print("Texto obtenido del audio:")
    print(text_from_audio)
