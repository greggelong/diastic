 
def load_string():
    
    with open("metamorphSml.txt",encoding="utf-8") as myfile:
        srctxt = myfile.read().rstrip("\n")   # .read() loads file as a string readlines() loads file as a list split at lines 
        return srctxt
            
            
def clean_string(original):
    
    for char in "\".?;,!":
        original = original.replace(char,"")
    return original

def word_list(string):
    return string.split(" ")

myString = load_string()
print(type(myString))
print(myString)
myclean = clean_string(myString)
print(myclean)
mylist = word_list(myclean)
print(mylist)