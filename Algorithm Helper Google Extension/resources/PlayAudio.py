import pyaudio
import wave

# Define the chunk size
CHUNK = 1024

stream = None
p = None

def PlayAudio():
    global stream, p
    wf  = wave.open('resources/audio_data/output.wav', 'rb')
    p = pyaudio.PyAudio()
    
    # Open a stream with the appropriate settings
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

    # Read data in chunks and play
    data = wf.readframes(CHUNK)
    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # Close the stream and PyAudio, then resets stream and p
    stream.close()
    stream = None
    p.terminate()
    p = None
    
def StopAudio():
    global stream, p
    
    if stream and p:
        stream.close()
        p.terminate()

