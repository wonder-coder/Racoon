import pyaudio
import wave
import speech_recognition as sr
import assemblyai as aai

aai.settings.api_key = "#######################"


def listen_audio():
    frames = []
    FILE_URL = "input_audio.mp3"
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    try:
        x = 250
        poo = True
        while poo:
            x-=1
            if not x <= 0:
                data = stream.read(1024)
                frames.append(data)
            else:
                poo = False
                print("stop!")
    except KeyboardInterrupt:
        pass
    stream.stop_stream()
    stream.close()
    audio.terminate
    sound_file = wave.open("input_audio.mp3", "wb")
    sound_file.setnchannels(1)
    sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(44100)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL)
    print(transcript.text)
    return transcript.text
        
