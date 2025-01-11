from openai import OpenAI
import os
from dotenv import load_dotenv

# Loads the api_key from a secure file called openAI_key.env
load_dotenv()
api_key = os.getenv('gpt_key')

if api_key: # Checks for valid api_key
    client = OpenAI(api_key=api_key) 
else:
    print('failed get OpenAI API Key\nPlease make sure filed is called openAI_key.env and inside contains OPENAI_API_KEY=\'YOUR KEY\'')

# sends message and forumulate ans
def send_message(message:str, history:list):
    print(f'sending message: \'{message}\' to openai')# Log
    history.append({'role': 'user', 'content': message})
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=history
    )
    
    return completion
    
class AI():
    def __init__(self, question:str):
        self.instruction = f'You are tasked to help the user solve the follow lc problem:\n{question}\nDont just solve it, the user will  walk you through how they will solve and you will give contsructive feed back. never directly solve it. You will be interacting with the user through voice so dont structure your respond, just respond in plain text'
        self.chat_history = [
            {'role':'system', 'content':self.instruction}
        ]
    
        
    def get_history(self):
        return self.chat_history
