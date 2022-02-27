import random
from random_word import RandomWords

def get_word():
    r = RandomWords()
    word = r.get_random_word()
    print(word)
    return word

def display_word(full_word, letters):
    display_word = ""
    for i in range(len(full_word)):
        if i in letters:
            display_word = display_word + full_word[i]
        else:
            display_word = display_word + "_"
    return display_word


def check_letter(word, letter, guesses):
    found = False
    for i in range(len(word)):
        if (word[i] == letter):
            if not (i in guesses):
                guesses.append(i)
            found = True
    return guesses, found

#
#
# while len(spejimas) != ilgis:
#     if bandymai == 0:
#         print("Game over")
#         break
#     raide = input("kokia raide speji?")
#     raides = tikrinam_raide(raide)
#     spausdinam_zodi(random, raides)
# print("Laimėjote")
#
#
#
#

