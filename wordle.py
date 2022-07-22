from dic import list_of_words
from random import choice

word_lenght = 5

list_of_words = [x for x in list_of_words if len(x) == word_lenght]

win_word = choice(list_of_words)

play = 0

while True:

    if play == word_lenght + 1:
        print("\n\033[1;31;40m LOSE \033[0m\n")
        break

    input_player = str(input(" guess:"))
    l_input_player = list(input_player)
    

    if len(l_input_player) == 5 and (input_player in list_of_words):
        
        play += 1

        for x in range(word_lenght):
            if l_input_player[x] == win_word[x]:
                l_input_player[x] = "\033[1;32;40m"+l_input_player[x]+ '\033[0m'
        
        for x in range(word_lenght):
            if list(input_player)[x] != win_word[x] and  list(input_player)[x] in list(win_word) and (list(input_player)[:x+1].count(list(input_player)[x]) <= win_word.count(list(input_player)[x])):
                l_input_player[x] = "\033[1;33;40m"+l_input_player[x]+'\033[0m'

        if input_player == win_word:
            
            for x in l_input_player:
                print(x,end= "")
            print("\n\033[1;31;40m WIN GG \033[0m\n")
            
            break
        
        
        for x in l_input_player:
            print(x,end= "")
        
        #print("\n"+win_word) # god mode - pls dont tell anyone
