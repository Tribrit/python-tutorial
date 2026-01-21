import random
#import random   comes first

list=["camel","driver","dreamer"]

#Choose a word from  the list  and a assign a variable called chosen _word
chosen_word=random.choice(list)
print(chosen_word)

guess=input("Guess a letter: ")#.  lowercase()
print(guess)