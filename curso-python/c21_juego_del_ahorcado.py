from random import randint
import os

def intro():
    print('********  **    ** ******** *******  ******** ******** *******  ********')
    print('********  **    ** ******** ******** ******** ******** ******** ********')
    print('**    **  **    ** **    ** **    ** **       **    ** **    ** **    **')
    print('********  ******** **    ** *******  **       ******** **    ** **    **')
    print('********  ******** **    ** *******  **       ******** **    ** **    **')
    print('**    **  **    ** **    ** **    ** **       **    ** **    ** **    **')
    print('**    **  **    ** ******** **    ** ******** **    ** ******** ********')
    print('**    **  **    ** ******** **    ** ******** **    ** *******  ********')
    print('')

def read():
    words = []
    with open('./archivos/data.txt','r') as w:
        for word in w:
            words.append(word)
    return words


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def letter_correct(guess_letter, secret_word, guess_word, life):
    # Variable para saber si se adivino alguna letra
    guess = False
    # Variable para saber si ya todas la letras esta llenas
    finish_letters = True 
    word_correct = []
    life_2 = life
    for i in range(len(guess_word)):
        if secret_word[i] == guess_letter:
            guess_word[i] = guess_letter
            guess = True
        
        if guess_word[i] == '_':
            finish_letters = False
    
    word_correct = ''.join(guess_word)
    if finish_letters:
        print('¡FELICITACIONES, ADIVINASTES LA PALABRA!')
        print('')
        print(word_correct)
        life = 0
    elif guess:
        print('¡Adivinastes la letra!')
        print('')
        print(word_correct)
    else:
        print('Lo siento, no adivinastes la letra')
        print('')
        print(word_correct)
        life = life - 1
    

    return guess_word, life, life_2, finish_letters


def dummy(life):
    if life == 0:
        print('=============        ')
        print('||         ||        ')
        print('||        _||_       ')
        print('||       (.)(.)      ')
        print('||      /  ()  \     ')
        print('||    _ \ |--| / _   ')
        print('||   { |-`""""`-| }  ')
        print('||    `"/      \"`   ')
        print('||      \      /     ')
        print('||     _/  /\  \_    ')
        print('||    {   /  \   }   ')
        print('||     `"`    `"`    ')
        print('=====================')
        print('')
    elif life == 1:
        print('=============        ')
        print('||         ||        ')
        print('||        _||_       ')
        print('||       (.)(.)      ')
        print('||      /  ()  \     ')
        print('||    _ \ |--| / _   ')
        print('||   { |-`""""`-| }  ')
        print('||    `"/      \"`   ')
        print('||      \    _ /     ')
        print('||     _/  /         ')
        print('||    {   /          ')
        print('||     `"`           ')
        print('=====================')
        print('')
    elif life == 2:
        print('=============        ')
        print('||         ||        ')
        print('||        _||_       ')
        print('||       (.)(.)      ')
        print('||      /  ()  \     ')
        print('||    _ \ |--| / _   ')
        print('||   { |-`""""`-| }  ')
        print('||    `"/      \"`   ')
        print('||      \ ____ /     ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('=====================')
        print('')
    elif life == 3:
        print('=============        ')
        print('||         ||        ')
        print('||        _||_       ')
        print('||       (.)(.)      ')
        print('||      /  ()  \     ')
        print('||    _ \ |--| / _   ')
        print('||   { |-`""""`-| }  ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('=====================')
        print('')
    elif life == 4:
        print('=============        ')
        print('||         ||        ')
        print('||        _||_       ')
        print('||       (.)(.)      ')
        print('||      /  ()  \     ')
        print('||    _ \ |--| /     ')
        print('||   { |-`""""`      ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('=====================')
        print('')
    elif life == 5:
        print('=============        ')
        print('||         ||        ')
        print('||        _||_       ')
        print('||       (.)(.)      ')
        print('||      /  ()  \     ')
        print('||      \ |--| /     ')
        print('||       `""""`      ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('=====================')
        print('')
    elif life == 6:
        print('=============        ')
        print('||         ||        ')
        print('||         ||        ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('||                   ')
        print('=====================')
        print('')



def run():
    os.system('clear')
    life = 6

    intro()
    words = read()
    length = len(words)
    secret_number = randint(0, length)
    secret_word = words[secret_number]
    secret_word = normalize(secret_word)
    guess_word = ['_' for i in range(len(secret_word) - 1)]

    #Mantiene corriendo mientras se tenga vidas
    while life != 0:
        guess_letter = input('Ingresa una letra: ')
        os.system('clear')
        guess_word, life, life_2, finish_letter = letter_correct(guess_letter, secret_word, guess_word, life)
        #print('secret word: ', secret_word)
        #print('guess word: ', guess_word)
        #print('life: ', life)
        if finish_letter:
            dummy(life_2)
        else:
            dummy(life)

    if finish_letter:
        print('')
        print('¡GANASTES!')
    else:
        print('')
        print('¡PERDISTES!')


    
    #print(guess_word)
    #dummy(life)



if __name__ == '__main__':
    run()