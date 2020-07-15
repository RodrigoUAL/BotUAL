from flask import Flask, session, render_template, request

from teste_nltk import bot_app,pre_response,post_response,get_context
from flask_mail import Mail, Message
import time
from pymessenger.bot import Bot
import os
import sys
import speech_recognition as sr
from urllib.request import urlopen
import subprocess

r = sr.Recognizer()
app = Flask(__name__)

app.secret_key = 'teste'

#inicializações das variaveis de sessao para o facebook
emailfb={}
assuntofb={}
assunto_textfb={}
corpo_textfb={}
contextfb={}

#access e verify token para o facebook app
ACCESS_TOKEN = 'EAAiZCzThIjXgBANNU0KBZBu1MbYVZCce9xgqFnwSVaiNA3todrXojgu6hemPC91t5cP50hqRCQxm0rtEUXZCnUI6uL7ptqh6TmHOBQO5zNmwlnGqzjeVyZBl5DC4RbvC7rV2ZCjFIzRx1h8SQYErfaYZCGfhdWe8uqkJwQOmvMQXwZDZD'
VERIFY_TOKEN = 'verify'
FB_MESSENGER_URI = "https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN


bot = Bot(ACCESS_TOKEN)


#configuração do servidor SMTP
app.config.update(
	DEBUG=True,
	
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'botualico@gmail.com',
	MAIL_PASSWORD = 'qwertyyy123'
	)

mail = Mail(app)

app.extensions['mail'].debug = 0

#função que envia email
def sendmail(assunto,corpo):
	with app.app_context():
		msg = Message(assunto,
			sender="botualico@gmail.com",
			recipients=["botualico@gmail.com"])
		msg.body = corpo
		mail.send(msg)




# --FACEBOOK---#
@app.route("/facebook", methods=['GET'])

#Login na APP
def verify():

    if request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")==VERIFY_TOKEN:
            return "falha na no token",403
        return request.args.get("hub.challenge"),200
    return "Messenger do facebook ligado",200

@app.route("/facebook", methods=['POST'])




