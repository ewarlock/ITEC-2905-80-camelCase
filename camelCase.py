def banner():
    """ Display program name, using stars """
    message = 'Awesome camelcase program!!'
    stars = '*' * len(message)
    print(f'\n{stars} \n{message} \n{stars} \n')

def instructions():
    """ Display instructions for how to use the program """
    print('Enter a sentence and this program will convert it to camelcase.\n')

def camel_case(sentence):

    #put each word of sentence into a starter list
    sentence_list = sentence.split()

    #make empty string for camel case sentence
    sentence_camelCase = ""

    #put the first word into the camelcase string in all lowercase & remove from starter list
    first_word = sentence_list[0]
    first_word = first_word.lower()
    sentence_camelCase += (first_word)

    #format the rest of the words in the starter list 
    for word in sentence_list:
        word_start = word[0:1].upper() #take first letter of each word and put in uppercase
        word_end = word.lower() #put all words in lowercase
        word_end = word_end[1:len(word) + 1] #removes the first letter of each lowercase word
        word_camel = word_start + word_end #adds the first uppercase letter to the start of each lowercase word
        sentence_camelCase += (word_camel) #add each word to end of camelcase string

    return sentence_camelCase


def main():
    banner()
    instructions()

    sentence = input('Please type in a sentence: ')
    camel_case_sentence = camel_case(sentence)
    print(camel_case_sentence)


if __name__ == '__main__':
    main()