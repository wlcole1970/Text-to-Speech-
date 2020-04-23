# Description : Program takes text from online article and converts to speech

#import libraries

from newspaper import Article
import nltk
from gtts import gTTS
import os

#get the article

article = Article('https://www.w3trainingschool.com/future-scope-of-python')

article.download() #downloads article

article.parse()

nltk.download('punkt')

#apply nlp
article.nlp()

#get the text and store to variable

my_text = article.text

#print text

print (my_text)

#choose language for speaach

language = 'en'

#convert text to speech

my_obj = gTTS(text=my_text, lang=language, slow=False)

#save the converted audio

my_obj.save('read_article.mp3')

#play file

os.system('start read_article.mp3')


