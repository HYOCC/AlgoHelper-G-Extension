import pyaudio
import wave
import threading
import time
import os
import speech_recognition as sr


class recorder():
    def __init__(self):
        self.recording = False
        self.r = sr.Recognizer()# Creates the speech to text system
    
    def toggle_recording(self):
        if self.recording:
            self.recording = False
            self.save_recording()
        else:
            self.recording = True 
            self.frames = []
            threading.Thread(target=self.record).start()
    
    def record(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024, input_device_index=0)
        
        while self.recording:
            data = stream.read(1024)
            self.frames.append(data)

        stream.stop_stream()
        stream.close()
        audio.terminate()
    
    def save_recording(self):
        folder = 'resources/audio_data'
        if not os.path.exists(folder):
            os.makedirs(folder)
        # Generate the filename with the current timestamp
        self.filename = os.path.join(folder, "recording" + ".wav")
        
        with wave.open(self.filename, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(self.frames))
            wf.close()
            print(f"Recording saved as {self.filename}")
    
    def translate_recording(self):
        audio_file = sr.AudioFile(self.filename)  
        with audio_file as source:
            self.r.adjust_for_ambient_noise(source, duration=.2)
            audio_data = self.r.record(source)
        try:
            text = self.r.recognize_google(audio_data)
            print("Transcription:", text)
            return text
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        

    
    


if __name__ == "__main__":
    audio  = recorder()
    
    while True:
        toggle = input('On or Off ')
        
        if toggle == 'Off':
            audio.toggle_recording()
            audio.translate_recording()
        elif toggle == 'On':
            audio.toggle_recording()