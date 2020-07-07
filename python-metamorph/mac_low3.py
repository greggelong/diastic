
def diastic(seed,text):
    phrase = "" # empty string to fill with words
    currentWord = 0 # to keep track of where we are reading in the text
    
    for i, char in enumerate(seed):   # use enumerate to get the char and index
        print(i,char)
        seedChar = char
        for j in range(currentWord,len(text)):
            if len(text[j]) > i and text[j][i] == seedChar:  # first check the word is long enough then check that the character and position match
                # this mimics the charAt() in p5js
                phrase += text[j]
                phrase += " "
                currentWord =j+1
                print(phrase)
                break
    
    return phrase
 


def load_string():
    "loads text from file and returns a string"
    srcstrg=""
    with open("metamorphSml.txt",encoding="utf-8") as myfile:
        srctxt = myfile.readlines()   # .read() loads file as a string readlines() loads file as a list split at lines 
        for line in srctxt:
            srcstrg =srcstrg+ line
    return " ".join(srctxt)
            
            
def clean_string(original):
    "cleans and returns a string"
    for char in "\".?;,!\n-":
        original = original.replace(char,"")
    return original

def word_list(string):
    return string.split()

myString = load_string()
#print(type(myString))
#print(myString)
myclean = clean_string(myString)
#print(myclean)
mylist = word_list(myclean)
#print(mylist)
print("Jackson Mac Low's Diastic reading Using Kafka's Metamorphosis")
seed = input("Please enter a seed phrase: ")
output = diastic(seed,mylist)
print(output)
