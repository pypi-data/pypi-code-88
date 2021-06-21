#Preprocessing text
#input a String as text, than output a list of words as corpus

#This function is suited for standard German and English.
#For more language, change the character for exchangement.

def preprocess(text):
    text=text.replace("ä","ae").replace("Ä","Ae").replace("ö","oe").replace("Ö","oe").replace("ü","ue").replace("Ü","ue")
    remove_digits = str.maketrans('', '', '0123456789')
    text = text.translate(remove_digits)
    text = re.sub(r'[^\w\s]','',text)
    word = text.split()
    return word
