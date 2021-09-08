#get input sentence from user
sentence_starter = input('Please type in a sentence: ')

#put each word of sentence into a starter list
sentence_list = sentence_starter.split()

#make blank list for camel case sentence
sentence_camelCase = []

#put the first word into the camelcase list in all lowercase
first_word = sentence_list[0]
first_word = first_word.lower()
sentence_camelCase.append(first_word)

#take the first word out of the starter list
sentence_list.pop(0)

#format the rest of the words in the starter list 
for word in sentence_list:
    word_start = word[0:1].upper() #take first letter of each word and put in uppercase
    word_end = word.lower() #put all words in lowercase
    word_end = word_end[1:len(word) + 1] #removes the first letter of each lowercase word
    word_camel = word_start + word_end #adds the first uppercase letter to the start of each lowercase word
    sentence_camelCase.append(word_camel) #add each word to end of camelcase list

#blank string for final product to be printed from
final_sentence = ''

#add contents of camelcase list to string...
for word in sentence_camelCase:
    final_sentence = final_sentence + word

#print final string
print(final_sentence)

#feel like this program can be simplified...