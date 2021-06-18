#Import the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os
from playsound import playsound


# get the article
article = Article('https://www.investopedia.com/terms/a/artificial-intelligence-ai.asp')
article.download()
article.parse()

nltk.download('punkt')

article.nlp()

#Get the articles text
mytext = article.text
#_>print(mytext)

language = 'en' #English

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("G:/rauf/STEPBYSTEP/Projects/SPEECH/Text to Speech/T2S Python/read_article.mp3")

# Playing the converted file
audio_file_path = 'G:/rauf/STEPBYSTEP/Projects/SPEECH/Text to Speech/T2S Python/read_article.mp3'

playsound(audio_file_path)

#here we go frineds we get our model played sound nearly 8 minutes cuz our arictle is not short
# anyway good job to convert text data to speech