#! /bin/python3

# QUIZ 6 QUESTION ??????
# --------------
# Choose any solutions below that are the same as the code below:
# my variable setup
text = 'Sam I am'
new_text = '' # using append, therefore it has to be a list
vowel = 'a'
new_text = []

# original question
for char in text:
    if char in 'aeiou':
        new_text.append(vowel)
    elif char in 'AEIOU':
       new_text.append(vowel.upper())
    else:
      new_text.append(char)
      
print(''.join(new_text))
# print(f'original: {new_text}')
# --------------

# Question answer options:

###############
text = 'Sam I am'
new_text = ''
vowel = 'a'
new_text = []
new_text = [ vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char for char in text]

print(''.join(new_text))

################
# okay
text = 'Sam I am'
new_text = ''
vowel = 'a'
new_text = []
new_text = map ( lambda char: vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char, text)

print(''.join(new_text))

################
# okay
text = 'Sam I am'
new_text = ''
vowel = 'a'
new_text = []
def new_char(char):
    return vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char

new_text = ''.join([new_char(char) for char in text])
print(''.join(new_text))

################
# okay 
text = 'Sam I am'
new_text = ''
vowel = 'a'
new_text = []
new_text = [ vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char for char in text]

print(''.join(new_text))
