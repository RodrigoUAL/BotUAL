import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()
nltk.download('punkt')

training_data = []

classes=[]
context=[]
class_words = {}
class_context = {}
corpus_words = {}



training_data.append({"class":"hello", "context":"None","sentence":"sim"})

training_data.append({"class":"candidatura","context":"None", "sentence":"Quais são as candidaturas ?"})
training_data.append({"class":"candidatura","context":"None", "sentence":"Possíveis candidaturas ?"})
training_data.append({"class":"candidatura","context":"None", "sentence":"Quero saber as candidaturas"})
training_data.append({"class":"candidatura","context":"None", "sentence":"Candidaturas disponíveis"})
training_data.append({"class":"candidatura","context":"None", "sentence":"Queria candidatar-me"})
training_data.append({"class":"candidatura","context":"None", "sentence":"Como posso candidatar-me a ual?"})
training_data.append({"class":"candidatura","context":"None", "sentence":"Queria candidatarme"})
training_data.append({"class":"candidatura","context":"None", "sentence":"Gostaria de candidatarme"})
training_data.append({"class":"hello","context":"None", "sentence":"olá"})
training_data.append({"class":"hello","context":"None", "sentence":"ola"})
training_data.append({"class":"hello","context":"None", "sentence":"hello"})
training_data.append({"class":"hello","context":"None", "sentence":"hola"})
training_data.append({"class":"hello","context":"None", "sentence":"hey"})
training_data.append({"class":"hello","context":"None", "sentence":"oi"})

training_data.append({"class":"cumprimentos_2", "context":"RHello" ,"sentence":"tambem esta tudo bem"})
training_data.append({"class":"cumprimentos_2", "context":"RHello","sentence":"sim"})
training_data.append({"class":"cumprimentos_2", "context":"RHello","sentence":"tambem"})
training_data.append({"class":"cumprimentos_2", "context":"RHello","sentence":"também"})
training_data.append({"class":"cumprimentos_2", "context":"RHello","sentence":"tudo"})
training_data.append({"class":"cumprimentos_2", "context":"RHello","sentence":"esta"})
training_data.append({"class":"cumprimentos_2", "context":"RHello","sentence":"está"})
training_data.append({"class":"cumprimentos_2", "context":"RHello", "sentence":"sim tudo bem"})
training_data.append({"class":None, "context":"None", "sentence":"sim"})
training_data.append({"class":None, "context":"None", "sentence":"nao"})


training_data.append({"class":"cumprimentos_3","context":"RHello", "sentence":"nao"})
training_data.append({"class":"cumprimentos_3","context":"RHello", "sentence":"não"})
training_data.append({"class":"cumprimentos_3","context":"RHello", "sentence":"nao esta muito bem"})
training_data.append({"class":"cumprimentos_1","context":"None", "sentence":"tudo bem ?"})
training_data.append({"class":"cumprimentos_1","context":"None", "sentence":"tudo bem ?"})
training_data.append({"class":"cumprimentos_1","context":"None", "sentence":"tudo bem ?"})
training_data.append({"class":"cumprimentos_1","context":"None", "sentence":"tudo bem?"})
training_data.append({"class":"cumprimentos_1","context":"None", "sentence":"como esta?"})
training_data.append({"class":"cumprimentos_1","context":"None", "sentence":"Esta tudo bem consigo?"})
training_data.append({"class":"nome","context":"None", "sentence":"Como te chamas?"})
training_data.append({"class":"nome","context":"None",  "sentence":"Qual e o teu nome?"})
training_data.append({"class":"nome","context":"None",  "sentence":"Quem es?"})
training_data.append({"class":"perguntas_1","context":"continuar",  "sentence":"sim"})
training_data.append({"class":"respostas_1","context":"continuar",  "sentence":"nao"})
training_data.append({"class":"respostas_1","context":"continuar",  "sentence":"não"})
training_data.append({"class":"respostas_1","context":"continuar",  "sentence":"mais nada"})


#sugestoes="Sugestoes:(menu)Candidaturas(menu)Cursos(menu)Licenciatura(menu)Mestrado(menu)Doutoramento(menu)Enviar Email"

