# BotUAL


## **INTRODUÇÃO**

Projecto final de curso que consiste em desenvolver um chatbot para a Universidade Autónoma de Lisboa de forma a funcionar num website e no Messenger do Facebook para esclarecer dúvidas acerca de candidaturas , cursos , e outras informações que os candidatos possam perguntar. 


## **FICHEIROS**

Botual/teste_nltk.py - Ficheiro que contem o código principal do bot que contem as funções que recebem as perguntas dos utilizadores, devolvendo as respectivas respostas

Botual/flask_app.py - Ficheiro que permite reencaminhar as respostas para o respectivo utilizador destinatário quer facebook ou no website
        

## **COMO USAR**

Poderá usar directamente em https://botual.pythonanywhere.com/

-OU-

Correr com as seguintes definições:

Source Code: /home/Botual/mysite

Working directory: /home/Botual/

Static Files : URL- /static/ Directory- /home/Botual/mysite/assets

Force HTTPS: Enabled



Para o Facebook:

Criar uma App no facebook developers

Activar o Webhooks e subscrever ao message_sends

Activar o Messenger e gerar o Access Token e Verify Token coloca-lo no ficheiro flask_app.py

Criar uma pagina no facebook e associar à app criada








## **BIBLIOTECAS USADAS**

[teste_nltk.py]

nltk - LancasterStemmer,RSLPStemmer

TfidfVectorizer

cosine_similarity

pandas

random 

string

[flask_app.py]

flask - Flask , session , render_template, request

flask_mail - Mail , Message

pymessenger.bot - Bot

os

sys

speech_recognition

urllib.request - urlopen

subprocess
        

## **AUTORES**

André Martins - 

Nuno Paradinha - 

Rodrigo Araújo - https://github.com/RodrigoUAL/BotUAL

Ricardo Clemente- https://github.com/ric-clemente