#Funcao que permite processar as mensagens do utilizador do facebook
def messenger():
   data = request.get_json()
   logdata(data)
   buttons=[]
   global emailfb,assuntofb,assunto_textfb,corpo_textfb,contextfb

   for event in data['entry']:
      messaging = event['messaging']
      for message in messaging:
        if message.get('message'):
            #Facebook Messenger ID for user so we know where to send response back to
            recipient_id = message['sender']['id']

            if recipient_id not in contextfb:
                contextfb.update( {recipient_id : 'None'} )

            if recipient_id not in emailfb:
                emailfb.update( {recipient_id : False} )
                assuntofb.update( {recipient_id : False} )
                assunto_textfb.update( {recipient_id : ''} )
                corpo_textfb.update( {recipient_id : ''} )



            if message['message'].get('text'):


                context_save=contextfb.get(recipient_id)
		
		#Gera as respostas ao utilizador
                response_sent_text = get_message(message['message'].get('text'),recipient_id)

                pre_response_sent_text = get_pre_message(message['message'].get('text'),recipient_id)

                post_response_sent_text = get_post_message(message['message'].get('text'),recipient_id)

                new_context=get_context(message['message'].get('text'),context_save)

                contextfb[recipient_id]=new_context


                
                if (pre_response_sent_text != 0 and emailfb.get(recipient_id)==False):


                    if check_menu(response_sent_text)==True:

                        buttons=create_buttons(response_sent_text,message['message'].get('text'))
                        send_quickreply(recipient_id, pre_response_sent_text,buttons)
                        
                    else:
                        send_message(recipient_id, pre_response_sent_text)

                        

                if (post_response_sent_text != 0 and emailfb.get(recipient_id)==False):

                    if check_menu(post_response_sent_text)==True:
                        buttons=create_buttons(post_response_sent_text,message['message'].get('text'))
                        response_sent_text=response_sent_text.split('(bot)')
                        send_quickreply(recipient_id, response_sent_text[1],buttons)
                    
                    



                if (check_menu(response_sent_text)==False and check_menu(post_response_sent_text)==False):

                    response_sent_text=response_sent_text.split('(bot)')
                    for i in range(1,len(response_sent_text)):
                        send_message(recipient_id, response_sent_text[i])
                    if post_response_sent_text!=0 and emailfb.get(recipient_id)==False:
                        send_message(recipient_id, post_response_sent_text)

                if emailfb.get(recipient_id)==True:

                    if check_menu(response_sent_text)==True:
                        response_sent_text=response_sent_text.split('(bot)')
                        buttons=create_buttons(response_sent_text[2],message['message'].get('text'))
                        send_quickreply(recipient_id, response_sent_text[1],buttons)
                    else:#ultima msg do email
                        response_sent_text=response_sent_text.split('(bot)')
                        for i in range(1,len(response_sent_text)):
                            send_message(recipient_id, response_sent_text[i])
                        emailfb[recipient_id]=False
                        emailfb.pop(recipient_id, None)
            
            #Se a mensagem conter algum attachment como por exemplo o audio para que se possa usar a funçao de reconhecimento de voz
            if message['message'].get('attachments'):
                try:
                    os.remove("test.mp4")
                    os.remove("test.wav")
                except:
                    response_sent_nontext = message['message'].get('attachments')[0].get('payload').get('url')
                    #send_message(recipient_id, response_sent_nontext)
                    mp4file = urlopen(response_sent_nontext)
                    #mp4file=urlopen('https://cdn.fbsbx.com/v/t59.3654-21/98979868_583150605671753_6905400662767435776_n.mp4/audioclip-1590074054000-1695.mp4?_nc_cat=110&_nc_sid=7272a8&_nc_oc=AQl2J5naMe1Bld2jCefuWZ8cROguQ0S0hsPypQ3lQ8vGf9oZ62J0KaHv9DzlxHDyEFKIQUoAspm2EiO8JHM7Hkp7&_nc_ht=cdn.fbsbx.com&oh=80a322e9b7f02c98b4cb1ce1a2d19dc2&oe=5EC84834')
                    with open("test.mp4", "wb") as handle:
                        handle.write(mp4file.read())

                    cmdline = ['avconv',
                               '-i',
                               'test.mp4',
                               '-vn',
                               '-f',
                               'wav',
                               'test.wav']
                    subprocess.call(cmdline)


                    with sr.AudioFile('test.wav') as source:
                        audio = r.record(source)
                    
                    textfb = r.recognize_google(audio, language = "pt-PT")
                    respostafb=get_message(textfb,recipient_id)
                    send_message(recipient_id, respostafb)
                    os.remove("test.mp4")
                    os.remove("test.wav")
   return "Message Processed"


#Devolve a resposta posterior a resposta principal ao utilizador
def get_post_message(user_response,r_id):
    global contextfb

    response= post_response(user_response,contextfb.get(r_id))
    try:
        split_string=response.split("(bot)")
        response=split_string[1]
        return response
    except:
        return response

#Devolve a resposta anterior a resposta principal
def get_pre_message(user_response,r_id):
    global contextfb
    response= pre_response(user_response,contextfb.get(r_id))
    try:
        split_string=response.split("(bot)")
        response=split_string[1]
        return response
    except:
        return response

