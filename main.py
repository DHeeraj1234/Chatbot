from flask import Flask, render_template, request, jsonify
import aiml
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from google import google
import os

import pyowm

owm = pyowm.OWM('90a4ba7a37daeeb84b8a060070c4e839')  
observation =  owm.weather_at_place('hyderabad,india')   
w = observation.get_weather()  
temperature = w.get_temperature('celsius')  
tomorrow = pyowm.timeutils.tomorrow()  
wind = w.get_wind()  
dict1={'wind speed: ':str(wind['speed']),'CurrentTemp:':str(temperature['temp']),'MaxTemp:':str(temperature['temp_max']),'MinTemp:':str(temperature['temp_min'])}

chatbot=ChatBot('charlie')
chatbot.set_trainer(ListTrainer)

app = Flask(__name__)

chatbot=ChatBot(
    "Math & Time Bot",
    logic_adapters=[
    	"chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    #'input_text': 'Help me!',
    trainer='chatterbot.trainers.ListTrainer'
)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
	message = str(request.form['messageText'])

	kernel = aiml.Kernel()

	if os.path.isfile("bot_brain.brn"):
	    kernel.bootstrap(brainFile = "bot_brain.brn")
	else:
	    kernel.bootstrap(learnFiles = os.path.abspath("aiml/std-startup.xml"), commands = "load aiml b")
	    kernel.saveBrain("bot_brain.brn")

	# kernel now ready for use
	while True:
	    if message == "quit":
	        exit()
	    elif message == "save":
	        kernel.saveBrain("bot_brain.brn")
	    elif 'search:' in message:
			message=message[:-7]			
			search_results = google.search(message)
			bot_response = search_results[1].description
			print('here')
			print bot_response
	        #bot_response = kernel.respond(message)
	    elif 'send to:mobile' in message:
			execfile('mobilemsg.py')
			return jsonify({'status':'OK','answer':'sent succesfully'})			
	    elif 'send to:' in message:
			execfile('gmail.py')
			return jsonify({'status':'OK','answer':'ok'})
	    
	    elif 'weather' in message:
	    		str1=str(dict1)
			return jsonify({'status':'OK','answer':str1})
	    else:
		#	print('here')
			
			response=kernel.respond(message)
						
			print 'Bot:',	
			print(response)
			#return jsonify({'status':'OK','answer':response})			
			return jsonify({'status':'OK','answer':str(response)})	
	        # print bot_response
	    return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run(debug=True)
