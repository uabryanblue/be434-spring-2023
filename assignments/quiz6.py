#! /bin/python3
# text = 'Sam I am'
# new = ''
# for char in text:
#     print(f'{char.upper()}')
#     new += char.upper()
# print(f'{text}')

# text = 'Sam I am'
# new_text = []
# vowel = 'e'
# for char in text:
#     if char in 'aeiou':
#         new_text.append(vowel)
#     elif char in 'AEIOU':
#        new_text.append(vowel.upper())
#     else:
#       new_text.append(char)
# print(f'{new_text}')


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

# Question options:

###############
# "map" solution has a syntax error
# def new_char(char):
#    return vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char

# print(''.join.(map(new_char, args.text))) # syntax error
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

#----------
exit()

text = 'Sam I am'
new_text = []
vowel = 'e'
# replace all values with one specified in "vowel"
for char in text:
    if char in 'aeiou':
        new_text.append(vowel)
    elif char in 'AEIOU':
       new_text.append(vowel.upper())
    else:
      new_text.append(char)
print(f'origl: {new_text}')

# Question options:

# okay
new_text =[]
new_text = [ vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char for char in text]
print(f'test1: {new_text}')

# no, map opject
new_text =[]
new_text = map ( lambda char: vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char, text)
print(f'test2: {new_text}')

# new_text =''
# def new_char(char):
#     return vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char

# print(''.join.(map(new_char, args.text)))

new_text =''
def new_char(char):
    return vowel if char in 'aeiou' else vowel.upper() if char in 'AEIOU' else char
new_text = ''.join([new_char(char) for char in text])
print(f'test3: {new_text}')

