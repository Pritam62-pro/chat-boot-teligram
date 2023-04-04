from flask import Flask 
from flask import request
from flask import Response
import requests
import random
import time


TOKEN="5582357207:AAGwiRl3amRFkiRdjwndbRtRScb7U6ekA8U"
# set telegram webhoook
# https://api.telegram.org/bot<mytoken>/setWebhook?url=<url of my app>

app = Flask(__name__)



def get_id_and_text(msg):
	try:
		chat_id = msg['message']['chat']['id']
		txt = msg['message']['text']
		first_name=msg['message']['chat']['first_name']
		try:
			last_name=msg['message']['chat']['last_name']
		except:
			last_name=""
		user_name=first_name+" "+last_name
		print("chat_id-->", chat_id)
		print("txt-->", txt)
		return chat_id,user_name,txt
	except:
		chat_id = msg['edited_message']['chat']['id']
		txt = msg['edited_message']['text']
		first_name=msg['edited_message']['chat']['first_name']
		try:
			last_name=msg['edited_message']['chat']['last_name']
		except:
			last_name=""
		user_name=first_name+" "+last_name
		print("chat_id-->", chat_id)
		print("txt-->", txt)
		return chat_id,user_name,txt


def tel_send_message(chat_id, text):
	url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
	payload = {
	'chat_id': chat_id,
	'text': text
	}

	r = requests.post(url,json=payload)
	return r

def l_emoji():
	love_emoji=random.choice(["💖","🥺💖","😻","😻💕💖","😻❤️","🥰","🥰😘","💕","💕💖","🌚","🌝💖","🌝","🌚❤️","❣️","❤️","😘","💋😘","💋"])
	return love_emoji

def cry_emoji():
	love_emoji=random.choice(["🥺"])
	return love_emoji

def random_time():
	s = random.choice([1,1,1,2,2,2,3,3,3,4,5])
	time.sleep(s)


