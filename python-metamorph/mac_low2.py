 
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
print(type(myString))
#print(myString)
myclean = clean_string(myString)
print(myclean)
mylist = word_list(myclean)
print(mylist)