Multiple_Responses = {
    "cumprimentos_1":[{"respostas":["Esta tudo bem por aqui e por ai?","Sim esta tudo bem e consigo?","Por aqui tudo numa boa e contigo?"],"context":"RHello"}],
    "cumprimentos_2":[{"respostas": ["Ainda bem! Como lhe posso ajudar?","Bom saber :) . Como lhe posso ser util? ","Espero que continue bem disposto! E entao como lhe posso ajudar?"],"context":"None"}],
    "cumprimentos_3":[{"respostas": ["Que pena! Espero que o resto do seu dia possa correr melhor. Como lhe posso ajudar?","Isso é que é mau :( Mas nao desanime e pense positivo! . Como lhe posso ser util? ","Nao se preocupe, pois melhores dias virão! E entao como lhe posso ajudar?"],"context":"None"}],
    "perguntas_1":[{"respostas": ['Em que lhe posso ajudar?','Como lhe posso ser útil?','Diga que eu ajudo :)'],"context":"None"}],
    "respostas_1":[{"respostas": ['Se precisar de mais ajuda estarei por aqui. Ate a proxima!','Obrigado. Ate a uma proxima vez','Obrigado e tenha um resto de um bom dia!'],"context":"None"}],
    "hello":[{"respostas": ['Olá como posso ajudar?','Olá posso ajudar?','Olá como lhe posso ser útil?'],"context":"None"}],
    "nome":[{"respostas": ['Sou um assistente da Ual. Em que lhe poderei ajudar?','Sou assistente da UAL mas estou apto para responder as suas questoes sobre candidaturas'],"context":"None"}],
    None:[{"respostas": ["Nao entendi","desculpe podia ser mais especifico?","Nao percebi. Podia reformular?"],"context":"None"}]
    }








classes = list(set([a['class'] for a in training_data]))

for key in Multiple_Responses.keys():
  #classes.append(key)
  if Multiple_Responses[key][0].get("context") not in context:
    context.append(Multiple_Responses[key][0].get("context"))



for c in classes:

    class_words[c] = []
    class_context[c]=[]

for data in training_data:
    class_context[data['class']]=data['context']

    for word in nltk.word_tokenize(data['sentence']):

        if word not in ["?"]:

            stemmed_word = stemmer.stem(word.lower())

            if stemmed_word not in corpus_words:
                corpus_words[stemmed_word] = 1
            else:
                corpus_words[stemmed_word] += 1


            class_words[data['class']].extend([stemmed_word])








def calculate_class_score(sentence,contexto, class_name, show_details=True):
    score = 0


    if contexto in class_context[class_name]:
        score=score+1
        print("entra aqui pq encontrou contexto")
    for word in nltk.word_tokenize(sentence):


        if stemmer.stem(word.lower()) in class_words[class_name]:


            score += (1 / corpus_words[stemmer.stem(word.lower())])

            if show_details:
                print ("   match: %s (%s)" % (stemmer.stem(word.lower()), 1 / corpus_words[stemmer.stem(word.lower())]))



    return score


def classify(sentence,con):
    high_class = None
    high_score = 0
    print(class_context)
    for c in class_words.keys():

        score = calculate_class_score(sentence, con, c, show_details=False)

        if score > high_score:
            high_class = c
            high_score = score


        if high_score==1:
            high_class=None
            high_score=0
    return high_class, high_score


#Bibliotecas
import random
import string
#import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
#import numpy as np
import warnings
import pandas as pd
#from nltk.stem.snowball import SnowballStemmer
from nltk.stem import RSLPStemmer





#Ignorar mensagens de aviso
warnings.filterwarnings('ignore')

#Download pacotes NLTK
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('rslp', quiet=True)