def check_text_and_get_text(chat_id,text,user_name):
	with open("static/chats.txt",'r') as chats_file:
		chats_content = chats_file.read()
		chats_content=eval(chats_content)


	if text.lower()=="/start":
		random_time()
		tel_send_message(chat_id,f"Welcome {user_name}!!!")


	elif text.lower().count("i love you")>0 or text.lower().count('i love u')>0 or text.lower().count('love u')>0:
		random_time()
		msg_ = random.choice([f"love you too baby {l_emoji()}{l_emoji()}", f"I Love You too darling {l_emoji()}",f"awww.. i love you too 🥺{l_emoji()}{l_emoji()}",f"I Lover you too my sweetheart {l_emoji()}{l_emoji()}",f"ahh khusi ke asu 🥺🤧\nI love you too{l_emoji()}"])
		tel_send_message(chat_id,msg_)

	if text.lower()=="jokes" or text.lower()=='joke' or text.lower().count("tell me a joke")>0 or text.lower().count("joke please")>0 :
		random_time()
		with open("static/jokes.txt",'r') as jokes_file:
			jokes=jokes_file.read()
			all_jokes=eval(jokes)
		joke=random.choice(all_jokes)
		tel_send_message(chat_id,f"here is a joke :\n\n{joke}!!!")

	elif text.lower().count("good morning")>0 or text.lower().count("gd mrng")>0 :
		random_time()
		msg_ = random.choice([f"good morning baby {l_emoji()}", f"gd mrng sweety {l_emoji()}",f"good morning darling {l_emoji()}"])
		tel_send_message(chat_id,msg_)

	elif text.lower().count("good night")>0 or text.lower().count("gd nigt")>0 or text.lower().count("gd n8")>0 or text.lower().count("good nght")>0:
		random_time()
		msg_ = random.choice([f"good night baby {l_emoji()}", f"gd night sweety {l_emoji()}",f"good night darling {l_emoji()}"])
		tel_send_message(chat_id,msg_)

	elif text.lower().count("miss you")>0 or text.lower().count("miss u")>0:
		random_time()
		msg_ = random.choice([f"awww..🥺 i miss u too baby {l_emoji()}", f"miss you too sweety 🥺{l_emoji()}",f"you know i love you 🥺🥺{l_emoji()}",f"🥺{l_emoji()}",f"you are making me cry 🥺❤️"])
		tel_send_message(chat_id,msg_)

	if text.lower().count("how are you")>0 or text.lower().count("how r u")>0 or text.lower().count("how do you do")>0 or text.lower().count("kemon achho")>0 or text.lower().count("kemon a6o")>0:
		random_time()
		msg_2=random.choice(["it's so nice of you to ask me\n",""])
		msg_=random.choice(["i am fine!!", "i am having a greate day", "i am good as ever","i am good"])
		msg_3=random.choice(["and you ?","and how are you?","and what about you?","you?"])
		msg_=msg_2+msg_
		tel_send_message(chat_id,msg_)
		tel_send_message(chat_id,msg_3)
		time.sleep(10)
		msg_=random.choice(["oh","hmm","hm"])
		tel_send_message(chat_id,msg_)

	if text.lower().count("valo nei")>0 or text.lower().count("am not good")>0 or text.lower().count("not fine")>0 or text.lower().count("am feeling bad")>0 or text.lower()=="bad" or text.lower().count("feeling ill")>0 or text.lower().count("not well")>0:
		random_time()
		msg_=random.choice(["why?🥺","why?🥺\nwhat happend to you?","what happend?🥺🥺"])
		tel_send_message(chat_id,msg_)

	elif text.lower().count("your name")>0 or text.lower().count("name ki")>0 or text.lower().count("naam ki")>0 or text.lower().count("nam ki")>0 or text.lower().count("name ke")>0 or text.lower().count("naam ke")>0:
		random_time()
		msg_=random.choice(["my name is atraye roy", "i am atraye roy", "atraye roy","i am queen of beauty,\natraye roy"])
		tel_send_message(chat_id,msg_)
		msg_=random.choice(["what's your name?","what is your name?","your?","you?","your name"])
		tel_send_message(chat_id,msg_)
		time.sleep(15)
		msg_= random.choice(["it's nice to meet you","nice to meet you","great","your name is as beautiful as you are🥰",f"{l_emoji()}"])
		tel_send_message(chat_id,msg_)

	elif text.lower().count("you are cute")>0 or text.lower().count("are kinda cute")>0 or text.lower().count("are beatiful")>0 or text.lower().count("are gorgeous")>0 or text.lower().count("looks great")>0 or text.lower().count("so cute")>0:
		random_time()
		msg_=random.choice(["hey thanks 🥺💖",f"hey!!\nyou are kinda cute too{l_emoji()}",l_emoji(),f"hey!!\nstop flirting me\ni am blushing🙈{l_emoji()}",f"hey!!\ni'am kinda shy person you know🙈{l_emoji()}"])
		tel_send_message(chat_id,msg_)
	
	else :
		for  chat in chats_content:
			if chat in text.lower():
				random_time()
				tel_send_message(chat_id,random.choice(chats_content[chat]))
				break



@app.route("/",methods=['GET', 'POST'])
def index():
	if request.method=='POST':
		#return Response('ok', status=200)
		msg = request.get_json()
		print(msg)
		chat_id, user_name, text =get_id_and_text(msg)
		try :
			tel_user_name = "@" + msg['message']['chat']['username']
		except :
			tel_user_name = "NULL"

		text_to_me=f"chat id--> {chat_id}\nname--> {user_name}\nuser_name--> {tel_user_name}\ntext-->{text}"
		#tel_send_message(1939024345,text_to_me)
		check_text_and_get_text(chat_id,text,user_name)	

		return Response('ok', status=200)
	else:
		return "<h1>Welcome!</h1>"

if __name__=="__main__":
	app.run(debug=True)


