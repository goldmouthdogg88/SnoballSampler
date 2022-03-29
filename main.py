from bs4 import BeautifulSoup
from bs4.element import Comment
#import urllib.request
from urllib.request import Request, urlopen

# NLTK
import nltk
nltk.download('punkt')
#from nltk.tokenize import word_tokenize


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

# http://www.nytimes.com/2009/12/21/us/21storm.html
  
#html = urllib.request.urlopen('https://towardsdatascience.com/how-to-scrape-the-dark-web-53145add7033').read()
#print(text_from_html(html))

  
req = Request('https://towardsdatascience.com/how-to-scrape-the-dark-web-53145add7033', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
text = text_from_html(webpage)
#tokens = word_tokenize(text_data)

allWords = nltk.tokenize.word_tokenize(text)
allWordDist = nltk.FreqDist(w.lower() for w in allWords)

stopwords = nltk.corpus.stopwords.words('english')
allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)  