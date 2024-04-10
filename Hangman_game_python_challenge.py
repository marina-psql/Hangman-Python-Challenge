from random import randrange            # imports the randrange function from the random module. It lets us randomly select an index position within a list.
words_list = ["FLOWERS", "GARDEN", "SPRING", "BLOOM", "DAYLIGHT", "PYTHON", "BOOTCAMP", "TABLEAU", "CODING", "CHALLENGE"]   # we manually create a words list
word = words_list[randrange(len(words_list))]   # randrange randomly selects a word from words_list and this can be done as many times as the list's length)
# option setting only one word -->  word = "TABLEAU"        # creates a string variable - it needs to be in uppercase, otherwise if the user inputs a capital letter, it will consider it wrong even if it is a matching letter
hidden_word = "-" * len(word)           # hides the word by replacing each character with a - and makes it as long as the word is

print(f"The hidden word is '{hidden_word}'. Can you guess it?\n =========================================================================")

mistake_count = 6                       # sets mistake count at 6 so that the count is descending
hidden_list = list(hidden_word)         # turns hidden_word into a list - I tried this on Friday and it did not work (error after error)
hangman={0:'''
        ____________
         |''',
        1:'''
        ____________
         |
         O''',
        2:'''
        ____________
         |
         O
        /''',
        3:'''
        ____________
         |
         O
        / \\''',
        4:'''
        ____________
         |
         O
        / \\
         |''',
        5:'''
        ____________
         |
         O
        / \\
         |
        /''',
        6:'''
        ____________
         |
         O
        / \\
         |
        / \\ '''}
hang_count = 0    # creates a variable that allows me to print the drawings later on

while mistake_count > 0:
    picked_letter = input("Enter a letter:").upper()        # asks input from user and capitalizes it for consistency
    if len(picked_letter) != 1:                             # makes sure input is only one character
        print(f"You have entered more than one character. Only one single letter is possible. Try again:")
        continue
    if not picked_letter.isalpha():                         # makes sure input is alphabetic (isalpha accepts other languages like Greek & Cyrillic, incl. ñ, ß, ç)
        print(f"Only A to Z letters are allowed. Try again:")
        continue
    if picked_letter in word:
        print(f"CORRECT! The word contains the letter '{picked_letter}'")
        for index in range(len(word)):                  # it loops through the word
            if word[index] == picked_letter:            # it checks which position the picked letter occupies within the word
                hidden_list[index] = picked_letter      # updates the list (made up of the hidden word) by replacing the right letter picked by the user
                hidden_word = "".join(hidden_list)      # turns the hidden word list into a string again
        print(f"The updated hidden word is: {hidden_word}.")
        if hidden_word == word:
            print(f"Congratulations! You guessed the word :) ")
            break
    else:
        mistake_count -= 1              # here we subtract one used chance to the mistake count
        hang_count += 1                 # here we forward to the second drawing without using the first one
        if mistake_count >= 1:          # as long as the mistake count is 1 or higher, it is going to keep asking for another letter
            print(f"WRONG! You have {mistake_count} more chances to guess. Please try again!{hangman[hang_count]}\n =========================================================================")
        # \n adds a new line within the print function
        else:
            print(f"HANGED! {hangman[6]} \n Sorry, you ran out of chances. The correct word was '{word}'. Good luck next time!")
            break