#Base de dados[ keywords,texto,links ]
data = {

        'keywords':[
                    'CANDIDATURA',#0
                    'DOCENTE',#1
                    'concurso institucional 12 ano',#2
                    'acesso para maiores de 23 anos',#3
                    'concurso especial de acesso para estudantes internacionais',#4
                    'programas de acumulação de conhecimentos',#5
                    'mudança de par instituição/curso',#6
                    'titulares de cursos superiores ou cursos médios',#7
                    'titulares de curso de especialização tecnológica',#8
                    'titulares de diploma de técnico profissional',#9
                    'reingresso',#10
                    'Cursos',#11
                    'Licenciatura',#12
                    'Mestrado',#13
                    'Doutoramento',#14
                    'Administração de unidades de saude',#15
                    'Arquitetura',#16
                    'CIÊNCIAS DA COMUNICAÇÃO',#17
                    'DIREITO',#18
                    'ECONOMIA',#19
                    'ENGENHARIA ELETRÓNICA E DE TELECOMUNICAÇÕES',#20
                    'ENGENHARIA INFORMÁTICA',#21
                    'GESTÃO',#22
                    'GESTÃO DO DESPORTO',#23
                    'HISTÓRIA',#24
                    'INFORMÁTICA DE GESTÃO',#25
                    'PSICOLOGIA',#26
                    'RELAÇÕES INTERNACIONAIS',#27
                    'COMUNICAÇÃO APLICADA',#28
                    'DIREITO',#29
                    'ENGENHARIA INFORMÁTICA E DE TELECOMUNICAÇÕES',#30
                    'ESTUDOS DA PAZ E DA GUERRA NAS NOVAS RELAÇÕES INTERNACIONAIS',#31
                    'GESTÃO DE EMPRESAS',#32
                    'HISTÓRIA ARQUEOLOGIA PATRIMÓNIO',#33
                    'PSICOLOGIA CLÍNICA E DE ACONSELHAMENTO',#34
                    'RELAÇÕES INTERNACIONAIS', #35
                    'Enviar Email', #36
                    'Faculdade', #37
                    'Contactos', #38
                    'Propinas', #39
                    'Direito Dtr', #40
                    'História Dtr', #41
                    'Media Sociedade Dtr', #42
                    'Relações Internacionais Dtr', #43
                    'Ver Sugestoes' #44

                    ],

        'texto':[ #0
                 '(menu)Concurso Inst 12ºano(menu)Acesso +23(menu)Estudantes Inter.(menu)Progr. Acc. Conhec.(menu)Mud. Par Ins/Curso(menu)Titul. Cursos Sup.(menu)Titul. Cursos Espec.(menu)Titul. Dipl. T.Prof.(menu)Reingresso',
                  #1
                 'https://autonoma.pt/docentes/',
                  #2
                 'https://autonoma.pt/a_autonoma/concurso-institucional-12o-ano/',
                 #3
                 'https://autonoma.pt/maiores-de-23-ano2020/',
                 #4
                 'https://autonoma.pt/a_autonoma/concurso-especial-de-acesso-para-estudantes-internacionais/',
                 #5
                 'https://autonoma.pt/a_autonoma/programas-de-acumulacao-de-conhecimentos/',
                 #6
                 'https://autonoma.pt/a_autonoma/mudanca-de-par-instituicao-curso/',
                 #7
                 'https://autonoma.pt/a_autonoma/titulares-de-cursos-superiores-ou-cursos-medios/',
                 #8
                 'https://autonoma.pt/a_autonoma/titulares-de-curso-de-especializacao-tecnologica/',
                 #9
                 'https://autonoma.pt/a_autonoma/titulares-de-diploma-de-tecnico-superior-profissional/',
                 #10
                 'https://autonoma.pt/a_autonoma/reingresso/',
                 #11
                 '(menu)Licenciatura(menu)Mestrado(menu)Doutoramento',
                 #12 #Cursos Licenciatura
                 '(menu)Unidades De Saúde(menu)Arquitetura(menu)C. Da Comunicação(menu)Direito(menu)Economia(menu)Eng. Eletrónica(menu)Eng. Informática(menu)GESTÃO(menu)Gestão do Desporto(menu)História(menu)Informática de Gest.(menu)Psicologia(menu)Relações Inter',
                 #13 Mestrado
                 '(menu)Comunicação Aplic.(menu)Direito(menu)Eng. Inf. e Telec.(menu)Estudos Paz e Guerra\n(menu)Gestão De Empresas(menu)Hist. Arqueologia Patr.(menu)Psicol. Clínica(menu)Relações Inter.',
                 #14 Doutoramento
                 '(menu)Direito Dtr.(menu)História Dtr.(menu)Media e Sociedade Dtr.(menu)Relações Inter. Dtr.',
                 #15
                 'https://autonoma.pt/cursos/administracao-de-unidades-de-saude/',
                 #16
                 'https://autonoma.pt/cursos/arquitectura/',
                 #17
                 'https://autonoma.pt/cursos/ciencias-da-comunicacao/',
                 #18
                 'https://autonoma.pt/cursos/direito/',
                 #19
                 'https://autonoma.pt/cursos/economia/',
                 #20
                 'https://autonoma.pt/cursos/engenharia-eletronica-e-de-telecomunicacoes/',
                 #21
                 'Para se candidatar necessita das seguintes provas de ingresso:(bot)Matemática(bot)Para mais informações pode aceder a este link:(bot)https://autonoma.pt/cursos/engenharia-informatica/',
                 #22
                 'https://autonoma.pt/cursos/gestao/',
                 #23
                 'https://autonoma.pt/cursos/gestao-do-desporto/',
                 #24
                 'https://autonoma.pt/cursos/historia/',
                 #25
                 'https://autonoma.pt/cursos/informatica-de-gestao/',
                 #26
                 'https://autonoma.pt/cursos/psicologia-2/',
                 #27
                 'https://autonoma.pt/cursos/relacoes-internacionais/',
                 #28
                 'https://autonoma.pt/cursos/mestrado-em-comunicacao-aplicada/',
                 #29
                 'https://autonoma.pt/cursos/direito-2/',
                 #30
                 'https://autonoma.pt/cursos/engenharia-informatica-e-de-telecomunicacoes/',

                 'https://autonoma.pt/cursos/guerra-e-paz-nas-novas-relacoes-internacionais/',

                 'https://autonoma.pt/cursos/gestao-de-empresas/',

                 'https://autonoma.pt/cursos/historia-arqueologia-e-patrimonio/',

                 'https://autonoma.pt/cursos/psicologia-clinica-e-de-aconselhamento/',

                 'https://autonoma.pt/cursos/relacoes-internacionais-2/', #35

                 'está na secção de enviar um mail. insira um assunto(bot)(menu)Cancelar', #36

                 'https://autonoma.pt/a_autonoma/a-autonoma/', #37

                 'Contacto geral: 213 177 600 <br> Mail geral: geral@autonoma.pt', #38

                 'https://autonoma.pt/tabela-de-propinas-2019-2020-2-2/', #39

                 'https://autonoma.pt/cursos/doutoramento-em-direito/', #40

                 'https://autonoma.pt/cursos/doutoramento-em-historia/', #41

                 'https://autonoma.pt/cursos/doutoramento-em-media-e-sociedade-no-contexto-da-comunidade-dos-paises-de-lingua-portuguesa/', #42

                 'https://autonoma.pt/cursos/doutoramento-em-relacoes-internacionais-geopolitica-e-geoeconomia/', #43
                 '(menu)Cursos(menu)Candidaturas(menu)Propinas(menu)Contacto' #44
                 ],

        'links':[
                 '', #0
                 '', #1
                 '0', #2
                 '0',#3
                 '0',#4
                 '0',#5
                 '0',#6
                 '0',#7
                 '0',#8
                 '0',#9
                 '0',#10
                 '',#11
                 '11',#12
                 '11',#13
                 '11',#14
                 '12',#15
                 '12',#16
                 '12',#17
                 '12',#18
                 '12',#19
                 '12',#20
                 '12',#21
                 '12',#22
                 '12',#23
                 '12',#24
                 '12',#25
                 '12',#26
                 '12',#27
                 '13',#28
                 '13',#29
                 '13',#30
                 '13',#31
                 '13',#32
                 '13',#33
                 '13',#34
                 '13', #35
                 '', #36
                 '', #37
                 '', #38
                 '', #39
                 '14', #40
                 '14', #41
                 '14', #42
                 '14',#43
                 ''#44
                 ]


        }