#Devolve a resposta principal ao utilizador
def get_message(user_response,r_id):

    global emailfb,assuntofb,assunto_textfb,corpo_textfb,contextfb

    
    if emailfb.get(r_id)==False:

        response=bot_app(user_response,contextfb.get(r_id))
        if response=='(bot)está na secção de enviar um mail. insira um assunto(bot)(menu)cancelar':
            #emailfb=True

            emailfb[r_id]=True


        return response



    if emailfb.get(r_id)==True and assuntofb.get(r_id)==False:
        if user_response=='cancelar':
            post_text=get_post_message('email',r_id)
            return '(bot)operação cancelada(bot)'+post_text
        else:
            assunto_textfb[r_id]=user_response
            assuntofb[r_id]=True
            emailfb[r_id]=True
        return "(bot)Insira o corpo (deixe o seu email ou nº de telefone para ser contactado)(bot)(menu)cancelar"

 
    if emailfb.get(r_id)==True and assuntofb.get(r_id)==True:

        if user_response=='cancelar':
            assuntofb[r_id]=False
            assuntofb.pop(r_id, None)
            assunto_textfb.pop(r_id, None)
            post_text=get_post_message('email',r_id)
            return '(bot)operação cancelada(bot)'+post_text
        else:

            corpo_textfb[r_id]=user_response
            #emailfb[r_id]=False
            assuntofb[r_id]=False
            sendmail(assunto_textfb.get(r_id),corpo_textfb.get(r_id))

            #emailfb.pop(r_id, None)
            assuntofb.pop(r_id, None)
            corpo_textfb.pop(r_id, None)
            assunto_textfb.pop(r_id, None)
            post_text=get_post_message('email',r_id)

        return '(bot)Email enviado com sucesso(bot)'+post_text


#usa a biblioteca PyMessenger para enviar as respostas geradas ao utilizador
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


#verifica se a mensagem contem a tag (menu)
def check_menu(text):
    if '(menu)' in str(text):
        return True
    else:
        return False

#Cria botoes caso haja a tag (menu)
def create_buttons(text,title):
    b=[]
    count=0
    m=text.split('(menu)')
    for i in m:
        count=count+1
        if i!='' and i!='(bot)':
            b.append({"content_type" : "text" , "title" : i , "payload" : title+str(count) })
 
    return b

#Funçao que permite criar botoes no facebook
def send_quickreply(reply_token, text, answers):
    global FB_MESSENGER_URI
    data = {
        "recipient": {"id": reply_token},
        "message": {"text": text}
    }
    if answers:
        data["message"]["quick_replies"] = answers
    r = requests.post(FB_MESSENGER_URI, json=data)
    if r.status_code != requests.codes.ok:
        print(r.content)


if __name__ == "__main__":

    app.run()




#--WEBSITE--
@app.route("/")
def adder_page():
    return render_template("new.html")




@app.route("/get")

#Funçao que restorna as respostas ao utilizador
def get_bot_response():
    

#Criaçao das variaveis de sessao

    if 'context' not in session:
        session['context']="None"



    if 'email' not in session:
        session['email']=False
        session['assunto']=False
        session['corpo_text']=''
        session['assunto_text']=''



    
    if session.get('email')==False:
        user_response = request.args.get('msg')

        response=bot_app(user_response,session.get('context'))
        pre_text=pre_response(user_response,session.get('context'))
        post_text=post_response(user_response,session.get('context'))
        session['context']=get_context(user_response,session.get('context'))
        
        
        if response=='(bot)está na secção de enviar um mail. insira um assunto(bot)(menu)cancelar':


            session['email']=True

        
        

        if pre_text==0 and post_text!=0:
            return response+post_text
        if pre_text==0 or session.get('email')==True:
            return response
        if post_text!=0:

            return pre_text+response+post_text
        if post_text==0:
            return pre_text+response


    if session.get('email')==True and session.get('assunto')==False:
		
        session['assunto_text']=request.args.get('msg')
        if session['assunto_text']=="cancelar":
            session['assunto']=False
            session['email']=False
            post_text=post_response('Email')
            return '(bot)Operacao cancelada'+post_text
        else:
            session['assunto']=True
        return '(bot)Insira o corpo (deixe o seu email ou nº de telefone para ser contactado)(bot)(menu)cancelar'

    if session.get('email')==True and session.get('assunto')==True:

        session['corpo_text']=request.args.get('msg')
        session['email']=False
        session['assunto']=False





        post_text=post_response('Email')
        if session['corpo_text']=="cancelar":
            session.pop('corpo_text', None)
            session.pop('assunto_text', None)
            return '(bot)Operacao cancelada'+post_text


        sendmail(session.get('assunto_text'),session.get('corpo_text'))

        session.pop('assunto_text', None)
        return '(bot)Email enviado com sucesso'+post_text
