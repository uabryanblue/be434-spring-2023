#! /bin/python3

# QUIZ 6 QUESTION ??????
# --------------
# Choose any solutions below that are the same as the code below:
# my variable setup
text = 'Sam I am'
new_text = [] # using append, therefore it has to be a list
vowel = 'e'

# original question
for char in text:
    if char in 'aeiou':
        new_text.append(vowel)
    elif char in 'AEIOU':
       new_text.append(vowel.upper())
    else:
      new_text.append(char)
print(f'original: {new_text}')
# --------------

# Question answer options:

###############
## "map" solution has a syntax error
## even if new_char and args.text arche change to hard coded values
# def new_char(char):
#     return vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char
## ORIGINAL LINE - don't have args parameters, so create a new line with variable changes
# print(''.join.(map(new_char, args.text))) # !! SYNTAX ERROR
## MODIFIED LINE - remplaced new_char with vowel and args.text with text
# print(''.join.(map(vowel, text))) # !! SYNTAX ERROR

print(f'test that uses: "''.join.(map(new_char, args.text)))"  solution generates syntax error')

################
# does not work, it returns "map" object "<map object at 0x7fd025263dc0>"
new_text = map ( lambda char: vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char, text)
print(f'test lambda: {new_text}')

################
def new_char(char):
    return vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char

new_text = ''.join([new_char(char) for char in text])
print(f'test join with new_char function: {new_text}')

################
new_text = [ vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char for char in text]
print(f'test list comprehension: {new_text}')