# Colocar a base de dados no dataframe
df = pd.DataFrame(data).applymap(str.lower)


#extrair os dados de cada coluna no formato de lista
texto = list(df['texto'])
keywords = list(df['keywords'])
links = list(df['links'])


#copiar a lista original com as keywords
keywordbackup = list(df['keywords'])
keywordprime = list(df['keywords'])
#cada posicao do array ira conter a opcao de cada submenu de uma keyword
menu_opcoes=[]

#iniciação da flags
submenu=False
bot_activo = True
multiple_message=0;
none_answer=0;
new_context="None"
lastindex=''

#Pre processamento (retirar pontuação , converter palavras para a sua root, converter para minusculas)
remove_punct_dict = dict( ( ord(punct),None) for punct in string.punctuation)

def string_steem(text):

  string_steem=[]
  stemmer = RSLPStemmer()

  for i in text.split():
    try:
      string_steem.append(stemmer.stem(i.lower().translate(remove_punct_dict)))
    except:
      string_steem.append('')
  return ' '.join(i for i in string_steem)



def check_submenu(text):
  global menu_opcoes
  global submenu
  global lastindex
  global links
  global texto
  global keywords
  menu_opcoes=[]

  if str(lastindex) in links:

    submenu=True
    for i in range(len(texto)):
      if links[i]==str(lastindex):
        menu_opcoes.append(keywords[i])
  else:
    submenu=False



#### FUNCOES ####

#Send mail


