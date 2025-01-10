import sounddevice as sd
import numpy as np
import keyboard
import wave
from openai import OpenAI
import pyautogui
import os
import time

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("A chave da API OpenAI não foi encontrada nas variáveis de ambiente.")
client = OpenAI(api_key=api_key)

# Configurações de áudio
SAMPLE_RATE = 22050
CHANNELS = 1
recording = False
audio_data = []

def audio_callback(indata, frames, time, status):
    if recording:
        # Converte para int16 e armazena
        audio_chunk = (indata * 32767).astype(np.int16)
        audio_data.append(audio_chunk)
        # Mostra indicador de volume para debug
        volume = np.abs(indata).mean()
        print('█' * int(volume * 50), end='\r')

def save_wave_file(filename, data):
    try:
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(2)  # 2 bytes por amostra
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(data.tobytes())
        filesize = os.path.getsize(filename) / 1024  # Tamanho em KB
        print(f"\nÁudio salvo: {filename} ({filesize:.1f} KB)")
        return True
    except Exception as e:
        print(f"\nErro ao salvar áudio: {e}")
        return False

def transcribe_and_type():
    global audio_data
    if not audio_data:
        print("\nNenhum áudio detectado!")
        return

    # Concatena os chunks de áudio
    recording_array = np.concatenate(audio_data)
    duration = len(recording_array) / SAMPLE_RATE
    print(f"\nDuração do áudio: {duration:.1f} segundos")

    if duration < 0.5:  # Menos de meio segundo
        print("Áudio muito curto!")
        return

    if save_wave_file("temp.wav", recording_array):
        try:
            print("Transcrevendo...")
            with open("temp.wav", "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    language="pt"
                )
            
            texto = transcription.text.strip()
            print(f"Transcrito: '{texto}'")
            if texto:
                pyautogui.write(texto + " ")
            else:
                print("Transcrição vazia!")

        except Exception as e:
            print(f"Erro na transcrição: {e}")
        finally:
            try:
                os.remove("temp.wav")
            except:
                pass

def main():
    global recording
    
    print("\nIniciando sistema de transcrição...")
    print("Configurando entrada de áudio...")
    
    try:
        stream = sd.InputStream(
            channels=CHANNELS,
            samplerate=SAMPLE_RATE,
            callback=audio_callback,
            dtype=np.float32
        )
        
        with stream:
            print("\n=== Sistema Pronto! ===")
            print("Pressione e segure CTRL + 1 para gravar")
            print("Solte para transcrever")
            print("CTRL + C para sair")
            
            while True:
                if keyboard.is_pressed('ctrl+1') and not recording:
                    recording = True
                    audio_data.clear()
                    print("\nGravando... (fale agora)")
                elif not keyboard.is_pressed('ctrl+1') and recording:
                    recording = False
                    print("\nProcessando...")
                    transcribe_and_type()
                time.sleep(0.01)

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()