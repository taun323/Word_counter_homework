#this function removes punctuation signs from the text by replacing them with nothing
#the input of the function is chosen by the user
def punctuation_remover(text):
    for character in punctuation:
        text = text.replace(character, "")
    return text

#this function splits the string, and it adds the words to the list
#the input of this function is the result of the previous function

def word_counter(text):
    for word in text.split():
        if word not in words:
            words.append(word)
    return len(words) #the length of words provides the amount of different words in it

#The variables contain the different texts
#The variables are selected by the user
source1 = open("book_one.txt", encoding = "UTF-8")
source2 = open("book_two.txt", encoding = "UTF-8")
source3 = open("book_three.txt", encoding = "UTF-8")

text = ""
words = []
punctuation = '¿?¡!().:,;»“”—-_/\+=0123456789"'

#This gives information to the user, before asking for input
print("This tool analyzes how many different words are used in a book")
print("Book 1, A Christmas Carol, by Charles Dickens")
print("Book 2, Metamorphosis, by Franz Kafka")
print("Book 3, The Adventures of Huckleberry Finn, by Mark Twain")

while True:
    #the while loop
    x = input("Enter a number from 1 to 3 to choose the book to analyze: ")
    try:
        #First check if the input is a number, if not except applies
        x = int(x)

        #The "text" variable is updated depending on user input
        if x == 1:
            text = source1.read().lower()
            print("Book 1, A Christmas Carol, contains: ")

        elif x == 2:
            text = source2.read().lower()
            print("Book 2, Metamorphosis, contains: ")

        elif x == 3:
            text = source3.read().lower()
            print("Book 3, the Adventures of Huckleberry Finn, contains: ")

        if x>0 and x<4:
            #"clean_text" variable is the return from the punctuation_remover function
            clean_text = punctuation_remover(text)

            print(word_counter(clean_text), "different words.")
            break
    except:
        print("write numbers only")