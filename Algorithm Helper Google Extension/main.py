from flask import Flask, jsonify, request
from flask_cors import CORS
import speech_recognition as sr
from threading import Thread
import pyttsx3
import resources.scrapper as scrapper 
import resources.sql as sql
import resources.gpt as gpt
import resources.audio as audio
import resources.textToVoice as TTV
import resources.PlayAudio as PA

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for all routes

def start_app():
    app.run(debug=True, use_reloader = False)    


mic_on = False# Global variable for keep track when mic is on 
@app.route('/mic', methods=['POST'])
def mic():
    global mic_on, ai
    
    PA.StopAudio()# Stops the audio if there is already one playing
    
    # Toggles mic to oppoosite of its state
    mic_on = not(mic_on)
    try:
        if mic_on:
            microphone.toggle_recording()
        else:
            microphone.toggle_recording()
            output = microphone.translate_recording()
            print(f'You said \'{output}\'')
            
            gpt_output = gpt.send_message(output, ai.get_history()).choices[0].message.content# Gets the response from AI
            print(gpt_output)# Log 
            
            TTV.create_audio(gpt_output)# Creates the audio base on the texyt
            PA.PlayAudio()# Playing the audio
    except:
        print('error, leetcode website not opened potentionally')
        pass
    return jsonify({'data': 'mic toggled'})
    

@app.route('/leetcode', methods=['POST'])
def start():
    global ai 
        
    received = request.get_json()
    
    print(f'Leetcode Website: {received} | start()')# log

    q_des = scrapper.scrape_lc_website(received)
    
    print(f'Description of the question:\n{q_des} | start()')# Log 
        
    ai = gpt.AI(q_des) 
    
    return jsonify({'data': 'Success'})

if __name__ == '__main__':
    microphone = audio.recorder()# Initializes microphone
    '''register_login = input('register or login? ')
    
    if register_login.lower() == 'register':
        username = input('make a username ')
        password = input('make a password ')
        sql.register_user(username, password)'''
    
    
    thread_app = Thread(target=start_app)
    thread_app.start()
