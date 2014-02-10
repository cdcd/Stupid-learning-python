import random
from urllib import urlopen
import sys

word_url = "http://learncodethehardway.org/words.txt"
words = []

phrases = {
           "class ###(###):":
           "Make a class named ### that is-a ###.",
           "class ###(object):\n\tdef __init__(self, ***)" :
           "class ### has-a __init__ that takes self and *** parameters.",
           "class ###(object):\n\tdef ***(self, @@@)":
           "class ### has-a function named *** that takes self and @@@ parameters.",
           "*** = ###()":
           "Set *** to an instance of class ###.",
           "***.***(@@@)":
           "From *** get the *** function, and call it with parameters self, @@@.",
           "***.*** = '***'":
           "From *** get the *** attribute and set it to '***'."
           }

phrases_frist = False

if len(sys.argv) == 2 and sys.argv[1] == 'english':
    phrases_frist = True
    
for word in urlopen(word_url).readlines():
    words.append(word.strip())
    
    
def convert(snippet,phrase):
    class_name = [w.capitalize() for w in
                  random.sample(words,snippet.count('###'))]
    
    other_names = random.sample(words,snippet.count('***'))
    
    results = []
    param_name = []
    
    for i in range(0,snippet.count('@@@')):
        param_count = random.randint(1,3)
        param_name.append(','.join(random.sample(words,param_count)))
        
    for sentence in snippet,phrase:
        result = sentence[:]
        
        for word in class_name:
            result += result.replace('###',word,1)
            
        for word in other_names:
            result += result.replace('***',word,1)
            
        for word in param_name:
            result += result.replace('@@@',word,1)
            
        
        
    
    
    
