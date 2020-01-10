# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    return ' '.join(words[1:] + words[0] + "ay" if words.isalpha() else words[0] for words in text.split() )
    #your code here