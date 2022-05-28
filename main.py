# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from itertools import count 

def read_file_content("story.txt"):
    # [assignment] Add your code here 
    file = open("./story.txt", "r")
    print(file.read())

    return "Hello World"

    read_file_content("story.txt")


def count_words(words,text):
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    words = text.split()
    print(words)
    count = dict()

    for word in words:
        if word in count.keys():
            count[words] += 1
        else:
            count[word] = 1
    
    print(count_words())

    return {"as": 10, "would": 20}
