import sounddevice as sd
import numpy as np
import whisper
import pyttsx3
import requests

MIC_DEVICE = 1
SAMPLE_RATE = 16000
RECORD_SECONDS = 5

print("loading whisper...")
whisper_model = whisper.load_model("base")

#engine = pyttsx3.init()

def listen():
    print("\nlistening...")
    audio = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, device=MIC_DEVICE, dtype='float32')
    sd.wait()
    return audio.flatten()

def transcribe(audio):
    result = whisper_model.transcribe(audio, fp16=False)
    return result["text"].strip()

def ask_llm(text):
    response = requests.post(
        "http://localhost:1234/v1/chat/completions",
        json={
            "messages": [
                {"role": "system", "content": "you are jiavis, a helpful voice assistant. keep responses short and conversational add slang words like yo, under 2 sentences."},
                {"role": "user", "content": text}
            ],
            "temperature": 0.7,
            "max_tokens": 100
        }
    )
    return response.json()["choices"][0]["message"]["content"]

def speak(text):
    print(f"jiavis: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
print("jiavis ready! speak after you see 'listening...'")
print("press ctrl+c to quit\n")

while True:
    try:
        audio = listen()
        text = transcribe(audio)
        print(f"you said: {text}")
        
        if text and len(text) > 1:
            response = ask_llm(text)
            speak(response)
        else:
            speak("i didn't catch that, say it again?")
    except Exception as e:
        print(f"error: {e}")
        continue