#Generate the response
def resposta(text,context):

  global lastindex
  global aux
  global keywords
  global multiple_message
  global none_answer
  global new_context
  #inicio da string
  bot_resposta = ''

  multiple_message=0
  none_answer=0

  #adiciona a resposta do user ao array
  keywords.append(text)

  #Cria TfidfVectorizer Object
  TfidfVec2 = TfidfVectorizer()

  #Convert o texto para uma matrix of TF-IDF features
  tfidf2 = TfidfVec2.fit_transform(keywords)

  #mede a similaridade (similarity scores)
  vals = cosine_similarity(tfidf2[-1], tfidf2)

  #obtem o index correspondente mais similar ao texto do input do user
  idx = vals.argsort()[0][-2]

  #guarda index na variavel global
  lastindex=str(idx)

  #Reduce the dimensionality of vals
  flat = vals.flatten()

  #sort the list in ascending order
  flat.sort()

  #vai buscar o 2º melhor score ja que o 1º e o propria keyword
  score = flat[-2]

  #teste

  #se score=0 entao nao encontrou nenhum texto similar
  print("a entrar")
  if score == 0:
    try:

      bot_resposta= bot_resposta + random.choice(Multiple_Responses[classify(aux,context)[0]][0].get('respostas'))
      new_context=Multiple_Responses[classify(aux,context)[0]][0].get("context")
      multiple_message=1
      print("texto",aux)
      print("set contexto",new_context)
      print("classificacao",classify(aux,context))

      if classify(aux,context)[0]==None:
          none_answer=1



    except:

      bot_resposta = bot_resposta + resposta(string_steem(classify(aux,context)[0]),context)


    return bot_resposta

  else:
    print(idx)
    bot_resposta = bot_resposta + texto[idx]
    check_submenu(text)

  return bot_resposta



for i in range(len(keywords)):

  keywords[i] = string_steem(keywords[i])
  keywordbackup[i] = string_steem(keywordbackup[i])




#### MAIN #############
def post_response(user_input,context):

    global submenu
    global multiple_message
    global keywords
    global none_answer
    global lastindex
    global new_context

    keywords = []
    keywords = keywordbackup.copy()
    user_input = string_steem(user_input)
    resposta(user_input,context)

    LISTA_RESPOSTAS_FINAIS=["Como poderei ajudar-lhe mais?","O que deseja saber mais?","Estarei ao seu dispor se necessitar mais ajuda","Deseja saber mais alguma coisa?"]

    if multiple_message!=1 and  str(lastindex)!='44':
        if submenu==False:
            new_context="continuar"
            return "(bot)"+random.choice(LISTA_RESPOSTAS_FINAIS)

    if none_answer==1 and str(lastindex)!='44':

        return "(bot)(menu)Ver Sugestoes(menu)Enviar Email"

    return 0





def pre_response(user_input,context):

    global keywords
    global keywordbackup
    global lastindex
    global submenu
    global multiple_message

    keywords = []
    keywords = keywordbackup.copy()
    user_response = user_input
    LISTA_RESPOSTAS_OPCOES = ["Encontrei informação acerca de "+keywordprime[int(lastindex)], "Sobre "+keywordprime[int(lastindex)]+" encontrei isto para si"]
    LISTA_RESPOSTAS_MENU =["Dentro de "+keywordprime[int(lastindex)]+ " temos estas opcoes","Para informações acerca de "+keywordprime[int(lastindex)]+ " tem como opcoes:","Temos esta lista para si relativamente a "+keywordprime[int(lastindex)]]
    user_response = string_steem(user_response)
    resposta(user_response,context)


    if str(lastindex)=='44':
        return "(bot)Sugestoes:"

    if multiple_message!=1:

        if submenu==True:
            return "(bot)"+random.choice(LISTA_RESPOSTAS_MENU)
        if submenu==False:
            return "(bot)"+random.choice(LISTA_RESPOSTAS_OPCOES)

    return 0



def get_context(user_input,context):
    global multiple_message
    global keywords
    global keywordbackup
    global new_context
    if new_context!='continuar':
        keywords = []
        keywords = keywordbackup.copy()
        #user_response = string_steem(user_input)
        resposta(user_input,context)
    return new_context

def bot_app(user_input,context):

    #print("Bot da Ual: Ola. Em que posso ajudar?")


    global keywords
    global keywordbackup
    global aux
    global submenu
    global menu_opcoes
    keywords = []
    keywords = keywordbackup.copy()
    user_response = user_input
    aux = user_response
    user_response = string_steem(user_response)


    #if lastindex == '36':
     #   lastindex=''
    #    return 36
    if user_response!='bye':


        if submenu==True:
          try:

            return "(bot)"+resposta(menu_opcoes[int(user_response)-1],context)
            submenu=False
          except: #se numero da opcao estiver incorrecto
            submenu=False
            return "(bot)"+ resposta(user_response,context)
        else:
          return "(bot)"+ resposta(user_response,context)
    else:
        #bot_activo=False
        return "(bot)Chat with you later !"
