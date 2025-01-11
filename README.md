# About Program
This is a google extension program that activates when you open leetcode.com or hackerrank.com and start solving problem. This application uses chrome's extension dev services to know when specific URLs is open.

When user is solving a problem, the description of the problem is scrapped from the current website and sent to back end to process allowing user to press on the microphone, indicating when they started talking and press again to indicate when they stop. Base on what you said, the application will respond accordingly


# Setup
Created a .env file in main.py directory

insert 'gpt_key = YOUR_OPENAI_KEY' into .env and save

Go into google chrome extension dev and add a extension, choosing the file to be this repo. 

When solving a problem or intend to, open repo in vsCode and run the program on main.py to replicate a local backend server
