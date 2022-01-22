# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 

while True:

    phrase = input('Please enter a word or phrase: ').lower()

# 2. Print the following message:
#      - What you entered is xx characters long
    print('What you entered is', len(phrase), 'characters long')

# 3. Return to step 1, unless the word 'quit' was entered.


    if phrase == 'quit':
        print(f'I"m leaving!')
        break



# python3 exercise-2.py