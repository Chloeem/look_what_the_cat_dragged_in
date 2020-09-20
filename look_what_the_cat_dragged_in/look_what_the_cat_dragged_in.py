import sys
import time
import emoji
from time import sleep
from pyfiglet import Figlet
import playsound
import random



# GAME ENDING CREDITS
def end_game():
    print("\n")
    intro_goodbye = "WHOOPS! Oh no {}! What a way to go!".format(name)
    for char in intro_goodbye:
        sleep(0.4)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1.5)
    print("\n")
    print("------------------------------------------------------------------------------------")
    time.sleep(1.5)
    print(" /\-/\    /\-/\    /\-/\    /\-/\    /\-/\    /\-/\    /\-/\    /\-/\    /\-/\ ")
    print("(=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=) ")
    print(" (>o<)    (>o<)    (>o<)    (>o<)    (>o<)    (>o<)    (>o<)    (>o<)    (>o<) ")
    time.sleep(1.5)
    print("Thank you for playing 'Look what the cat dragged in!'. We hope you enjoyed it!")
    print("------------------------------------------------------------------------------------")
    time.sleep(3)
    print("\n\n\n\n")
    print("------------------------------------------------------------------------------------")
    playsound.playsound('squeaks.wav', False)
    time.sleep(0.5)
    print("Would you like to play again? [Y]/[N] ")
    time.sleep(1.5)
    restart = input("Answer: ")
    time.sleep(0.5)
    game_over = Figlet(font='small')
    if restart == "Y" or restart == "y" or restart == "yes" or restart == "Yes" or restart == "YES":
        intro()
    elif restart == "N" or restart == "n" or restart == "No" or restart == "no" or restart == "NO":
        print("------------------------------------------------------------------------------------")
        print("\n\n\n\n")
        time.sleep(1.5)
        print(game_over.renderText("GAME OVER!"))
    else:
       print("'Sorry I dont understand! Eeek! Please try again!'")
       end_game()

# WINNER
def you_won():
    time.sleep(1)
    playsound.playsound('pitterpatter.wav', False)
    print("\n")
    print("*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n")
    time.sleep(1)
    winner = Figlet(font='small')
    print(winner.renderText("    !!!!       W I N N E R        !!!!"))
    time.sleep(1)
    print("*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*<>*\n")
    time.sleep(2)
    print("\n\n")
    print("------------------------------------------------------------------------------------")
    congrats = "                      CONGRATULATIONS {} YOU WON!!\n".format(name)
    for char in congrats:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1.5)
    playsound.playsound('squeaks.wav', False)
    time.sleep(0.2)
    print("                        /")
    print("                       /")
    print("                   ()()                             ____ ")
    print("                   (..)                            /|o  | ")
    print("                   /\/\                           /o|  o| ")
    print("                  c\db/o...                      /o_|_o_|  ") 
    time.sleep(1.5)
    print("\n")
    print("Thank you for playing 'Look what the cat dragged in!'. We hope you enjoyed it!")
    print("------------------------------------------------------------------------------------")
    time.sleep(3)
    print("\n\n\n\n")
    print(" -----------------------------------------------------------------------------------")
    time.sleep(0.5)
    print("|     Would you like to play again? [Y]/[N]                                         |")
    time.sleep(1.5)
    play_again = input("Answer: ")
    time.sleep(0.5)
    game_end = Figlet(font='small')
    if play_again == "Y" or play_again == "y" or  play_again == "yes" or  play_again == "Yes" or  play_again == "YES":
        intro()
    elif    play_again == "N" or play_again == "n" or play_again == "No" or play_again == "no" or  play_again == "NO":
        print(" -----------------------------------------------------------------------------------")
        print("\n")
        time.sleep(1.5)
        print(game_end.renderText("GAME OVER!"))
    else:
       print("'Sorry I dont understand! Eeek! Please try again!'")
       you_won()

#OPTION THREE
def after_moth_quiz():
    print("\n")
    playsound.playsound('moth_laugh.wav', False)
    for char in "\nThe Moth disappears for moment, giggling to herself maniacally\n'HEHEHEhehohohohehe...'\nAnd returns with a lettuce leaf\nShe gestures to give it to you\nYou look at her confused...\nDo you accept the random leaf offer?\n[Yes]/[No]\n":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    # print("Moth gives you a lettuce leaf")
    # time.sleep(1.5)
    playsound.playsound('squeaks.wav', False)
    leaf_offer = "@@@@"
    while leaf_offer.lower() != "yes" and leaf_offer.lower() != "no":
        leaf_offer = input("Enter Choice: ")
    for char in "\nThe Moth tells a story of how she comes to be there (through an open window)\nShe was starring longing at her reflection in the glass\nWondering who the other fine specimen of a Moth was\nShe flew into the house, only to realise she was alone..\nShe has been stuck here ever since.\nYou having a larger mousey brain look up and see the window\nits a little higher than you...\n....\n'How could she have been stuck so long with wings!?\nHMMMM...\nThe Moth offers to take you to the toaster for a tour.\nYou look even more confused..\nDo you accept her tour offer?\n[Yes]/[No]\n":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    tour_offer = "@@@@"
    while tour_offer.lower() != "yes" and tour_offer.lower() != "no":
        tour_offer = input("Enter Choice: ")
        playsound.playsound('moth_laugh.wav', False)
    if tour_offer.lower() == "yes":
        for char in "\nThe Moth starts giggling againn..\n'HEHEHEhehohohohehe...'\nShe turns to the toaster with the biggest grin on her mothy face\nand tells you this is her hilarious best friend\nPointing to the toaster\n...\nShe says it tells great jokes in the morning..\nYou look at her perplexed and start to wonder if she can help\nyou after all...\nIt seems loneliness has got to her..\nShe starts explaining to you how the toaster works.\nYou leap to the ready, down into the toaster...\n'1!!!' She shouts..\n....2!!..\n...3!!!..\nThe moth pushes the lever flying you up UP UPPPPP\nand AWWWWAAAAAYY..\nOut the window...jumping with..\n":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("\n\n")
        print(" ----------------------------------------------------------    ")
        print("|                                                          |    ")
        print("|              ______                                      |    ")
        print("|          ___((     )_                                    |    ")
        print("|        |'->==))   (= \                                   |    ")
        print("|        |  \ ||_____|_ \                                  |    ")
        print("|        |[> \___________\                                 |    ")
        print("|        | | |            |                                |    ")
        print("|         \  |   TOASTER  |             .--.               |    ")
        print("|          \ |   -------  |)---.   .---'    `-.----(]=     |    ")
        print("|           \|____________|     `-'                        |    ")
        print("|                                                          |    ")
        print(" ----------------------------------------------------------     ")                                     
        print("\n\n")
        if leaf_offer.lower() == "yes":
            for char in "\nThe Moth shout to you\n\nLETTUCE LEAFFFFF'\n\nYou grab the leaf and paraglide out the window....":
                sleep(0.15)
                sys.stdout.write(char)
                sys.stdout.flush()
            you_won()
        else:
            for char in "\nThe Moth waves the lettuce leaf and shouts 'GLIDERRRR' at to you\n\nYOU PANIC\nNOOOOO!!\nYou should have taken the leaf to glide on\n....\nNOOOOO\nAHHHH...\n....You SPLAT on the window\n":
                sleep(0.15)
                sys.stdout.write(char)
            print("\n")
            print(" ------------------------------")
            print("|   !!     !           !!      |
            print("|           .  !   .           |")
            print("|       .  /|     /\  ,    !!  |")    
            print("|    !  |\/ |/\__/  \/|___     |")
            print("|     __|                /     |")
            print("|     \       SPLAT!     \  !  |")
            print("|!!   /       -----      _\    |")
            print("|    /___  _  _         _\     |")
            print("|       /,' \| \  /\|\ |       |")
            print("|      /'    `  \/  ` \|    !! |")
            print("|  !!          !          !    |")
            print(" ------------------------------")
            print("\n")
            playsound.playsound('splat.wav', False)
            time.sleep(1.5)
            playsound.playsound('squeaks.wav', False)
            time.sleep(1.5)
            playsound.playsound('dead.wav', False)
            end_game()
    else:
        for char in "\nYou go back to kitchen to explore some more...\n":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        time.sleep(1.5)
        after_spider_quiz()

def moth_quiztime():
    wins = 0
    losses = 0
    rounds = 3
    q_num = 1
    tries = 2

    questions_moth = (
        "I am an insect! What am I?",
        "I have a thick, furry body! What am I?",
        "I have a long tongue, called a PROBOSCIS! What am I?",
        "I taste food with my feet! What am I?",
        "I am more often brightly colored than not. What am I?",
        "Most of my kind fly during the day! What am I?",
        "I fold my wings beside my body when I'm resting. What am I?",
        "I help plants pollinate! What am I?",
        "My feelers can be many shapes and sizes. What am I?",
        "I went through a metamorphosis. What am I?"
    )

    answers_moth = (
        "[Butterfly]    [Moth]    [Both]    [Neither] ",
        "[Butterfly]    [Moth]    [Both]    [Neither] ",
        "[Butterfly]    [Moth]    [Both]    [Neither] ",
        "[Butterfly]    [Moth]    [Both]    [Neither] ",
        "[Butterfly]    [Moth]    [Both]    [Neither] ",
        "[Butterfly]    [Moth]    [Both]    [Neither] ",
        "[Butterfly]    [Moth]    [Both]    [Neither] ",
        "[Butterfly]    [Moth]    [Both]    [Neither] ",
        "[Butterfly]    [Moth]    [Both]    [Neither] ",
        "[Butterfly]    [Moth]    [Both]    [Neither] "
    )

    good_answer_moth = (
        "both",
        "moth",
        "both",
        "both",
        "butterfly",
        "butterfly",
        "moth",
        "both",
        "moth",
        "both"
    )

    wikimoth = (
        "These insects have three body parts: a head,\nthorax and abdomen. They also have six legs and\nlarge wings that are covered in tiny scales.",
        "A butterfly on the other hand, has a slender, hairless body.",
        "The proboscis works like a drinking straw that they\nuse to sip nectar.",
        "They only eat with their proboscis. Isn't that strange.",
        "A moth is usually dull in color, although there are\nexceptions to the rule, such as the luna moth, which has\nnlight-green wings. Most butterflies have vibrant colors.",
        "A moth is opposite. It usually flies at night.",
        "A butterfly brings its wings up over its body.",
        "They help the plants by spreading pollen that plants need.",
        "A butterfly's feelers are always long and slender with a knob on the tip.",
        "There are four changes in their metamorphosis: egg, larva, pupa and adult."
    )
    while tries > 0:
        tries -= 1
        while wins + losses < rounds:
            rquestion = random.randint(0,9) #randomize a question
            if q_num == 1:
                q1_index = rquestion
            elif q_num == 2:
                while rquestion == q1_index:
                    rquestion = random.randint(0,9)    #randomize a question again if duplicate
                q2_index = rquestion
            else:
                while rquestion == q1_index or rquestion == q2_index:
                    rquestion = random.randint(0,9)    #randomize a question again if duplicate
            print()
            print("Question ",str(q_num))
            print(questions_moth[rquestion])
            q_num += 1
            user_answer = "####"
            while user_answer.lower() not in answers_moth[rquestion].lower():
                user_answer = input(answers_moth[rquestion])
            if user_answer.lower() == good_answer_moth[rquestion]:
                wins += 1
                playsound.playsound('correct.wav', False)
                print("Correct answer!")
                time.sleep(1.5)
                print(wikimoth[rquestion])
                time.sleep(3.5)
            else:
                losses += 1
                playsound.playsound('wrong.wav', False)
                print("Wrong answer")
                time.sleep(1.5)
                print("The correct answer was ",good_answer_moth[rquestion].capitalize())
                print(wikimoth[rquestion])
                time.sleep(3.5)
        print()
        print("You got ",wins," out of ",rounds," correct!")
        time.sleep(1.5)
        if wins == rounds:
            tries = 0
            after_moth_quiz()
        else:
            if tries > 0:
                print("I'm feeling generous... You can have one more crack at it {}".format(name))
                print()
                wins = 0
                losses = 0
                rounds = 3
                q_num = 1
                time.sleep(1.5)
    if wins < 3:
        playsound.playsound('wrong.wav', False)
        print("Clearly you know nothing about moths or butterflies\n....\n")
        time.sleep(1.5)
        print("I cannot help you")
        playsound.playsound('cat_shreak.wav', False)
        end_game()

def after_spider_quiz():
    print("\n")
    playsound.playsound('squeaks.wav', False)
    for char in "\nAfter hard swallowing your shared Wasp dinner and\nmanaging to keep it down in your stomach,\nyou crack a smile on your fuzzy face as the Spider\ntakes you into the kitchen counter to look around.\nWhat do you want to explore?\n[Espresso Machine]\n[Sink]\n[Cat flap]\n":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    explore = "####"
    while explore.lower() not in "[espresso machine][sink][cat flap][espresso][Espresso]":
        explore = input("Enter Choice: ")
    if explore.lower() == "espresso machine":
        print("\n\n")
        print(" -----------------------------------------------------------------")
        print("|                                ______________________           |")
        print("|                                (___________           |         |")
        print("|                                  [XXXXX]   |          |         |")
        print("|                             __  /~~~~~~~\  |          |         |")
        print("|                            /  \|@@@@@@@@@\ |          |         |")
        print("|             )              \   |@@@@@@@@@@||          |         |")
        print("|            (                   \@@@@@@@@@@||  ______  |         |")
        print("|           __)__                 \@@@@@@@@/ | |on|off| |         |")
        print("|        C\|     \               __\@@@@@@/__|  ~~~~~~  |         |")
        print("|          \     /              (____________|__________|         |")
        print("|           \___/               |_______________________|         |")
        print("|                                                                 |")
        print(" -----------------------------------------------------------------")
        print("\n\n")
        playsound.playsound('drink.wav', True)
        playsound.playsound('energized.wav', False)
        for char in "\nWo0o0OOOo0ooooOo0o0oo00ooooooo...\nYou try the coffee, feeling SUPER energised and invinsible\nYou eyes dart around frantically looking for clues...\n....\nYou notice a moth in a bag of flour\nDo you want to Speak to moth?\n[Yes]/[No]\n":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        option = "@@@@"
        while option.lower() != "yes" and option.lower() != "no":
            option = input("Enter Choice: ")
        if option.lower() == "yes":
            for char in "\nYou wander over the bag of flour where the moth\nis buried deep and chattering to herself\nshe heres your little mousey footsteps\nand pops out the bag\n\n....\n'OH HELLO! A MOUSE WOW!\nI'm Silve the moth...Nice to meet you!\n\nYou tell her your story and she offers to help under one\ncircumstances...":
                sleep(0.15)
                sys.stdout.write(char)
                sys.stdout.flush()
            time.sleep(2)
            playsound.playsound('gameshow.wav', False)
            print("\n\n")
            print(" --------------------------------------------------------------------------------------------------")
            print("|                                                                                                  |")
            print("|         .-'''''''   ,.               n,                                      ..      ..          |")
            print("|        \-          ,,'''-..      n   '\.                ,.n           ..--''           )         |")
            print("|         \-     . .,;))     ''-,   \     ''.. .'''. .,-''    .n   ..-''   (( o         _/         |")
            print("|          \- ' ''''':'          ''-.'' '--_  '     '  ,.--'''.. ''         ' ' ' - .  _/          |")
            print("|           \-                       ''->.   '  ,--. '/' >..''                        _/           |")
            print("|            \                     (,       /  /.  .\ \ ''    ,)                     ./            |")
            print("|             ''.    .  ..         ')          \ .. /         ('          ..       ./              |")
            print("|                ''-... . ._ .__         .''.   /..\   ,'.            __ _ _,__.--'                |")
            print("|                   /' ((    ..'' ' ' '-'  6  \/__\/  ' '- - -' ' ',''   - '\                      |")
            print("|                  '(.  6,    '..          /.   ''  .'          ,,'     ) )  )                     |")
            print("|                    '\  \ C_,_   ==,      / '_      _|\       ,'', ,,_.;-' _/                     |")
            print("|                      '._ ,   ')   E     /'|_ ')()('_' \     C  ,I'''  _.-'                       |")
            print("|                         ''''''\ (('   ,/  ''  (()) ''  '-._ _ __---'''                           |")
            print("|                                '' '' '    '==='()'=='                                            |")
            print("|                                           '(       )'                                            |")
            print("|                                           '6        '                                            |")   
            print("|                                            \       /            - Hi                             |")
            print("|                                            '       '                                             |") 
            print("|                                            '       '                                             |")
            print("|                                             '      '                                             |") 
            print("|                                              '    '                                              |")
            print("|                                               '..'                                               |")
            print("|                                                                                                  |")
            print(" --------------------------------------------------------------------------------------------------")
            playsound.playsound('hi.wav', False)
            print("\n\n")
            time.sleep(1.5)
            for char in "\n\n###############################\n##         MOTH QUIZ         ##\n###############################\n\nTry to answer 3 moth related questions.\n\n":
                sleep(0.15)
                sys.stdout.write(char)
                sys.stdout.flush()
            moth_quiztime()
        else:
            for char in "\nAwww you scardey mouse...\nYou just lost a potential new friend..\n":
                sleep(0.15)
                sys.stdout.write(char)
                sys.stdout.flush()
            after_spider_quiz()
    elif explore.lower() == "sink":
        for char in "\nYou scurry over to the sink as you're hit by\nthe STENCHHHH of rotten pumpkin spice latte...\n....\nThe sink is full of old plates\nand mold is thriving in the mugs\nThat Wasp meal starts to stir in your tummy..\nLeave?\n[Yes]/[No]\n":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        option = "@@@@"
        while option.lower() != "yes" and option.lower() != "no":
            option = input("Enter Choice: ")
            if option.lower() == "no":
                playsound.playsound('slimy.wav', False)
                for char in "\nGrime is life! You choose to stay n chill\nThinking to yourself 'I love this place!'\n....\nWRONG MOUSEY....You fall sick and say hello to that Wasp again...\n\n":
                    sleep(0.15)
                    sys.stdout.write(char)
                    sys.stdout.flush()
                playsound.playsound('squeaks.wav', False)
                time.sleep(1.5)
                playsound.playsound('dead.wav', False)
                print("\n")
                print(" ------------------------------")
                print("|   !!     !           !!      |
                print("|           .  !   .           |")
                print("|       .  /|     /\  ,    !!  |")    
                print("|    !  |\/ |/\__/  \/|___     |")
                print("|     __|                /     |")
                print("|     \       DEAD!      \  !  |")
                print("|!!   /       -----      _\    |")
                print("|    /___  _  _         _\     |")
                print("|       /,' \| \  /\|\ |       |")
                print("|      /'    `  \/  ` \|    !! |")
                print("|  !!          !          !    |")
                print(" ------------------------------")
                print("\n")
                end_game()
            else:
                after_spider_quiz()
    elif explore.lower() == "cat flap":
        playsound.playsound('cat_purr.wav', False)
        for char in "\nbut you have to jump down from the counter\nCat flap is locked, it uses the cats microchip to open\nThats the only way out :(\n":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        #back to the kitchen counter...
        after_spider_quiz()
    else:
        after_spider_quiz()
def spider_quiztime():    
    wins = 0
    losses = 0
    rounds = 3
    q_num = 1
    tries = 2

    questions = (
        "Is the venom of the female black widow spider more potent,\ndrop per drop, than that of the rattlesnake? ",
        "In what country can the smallest spider in the world be found in? ",
        "Do spiders have more legs than crabs? ",
        "Which country has the deadliest spider,\nbased upon the potency of the venom? ",
        "Which country are the Kauai cave wolf spider\nand the Doloff cave spider found in? ",
        "A spider's silk is approximately twice as strong\nas a steel strand of the same diameter. ",
        "Is the Sydney funnel-web spider another name\nfor the Sydney trapdoor spider? ",
        "Jumping spiders can leap how many times their own body length? ",
        "The largest spider in the world is which of the following? ",
        "Can you stop the flow of blood by putting spider webs on a cut? ",
        "Are there spiders that can mimic ants? ",
        "Has there been a confirmed death in Australia\nbetween the years 1980-2002 due to a spider bite? ",
        "What is the usual minimum number of silk gland\npairs that a spider possesses? ",
        "Is the orb weaver the heaviest spider that is known in Britain? ",
        "Can spiders get trapped in their own webs? "
    )

    answers = (
        "[Yes]     [No] ",
        "[Samoa]     [France]     [Indonesia]     [South Africa] ",
        "[Yes]     [No] ",
        "[Brazil]     [South Africa]     [Australia]     [Russia] ",
        "[New Zealand]     [Peru]     [China]     [USA] ",
        "[True]     [False] ",
        "[Yes]     [No] ",
        "[20]     [30]     [40]     [50] ",
        "[Tropical orb weaver]     [Black Money]     [Cardinal]     [Goliath bird-eating] ",
        "[Yes]     [No] ",
        "[Yes]     [No] ",
        "[Yes]     [No] ",
        "[1]     [2]     [3]     [4] ",
        "[Yes]     [No] ",
        "[Yes]     [No] "
    )

    good_answer = (
        "yes",
        "samoa",
        "no",
        "brazil",
        "usa",
        "true",
        "no",
        "50",
        "goliath bird-eating",
        "yes",
        "yes",
        "no",
        "3",
        "yes",
        "yes"
    )

    wikispider = (
        "The female black widow is the most venomous spider\nin North America and its venom is 2 times more\ntoxic than the rattlesnake's. Though the venom\nis more toxic, they are not as deadly, as the black\nwidow spider can only deliver a single small bite.",
        "This spider is the Paut marplesi from Western Samoa.\nIn 1965 a male specimen was found whose overall\nlength was 0.43 mm or 0.017 inches, which is approximately\nthe size of the full stop (period) at the end of this sentence.",
        "Spiders have 8 legs and crabs have 10 legs.",
        "The banana spider, Brazilian huntsman, and wolf spider\nare regarded as the most lethal in the world and\ncome from Brazil. The criterion of 'deadliest' is given\naccording to the spider's venom yield (lethal potential)\ndivided by their venom potency. The banana spider,\nwhen using this criterion, yields 6mg of venom with\n1 mg being the estimated lethal dosage for human beings.\nThe Brazilian huntsman only needs 0.006 mg to kill a mouse.",
        "The abovementioned were regarded in 2001 as the two\nmost endangered species of spiders by the International\nUnion for the Conservation of Nature.",
        "Spider silk is also being investigated for aiding in\nreplacing damaged tendons and ligaments of humans\nand is being used in bulletproof vests.",
        "The Sydney trapdoor spider is from the family Ictenizidae.\nThey usually construct burrows that are closed\nby a 'door'. Bites from these spiders are rarely\nrecorded and there never has been a fatality\nin Australia resulting from them. The Sydney funnel-web\nspiders belongs to the Atrax and Hadronyche genera\nand are highly venomous. Before the antivenin was discovered,\ntheir bite was often fatal. These spiders build\na flat web with two tunnel-like entrances in a Y configuration.",
        "The jumping spider is the most common spider in the world.\nThis spider has four large eyes on its face as well\nas four small eyes on top of its head. These spiders\nhunt during the day and have good eyesight.\nThe family name for them is Salticidae.",
        "The Goliath bird-eating spider lives mostly in the\nrainforests of Suriname, Guyana and French Guiana; but they\nalso have been found in Venezuela and Brazil. The leg span of\none of these spiders captured in Venezuela in 1965 was\nrecorded at 28 cm or 11 in. The Goliath bird-eating spider feeds mostly on rodents.",
        "A spider web has a natural clotting agent in it.\nWhen put on a cut this can assist in quickly stopping the blood flow.",
        "There are several groups of spiders that have evolved\nto look and behave like ants, flies and wasps, which\nis known as mimicry. A few of these spiders can even smell\nlike ants and are so convincing that the ants themselves\nare tricked, therefore the spider is able to enter\nthe nest easily to steal the young.",
        "There have been no confirmed deaths in Australia due\nto spider bites since 1979. The only two spiders that\nhad caused deaths now have antivenom available. Redback spiders'\nantivenom became available in 1956, and for funnel-web spiders,\nit was introduced in 1980. Antivenom for the funnel-web has been\ngiven to over 100 people annually since 1980.",
        "These glands are found in the rear part of the spider's\nbody and open via holes on the end of another small\norgan called spinnerets. The majority of spiders have\nthree pairs of spinnerets, though some only have one\nor two. Each silk gland pair produces a different\nkind of silk, thus most spiders can produce three\nvarious types of silk.",
        "A female can weigh up to 2.25 grams or 0.08 ounces.",
        "If a spider is startled or disoriented it can be entangled\nin its own web. Usually the spider differentiates\nbetween safe and non-safe or sticky threads, as these\nthreads are made using different types of silk.\nHighly sensitive feet and 'knowing its own web structure'\nprovides the ability for the spider to move freely around."
    )
    while tries > 0:
        tries -= 1
        while wins + losses < rounds:
            rquestion = random.randint(0,14)    #randomize a question
            if q_num == 1:
                q1_index = rquestion
            elif q_num == 2:
                while rquestion == q1_index:
                    rquestion = random.randint(0,14)    #randomize a question again if duplicate
                q2_index = rquestion
            else:
                while rquestion == q1_index or rquestion == q2_index:
                    rquestion = random.randint(0,14)    #randomize a question again if duplicate
            print("Question ",str(q_num))
            print(questions[rquestion])
            q_num += 1
            user_answer = "@@@@"
            while user_answer.lower() not in answers[rquestion].lower():
                user_answer = input(answers[rquestion])
            if user_answer.lower() == good_answer[rquestion]:
                wins += 1
                print("Correct answer!")
                time.sleep(1.5)
                print(wikispider[rquestion])
                time.sleep(3.5)
                print()
            else:
                losses += 1
                print("Wrong answer")
                time.sleep(1.5)
                print("The correct answer was ",good_answer[rquestion].capitalize())
                print(wikispider[rquestion])
                time.sleep(3.5)
        print("You got ",wins," out of ",rounds," correct!")
        time.sleep(1.5)
        if wins == rounds:
            tries = 0
            after_spider_quiz()
        else:
            if tries > 0:
                print("HMMMM.. Close.. You can have one more crack at it")
                print()
                wins = 0
                losses = 0
                rounds = 3
                q_num = 1
                time.sleep(1.5)
    if wins < 3:
        playsound.playsound('boo.wav', False)
        print("BOOO Mousey! You do not know much about spiders..Pfft! ")
        time.sleep(1.5)
        print("I cannot help you...I guess you're stuck here forever")
        time.sleep(1.5)
        playsound.playsound('cat_purr.wav', True)
        time.sleep(1.5)
        playsound.playsound('cat_meow.wav', True)
        time.sleep(1.5)
        playsound.playsound('attack.wav', False)
        time.sleep(1.5)
        playsound.playsound('cat_shreat.wav', False)
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        end_game()

def help_spider():
    print("\n\n")
    playsound.playsound('hi.wav', False)
    print(" -----------------------------------")
    print("|                 |                 |")
    print("|                 |                 |")
    print("|                 |   - Hola!       | ")
    print("|                 |                 | ")
    print("|             /   |   \             | ")
    print("|             \   |   /             | ")
    print("|           .  --\|/--  ,           | ")
    print("|            '--|___|--'            |")
    print("|            ,--|___|--,            | ")
    print("|           '  /\o o/\  `           | ")
    print("|             +   +   +             |")
    print("|              `     '              |")
    print("|                                   |")
    print(" -----------------------------------")
    print("\n\n")
    playsound.playsound('attack.wav', False)
    for char in "\nThe three of you start brawling dust is flying\nYou make a sudden jump in the wasps direction\npinning him to the window, he cant get away...\nThe Spider karate chops the Wasp with her 8 legs\n\n!!SUPER POWER KICK!!\n\nThe wasp is DEAD!!!\nThe Spider offers you some of the Wasp\nto feast on as thank you.....\nHis fresh delicacy that you assisted in preparing...\nDo you accept this offer?\n[Yes]/[No]\n":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    eat_offer = "@@@@"
    while eat_offer.lower() != "yes" and eat_offer.lower() != "no":
        eat_offer = input("Enter Choice: ")
    if eat_offer.lower() == "yes":
        for char in "\n'GROSS' you think.. you mull it over thinking 'Fine..\nI want to be polite and I need the help..\nBut i'm really not pleased about it..'\nHolding your little mousey nose you swallow the wasp chunk whole\nThe Spider smiles and says 'ITS QUIZ TIME!!'":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        playsound.playsound('gameshow.wav', False)
        for char in "\n\n###############################\n##        SPIDER QUIZ        ##\n###############################\n\nTry to answer 3 spider related questions\n\n":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        spider_quiztime()
    else:
        for char in "\n'GROSS NOPE'\n'NOT HAPPENING'\nYou say outloud!!\nYou quick reaction has offended the Spider!!\n....\nThe Spider dashes towards you spinning you up in a web\n....\n......you scream HELP......\nThe cat MEOWS in the distance...\n":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        playsound.playsound('squeaks.wav', False)
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()

def help_wasp():
    print("\n")
    for char in "\nThe Spider and Wasp continue brawling around with dust flying\nArms flalling and the Wasp near misses the Spider\nwith it's stinger but he just manages to push the Spider away\nBut you're stood to close and he thinks you're after\nhim too...\nOUCHHHHH!\n....\n\nYOU'VE BEEN STUNG!!\n....You're falling to the floor in pain....\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")
    print(" ------------------------------")
    print("|   !!     !           !!      |
    print("|           .  !   .           |")
    print("|       .  /|     /\  ,    !!  |")    
    print("|    !  |\/ |/\__/  \/|___     |")
    print("|     __|                /     |")
    print("|     \       SPLAT!     \  !  |")
    print("|!!   /       -----      _\    |")
    print("|    /___  _  _         _\     |")
    print("|       /,' \| \  /\|\ |       |")
    print("|      /'    `  \/  ` \|    !! |")
    print("|  !!          !          !    |")
    print(" ------------------------------")
    print("\n")
    playsound.playsound('splat.wav', False)
    time.sleep(1.5)
    playsound.playsound('squeaks.wav', False)
    time.sleep(1.5)
    playsound.playsound('dead.wav', False)
    print("\n")
    print(" ------------------------------")
    print("|   !!     !           !!      |
    print("|           .  !   .           |")
    print("|       .  /|     /\  ,    !!  |")    
    print("|    !  |\/ |/\__/  \/|___     |")
    print("|     __|                /     |")
    print("|     \       DEAD!      \  !  |")
    print("|!!   /       -----      _\    |")
    print("|    /___  _  _         _\     |")
    print("|       /,' \| \  /\|\ |       |")
    print("|      /'    `  \/  ` \|    !! |")
    print("|  !!          !          !    |")
    print(" ------------------------------")
    print("\n")
    time.sleep(1.5)
    end_game()
def go_option3():  
    for char in "\n\nYou run to the bottom of the velvet curtains who look like\ntheyve seen better days....\nBillows of dust come flying off as you scale\nthe curtain to the top trying not to\nchoke as you get a better vantage point....\nYou see a web on the window sill,\nwhere a Spider is being attacked by a\nmean looking Wasp.\n\nWho do you want to help?\n[Spider]/[Wasp]\n":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    who_to_help = "@@@@"
    while who_to_help.lower() != "spider" and who_to_help.lower() != "wasp":
        who_to_help = input("Enter Choice: ")
    if who_to_help.lower() == "spider":
        help_spider()
    elif who_to_help.lower() == "wasp":
        help_wasp()
# OPTION TWO
# DADDY EXTRA HELP IF USER LOSES
def daddy_lose():
    print("\n\n")
    playsound.playsound('squeaks.wav', False)
    for char in "'Too bad.. I am kind of insulted that\nyou know so little about us Daddy Longlegs..\nbut im feeling generous so i'll give you\na long list of places to look..\n[A: Behind the paint tins]\n[B: Next to the bass guitar amp]\n[C: By the crabbing nets]\n[D: Derelict dollshouse]\n[E: Leaf Blower]\nAnswer: \n":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    places_choice = input()
    if places_choice == "D" or places_choice == "d" or places_choice == "Derelict Dollshouse" or places_choice == "derelict dollshouse" or places_choice == "DERELICT DOLLSHOUSE":
        print("\n")
        for char in "You thank the Daddy Longlegs and begin on your way\ntowards the derelict dollshouse that looks just as scary\nas the big house you're in..\nYou peak through the window to see combwebs everywhere\nMiniture furniture covered in dust and mildew..\nContinuing round the back of the house\nyou approach with caution..\nyou hear a loud\nCRREEEEEAAAAAAKK!!\n...purrrrrrrrr!\n...\n...\nyou gulp and remind yourself this is your only chance out of here...":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        you_won()
    elif places_choice == "A" or places_choice == "a" or places_choice == "Behind the paint tins" or places_choice == "behind the paint tins" or places_choice == "Behind The Paint Tins" or places_choice == "BEHIND THE PAINT TINS" or places_choice == "paint tins" or places_choice == "Paint Tins" or places_choice == "PAINT TINS":
        print("\n")
        for char in "You thank the Daddy Longlegs and begin on your way..\n'Oh please let there be a hole behind\nthose paint cans' you think...\nYou hear 'MEOWING' in the distance...\nThree paint cans gather together in a corner\nlooking omnious from your view.....\nYou get closer\n....\n\nOHHHH\n\bOOOPS!\n\nWrong choice.. You walk back to the Daddy Longlegs\n...\n'Hi Mousey, lets try again with that quiz...'\n" :
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        daddy_quiz1()
    elif places_choice == "B" or places_choice == "B" or places_choice == "Next to the bass guitar amp" or places_choice == "next to the bass guitar amp" or places_choice == "NEXT TO THE BASS GUITAR AMP" or places_choice == "Guitar amp" or places_choice == "guitar amp" or places_choice == "Guitar Amp" or places_choice == "GUITAR AMP" or places_choice == "CRABBING NETS":
        print("\n")
        for char in "You thank the Daddy Longlegs and begin on your way..\nIn the corner of the room you see the bass guitar amp\nthe cats water bowl is sat right next to it, full to the brim\n...It's a risky move\n...\nYou tiptoe round the back of the cans..\nOOOPS! Wrong choice.. The hole has been filled in!\n....\n\nYou walk back to the Daddy Longlegs\n....\n'Hi Mousey, lets try again with that quiz...'\n":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        daddy_quiz1()
    elif places_choice == "C" or places_choice == "c" or places_choice == "by the crabbing nets" or places_choice == "By the crabbing nets" or places_choice == "By The Crabbing Nets" or places_choice == "BY THE CRABBING NETS" or places_choice == "crabbing nets" or places_choice == "Crabbing nets" or places_choice == "Crabbing Nets" or places_choice == "CRABBING NETS":
        print("\n")
        playsound.playsound('cat_purr.wav', False)
        for char in "You thank the Daddy Longlegs and begin on your way..\nIn the conservatory you see some large crabbing nets\ndraped over some old cardboard boxes..\nWhat's that you can hear...\npurrrrrrr!!\nPURRRRRR..!!\nIt seems to be getting closer...\n\nRUN RUN! BEFORE THE CAT GETS YOU!\n\n....You run with all your might towards those crabbing nets and boxes\n....\nClimbing up the net as fast as you can\nto see if the window is open...\n....\nThe cat 'MEEOOWWWWS' below you..\nOH NO THE WINDOW IS TOO HIGH\n....\nSuddenly there is a loud BANGING and calls of 'Oh kitty cat, diner time!'\nThe cat runs out the room\nYou dash back down the crabbing nets to the floor and back\nout the room!\nPHEW! That was so close!\n\nYou walk back to the Daddy Longlegs\n...\n'Hi Mousey, lets try again with that quiz...'\n":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        daddy_quiz1()
    elif places_choice == "E" or places_choice == "e" or places_choice == "Leaf blower" or places_choice == "leaf blower" or places_choice == "Leaf Blower" or places_choice == "LEAF BLOWER":
        print("\n")
        leaf_blower2 = "You spot the leaf blower up on the sideboard\nIt looks so far away from down on the ground..\nYou shimmy your way up the back...\nDigging your little claws in for your life..\n Once you get to the top you manage to spot a toad\nwho with a sinister grin on his face offers\nto sit on the button for you help...\nYou scramble to the opening of the leaf blower\n...\The open window in sight...\nThe toad says '1....\n....2\n....\n...3!!!\nHe sits on the button\nYou fly through the air....\n\nUGH OHHHHHHH\n\nYou miss\nand\n....\nSPLAAAAAATTTT!!!\n.....\n....."
        for char in leaf_blower2:
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       SPLAT!     \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        playsound.playsound('splat.wav', False)
        time.sleep(1.5)
        playsound.playsound('squeaks.wav', False)
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    else:
        print("\n\n")
        print("'OOOPS! That's not an option, please try again!'")
        daddy_lose()   
# DADDY HELP AFTER THE USER WINS THE QUIZ
def daddy_help():
    daddy_clues = "'Ok well done you! I'll give you two clues to choose from..\nYou can potentially escape with the leaf blower\nor\nbehind the derelict dolls house..\n[A: Leaf blower]/[B: Derelict Dollshouse]\nAnswer: \n"
    if daddy_clues == "B" or daddy_clues == "b" or daddy_clues == "derelict dollshouse" or daddy_clues == "Derelict dollshouse" or daddy_clues == "Derelict Dollshouse" or daddy_clues == "dollshouse" or daddy_clues == "Dollshouse" or daddy_clues == "DOLLSHOUSE":
        success = "You thank the Daddy Longlegs and begin on your way\ntowards the derelict dollshouse that looks just as scary\nas the big house you're in..\nyou approach with caution..\nyou hear a loud\nCRREEEEEAAAAAAKK!!\n...purrrrrrrrr!\n...\nyou gulp and remind yourself this is your only chance out of here..."
        for char in success:
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        playsound.playsound('squeaks.wav', False)
        you_won()
    elif daddy_clues == "A" or daddy_clues == "a" or daddy_clues == "Leaf blower" or daddy_clues == "leaf blower" or daddy_clues == "Leaf Blower" or daddy_clues == "LEAF BLOWER":
        leaf_blower = "You spot the leaf blower up on the sideboard\nIt looks so far away from down on the ground..\nYou shimmy your way up the back...\nDigging your little claws in for your life..\n Once you get to the top you manage to spot a toad\nwho with a sinister grin on his face offers\nto sit on the button for you help...\nYou scramble to the opening of the leaf blower\n...\The open window in sight...\nThe toad says '1....\n....2\n....\n...3!!!\nHe sits on the button\nYou fly through the air....\n\nUGH OHHHHHHH\n\nYou miss\nand\n....\nSPLAAAAAATTTT!!!\n.....\n....."
        for char in leaf_blower:
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       SPLAT!     \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        playsound.playsound('splat.wav', False)
        time.sleep(1.5)
        playsound.playsound('squeaks.wav', False)
        time.sleep(1.5)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        playsound.playsound('dead.wav', False)
        print("\n")
        end_game()
    else: 
        print("\n\n")
        wrong_entry = "'Sorry that isnt one of the clues I gave you, silly mouse. Try again!'"
        for char in wrong_entry:
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        daddy_help()
# DADDY LONGLEGS QUIZ
# Question 3:
def daddy_quiz3():
    print("\n")
    print(" ---------------
    print("|     ┏━━━┓     |")
    print("|     ┃┏━┓┃     |")
    print("|     ┗┛┏┛┃     | ")
    print("|       ┃┏┛     |")
    print("|       ┏┓      |")
    print("|       ┗┛      |")
    print(" ---------------
    print("\n")
    daddy_score = 2
    daddy_answer3 = input("How many species of Daddy Longlegs are there in the world?\n[A: 10,000] \n[B: 100]\n[C: 500]\nAnswer: \n")
    if daddy_answer3 == "A" or daddy_answer3 == "a" or daddy_answer3 == "10,000" or daddy_answer3 == "10000":
        daddy_score += 1
        time.sleep(1.5)
        playsound.playsound('correct.wav', False)
        print("Correct!")
        time.sleep(1.5)
        print("Fun fact: There might be as many as 10,000 species of daddy longlegs, with 6000 to 7000 currently described. We’re describing new ones all the time, they are generally very, very bad at getting around, so they tend to have lots of species, because the minute a river flows between two different populations or a mountain rises and cuts one population off from another population, they split into two new species.")
        print("Score: ", daddy_score)
        time.sleep(4)
        print("You won! Ok i'll help you!")
        time.sleep(1.5)
        print("\n\n")
        daddy_help()
    else:
        playsound.playsound('wrong.wav', False)
        time.sleep(1.5)
        playsound.playsound('boo.wav', False)
        print("Booooo! WRONG!")
        time.sleep(1.5)
        print("Score: ", daddy_score)
        time.sleep(1.5)
        print("LOSER!")
        time.sleep(2)
        daddy_lose()
# Question 2:
def daddy_quiz2():
    print("\n")
    print(" ---------------
    print("|     ┏━━━┓     |")
    print("|     ┃┏━┓┃     |")
    print("|     ┗┛┏┛┃     | ")
    print("|       ┃┏┛     |")
    print("|       ┏┓      |")
    print("|       ┗┛      |")
    print(" ---------------
    print("\n")
    daddy_score = 1
    daddy_answer2 = input("How old are Daddy Longlegs as a species? \n[A: 100 million years]\n[B: 1 year]\n[C: 400 million years]\nAnswer: \n")
    if daddy_answer2 == "c" or daddy_answer2 == "C" or daddy_answer2 == "400 million years" or daddy_answer2 == "400" or daddy_answer2 == "400 Million Years" or daddy_answer2 == "400 MILLION YEARS" or daddy_answer2 == "400 Million years":
        daddy_score += 1
        playsound.playsound('correct.wav', False)
        time.sleep(1.5)
        print("Look at you go! Maybe ill let you be\nan honourary Daddy Longleg {}".format(name))
        time.sleep(1.5)
        print("Fun fact: It is believed daddy longlegs split off from scorpions, which were becoming terrestrial about 435 million years ago. To put this in perspective, this is about 200 million years before dinosaurs appeared, which were only around for about 165 million years.")
        print("Score: ", daddy_score)
        time.sleep(4)
        print("\n\n")
        daddy_quiz3()
    else:
        playsound.playsound('wrong.wav', False)
        time.sleep(1.5)
        playsound.playsound('boo.wav', False)
        print("Booooo! WRONG!")
        time.sleep(1.5)
        print("Score: ", daddy_score)
        time.sleep(1.5)
        print("LOSER!")
        time.sleep(2)
        daddy_lose()
# Question 1:
def daddy_quiz1():
    print("\n")
    print(" ---------------
    print("|     ┏━━━┓     |")
    print("|     ┃┏━┓┃     |")
    print("|     ┗┛┏┛┃     | ")
    print("|       ┃┏┛     |")
    print("|       ┏┓      |")
    print("|       ┗┛      |")
    print(" ---------------
    print("\n")
    daddy_score = 0
    daddy_answer1 = input("Are Daddy Longlegs Spiders?\n[A: Yes]\n[B: No]\nAnswer: \n")
    if daddy_answer1 == "b" or daddy_answer1 == "B" or daddy_answer1 == "No" or daddy_answer1 == "no" or daddy_answer1 == "No" or daddy_answer1 == "N"or daddy_answer1 == "n":
        time.sleep(1.5)
        daddy_score += 1
        playsound.playsound('correct.wav', False)
        print("Yes! Wow im impressed {}!".format(name))
        time.sleep(1.5)
        print("Score: ", daddy_score)
        print("Fun fact: Yes, they’re arachnids, but they’re actually more\nclosely related to scorpions than they are to spiders.\nThey don’t produce silk, have just one pair of eyes,\nand have a fused body (unlike spiders, which have\na narrow “waist” between their front and rear)")
        time.sleep(4)
        print("\n\n")
        daddy_quiz2()
    else:
        playsound.playsound('wrong.wav', False)
        time.sleep(1.5)
        playsound.playsound('boo.wav', False)
        print("Booooo! WRONG!")
        time.sleep(1.5)
        print("Score: ", daddy_score)
        time.sleep(1.5)
        print("LOSER!")
        time.sleep(2)
        daddy_lose()
# DADDY LONGLEGS
def daddy_longlegs():
    daddy_approach = "You approach the entrance and theres is no\nDaddy Longlegs in sight. You keep walking down\na steep dark pathway when suddenly\n....\n\nBANG!!!!\n\nYou have ran into the Daddy Longlegs after all.."
    for char in daddy_approach:
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(2)
    print("\n\n")
    print(" -------------------------------------------")
    print("|                                           |")
    print("|            | |     |     |                |")
    print("|             \ \    |    /                 |")
    print("|              \ \   |   /                  | ")
    print("|               \ \  |  /                   | ") 
    print("|                \ \ | /                    |")
    print("|                 \ \|/                     |")
    print("|                _____                      |")
    print("|               '||  (o)  - hellooo         |") 
    print("|               `---'--                     |")
    print("|                 / /|\                     |")
    print("|                / / | \                    | ")
    print("|               / /  |  \                   |")
    print("|              / /   |   \                  | ")
    print("|             / /    |    \                 |")
    print("|            | |     |     |                |")
    print("|                                           |")
    print(" -------------------------------------------")
    print("\n\n")
    playsound.playsound('hello.wav', False)
    time.sleep(1.5)
    daddy_hello = "'Oh hello you fuzzy little thing\nOh you want my help!\nFirst things first, us Daddy Longlegs are\nvery proud bugs especially of our long\nlooooonggggggg legs.\nSo you must answer some questions!\nGet them right and i'll help you get out of here!' "
    for char in daddy_hello:
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1.5)
    playsound.playsound('gameshow.wav', False)
    print("\n\n")
    print("\n\n###############################\n##        DADDY LONGLEGS QUIZ        ##\n###############################\n\n")
    time.sleep(2)
    print("\n\n")
    daddy_quiz1()
# daddy_longlegs()

def gerbil_choice():
    for char in "\nYou successfully navigated the Percy the Gerbil's quiz.\nAs a means of congratulations, he would like to offer you a tip.\nIt is up to you which one you choose..\n\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    for char in "The Gerbil presents you with two pieces of advice..\n\nBut..Do you trust the Gerbil?\n[A: He points towards the Hot Wheels ramp leading to a window that has been left ajar]\n[B: The Gerbil disuades you from going entering the small crack located\nbehind the radiators it is guarded by a vicious Daddy Longlegs and the path leads to nowhere]\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    gerbil_a_b = input
    if gerbil_a_b == "A" or gerbil_a_b == "a" or gerbil_a_b == "B" or gerbil_a_b == "b" and trust_gerbil == "Y":
        for char in "\nYou chose to follow the Gerbil's advice\nYou brace yourself inside the Hot Wheels car\nAs that devious little Gerbil presses the GO button\n\nOHHH NOOOO\n\nHe knew what he was doing\n...\nTheres no way youre going to make it...\nAHHHH...":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       SPLAT!     \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        playsound.playsound('splat.wav', False)
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        end_game()
    elif gerbil_a_b == "A" or gerbil_a_b == "a" or gerbil_a_b == "B" or gerbil_a_b == "b" and trust_gerbil == "N":
        print("Very wise indeed... That pesky Gerbil wasnt to be trusted!!\nYou now make your way to the entrance\n")
        daddy_longlegs()
    else:
        print("I do not recognise that option. Please check your spelling and try again")
        gerbil_choice()
def gerbil_quiz_3():
    for char in "'HMMMM...Who'd of guessed it...?!\nYou have made to the last quiz...'\nNow Percy is looking at you even more annoyed...\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")
    print(" ---------------
    print("|     ┏━━━┓     |")
    print("|     ┃┏━┓┃     |")
    print("|     ┗┛┏┛┃     | ")
    print("|       ┃┏┛     |")
    print("|       ┏┓      |")
    print("|       ┗┛      |")
    print(" ---------------
    print("\n")
    response_gerbil_3 = input("Can you name the country located in West Africa?\n[A: Kenya]\n[B: Ethiopia]\n[C: Ghana]\nAnswer: \n")
    if response_gerbil_3 == "A" or response_gerbil_3 == "a" or response_gerbil_3 == "ENTER":
        playsound.playsound('wrong.wav', False)
        print("WRONG!!!!\nLooks like your luck has ran out!\n")
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    elif response_gerbil_3 == "B" or response_gerbil_3 == "b" or response_gerbil_3 == "ENTER":
        playsound.playsound('wrong.wav', False)
        print("WRONG!!!!\nLooks like your luck has ran out!\n")
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        time.sleep(1.5)
        print("\n")
        end_game()
    elif response_gerbil_3 == "C" or response_gerbil_3 == "c" or response_gerbil_3 == "ENTER":
        playsound.playsound('correct.wav', False)
        print("CORRECT!!\nWELL DONE\n3 for 3!!\n")
        gerbil_choice()
    else:
        print("I do not recognise that option. Please check your spelling and try again")
        gerbil_quiz_3()

def gerbil_quiz_2():
    for char in "So you have made it to the next round.\nOn to question two...\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")
    print(" ---------------
    print("|     ┏━━━┓     |")
    print("|     ┃┏━┓┃     |")
    print("|     ┗┛┏┛┃     | ")
    print("|       ┃┏┛     |")
    print("|       ┏┓      |")
    print("|       ┗┛      |")
    print(" ---------------
    print("\n")
    response_gerbil_2 = input("Who is the most popular DC comic character?\n[A: Batman]\n[B: Superman]\n[C: Wonder Woman]\nAnswer: \n")
    if response_gerbil_2 == "A" or response_gerbil_2 == "a" or response_gerbil_2 == "ENTER":
        playsound.playsound('correct.wav', False)
        print("You guessed it right!!\nOne more question!!\n")
        time.sleep(1.5)
        gerbil_quiz_3()
    elif response_gerbil_2 == "B" or response_gerbil_2 == "b" or response_gerbil_2 == "ENTER":
        playsound.playsound('wrong.wav', False)
        print("NOOOOOOOOOOOOOOOO\nLooks like your luck has ran out!\n")
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    elif response_gerbil_1 == "C" or response_gerbil_1 == "c" or response_gerbil_1 == "ENTER":
        playsound.playsound('wrong.wav', False)
        print("NOOOOOOOOOOOOOOOO\nLooks like your luck has ran out!\n")
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    else:
        print("I do not recognise that option. Please check your spelling and try again")
        gerbil_quiz_2()

def gerbil_quiz_1():
    playsound.playsound('gameshow.wav', False)
    for char in "\n\n###############################\n##        GERBIL QUIZ        ##\n###############################\n\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n\n")
    for char in "Welcome to the fantantic world of Gerbils.\nThink very carefully about the next step you take, it is crucial!\nIf you choose the wrong answer you could delay your path.\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")
    print(" ---------------
    print("|     ┏━━━┓     |")
    print("|     ┃┏━┓┃     |")
    print("|     ┗┛┏┛┃     | ")
    print("|       ┃┏┛     |")
    print("|       ┏┓      |")
    print("|       ┗┛      |")
    print(" ---------------
    print("\n")
    response_gerbil_1 = input("Which of these following Disney characters is a prince?\n[A: Charming]\n[B: Mark]\n[C: Jorneal]\nAnswer: \n")
    if response_gerbil_1 == "A" or response_gerbil_1 == "a" or response_gerbil_1 == "Charming":
        playsound.playsound('correct.wav', False)
        print("You guessed it right!!\nYou live to see the next day!!\nTwo more questions to go!!\n")
        time.sleep(1.5)
        gerbil_quiz_2()
    elif response_gerbil_1 == "B" or response_gerbil_1 == "b" or response_gerbil_1 == "Mark":
        playsound.playsound('wrong.wav', False)
        print("NOOOOOOOOOOOOOOOO\nLooks like your luck has ran out!\n")
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    elif response_gerbil_1 == "C" or response_gerbil_1 == "c" or response_gerbil_1 == "Jorneal":
        playsound.playsound('wrong.wav', False)
        print("NOOOOOOOOOOOOOOOO\nLooks like youre WRONG!\n")
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    else:
        print("I do not recognise that option. Please check your spelling and try again")
        gerbil_quiz_1()


def dog_cat_choice():
    for char in "\nYou feel the weight of the world on your shoulders.\nJust as you thought you could relax, you have another\nimportant decision to make...Racing down the corridor you hacve to decide..\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    dog_cat_response = input("Do you carry on running like Usain Bolt, knowing that you can make it past the dog or accept your fate and sacrifice yourself to be a tasty meal?\n[A: Carry on running like Usain Bolt]\n[B: Accept your fate]\nAnswer: \n")
    if dog_cat_response == "A" or dog_cat_response == "a" or dog_cat_response == "carry on running like Usain Bolt":
        for char in "LUCKY SHOT!!\nLenny comes running and scares the cat away\n....\nThe cat runs out of the cat flap whilst you see\na little hole beside of it to run through\n":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        playsound.playsound('cat_shreak.wav', False)
        time.sleep(1.5)
        for char in "WOOHOO....\nYOU MADE IT OUT!\n":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        you_won()
    elif dog_cat_response == "B" or dog_cat_response == "b" or dog_cat_response == "Accept your fate":
        for char in "YUM YUM\nI love the taste of scared mouse!\n":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        playsound.playsound('squeaks.wav', False)
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    else:
        print("I do not recognise that option. Please check your spelling and try again")
        dog_cat_choice()
#dog_cat_choice()

def dog_escape():
    for char in "\nThis dog is really a lonely old soul and just\nwanted the company. 'Hi Im Lenny' says the dog as he sweeps you\nof your little limbs and takes your away\nfrom the room. Lenny is gentle at heart and just wanted a little company.\n\nBefore you know it, hours have passed on\nLenny's back as he recalls his fondest memories and moments.\n\nYou also remember that you prefer to be alone and search\nfor an escape route. You know Lennie is reluctant to let you\nleave him, but you plot your departure nontheless.\nYou devise a plan and ask Lenny to take you outside.\n\nHe refuses point blank and he reminds you that now you are his best friend. \nOtherwise his 42 teeth can eat you in less than 5 seconds.\nYou now need to make a decision!\n\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1.5)
    print("\n\n")
    print(" --------------------------------------------------------------------------")
    print("|                                                                          |")
    print("|                                     ,._                                  | ")
    print("|                             ,--.    |   `-.                              | ")
    print("|                          ,-'    \   :      `-.                           | ")
    print("|                         /__,.    \  ;  `--.___)                          |")
    print("|                        ,'    \    \/   /       ,-'`.                         ")
    print("|                           __,-' - /   '\      '   ,'                     |  ")
    print("|                       ,-'              `-._ ,---^.                       |  ")
    print("|                        \   ,                `-|                          | ")
    print("|                         \,(o                  ;    |                     | ")
    print("|                     _,-'   `-'                |    |                     |")
    print("|                  ,-'                          |    |                     |")
    print("|              Y8PYF                            ;    ;                     | ")
    print("|              `"" `           ,         ,--   /    :                      | ")
    print("|               \      .   ___/|       ,'\   ,' ,'  ;                      |")
    print("|                `.     ;-' ___|     ,'  |\   ,'   /                       |")
    print("|                  `---'  __\ /    ,'    | `-'   ,'                        |")
    print("|            ,-           \ ,'   ,'      `--.__,'                          |")
    print("|          ,'     ,-'     ,'    /                      -GRRRRRR!!          | ")
    print("|               ,'  ,     `----'                                           | ")
    print("|                 ,'                                                       | ")
    print("|                (                                                         | ")
    print("|                                                                          | ")
    print("|                                                                          |")
    print(" --------------------------------------------------------------------------")
    print("\n\n")
    playsound.playsound('dead.wav', False)
    print("\n")
    print(" ------------------------------")
    print("|   !!     !           !!      |
    print("|           .  !   .           |")
    print("|       .  /|     /\  ,    !!  |")    
    print("|    !  |\/ |/\__/  \/|___     |")
    print("|     __|                /     |")
    print("|     \       DEAD!      \  !  |")
    print("|!!   /       -----      _\    |")
    print("|    /___  _  _         _\     |")
    print("|       /,' \| \  /\|\ |       |")
    print("|      /'    `  \/  ` \|    !! |")
    print("|  !!          !          !    |")
    print(" ------------------------------")
    print("\n")
    time.sleep(1.5)
    playsound.playsound('squeaks.wav', False)
    time.sleep(1.5)
    for char in "Do you promise to sit with Lenny, his kid\nowner Andy and watch Shrek 1 together.\nThen as soon as they fall asleep you make a mad\ndash for your escape or nip him and run for it now?\n[A: Promise to sit with Lenny]\n[B: Nip him and run]\nAnswer: \n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    escape_decision = input()
    if escape_decision == "A" or escape_decision == "a" or escape_decision == "promise to sit with Lenny":
        for char in "\nYou hang out with Lenny and Andy, thinking to yourself\n'They really did well with all of the Shrek movies!'\nWhen you suddenly notice something\nmoving in a glass bowl up on a table\n....\n\nAha! You climb and meet Percy the Gerbil\n....\nHe seems friendly but also kind of angry at you\nYou're not sure why...\nBut he could be your ticket out of here\nSo you chat to him some more and he agrees\nto help you if you get his questions right too!\n":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("\n\n")
        print(" -------------------------------------------------------")
        print("|                                                       |")
        print("|         ) _     _                                     |")
        print("|        ( (^)-~-(^)                                    | ")
        print("|    __,-.\_( 6 6 )__,-.___   Pffft what sort           |")
        print("|      'M'   \   /   'M'       of name is ".format(name))
        print("|             >o<                                       |")                       
        print("|                                                       |")
        print(" -------------------------------------------------------")
        print("\n\n")
        time.sleep(1.5)
        gerbil_quiz_1() 
    elif escape_decision == "B" or escape_decision == "b" or escape_decision == "Nip him and run":
        for char in "You sink your tiny mousey teeth into Lenny\nHe let's out a loud\nOOUUCCCCCHHHHH!\nHeart POUNDING you race down the stairs and into the kitchen\n....":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        playsound.playsound('ouch.wav', False)
        time.sleep(1)
        playsound.playsound('squeaks.wav', False)
        time.sleep(1.5)
        for char in "You can feel the dog's breath beating on your back\nand the cat is a few metres ahead\nYou must make a choice in a split second. Do you...":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        dog_cat_choice()
    else:
        print("I do not recognise that option. Please check your spelling and try again")
        dog_escape()
#dog_escape()

def dog_quiz_3():
    playsound.playsound('cat_purr.wav', False)
    for char in "I see you have made it to the final step of this quiz.\nLAST ROUND\nGet this correct and I will help you!\nTime for the 3rd question!\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1.5)
    print("\n")
    print(" ---------------
    print("|     ┏━━━┓     |")
    print("|     ┃┏━┓┃     |")
    print("|     ┗┛┏┛┃     | ")
    print("|       ┃┏┛     |")
    print("|       ┏┓      |")
    print("|       ┗┛      |")
    print(" ---------------
    print("\n")
    response_dog_3 = input("How many teeth does a normal, adult dog possess?\n[A: 38]\n[B: 42]\n[C: 46]\nAnswer: \n")
    if response_dog_3 == "A" or response_dog_3 == "a" or response_dog_3 == "38":
        playsound.playsound('wrong.wav', False)
        print("NOOOOOOOOOOOOOOOO\nWrong answer!!\nYou sacrificed your life to be the cat's tasty meal!")
        time.sleep(1.5)
        playsound.playsound('cat_shreak.wav', False)
        time.sleep(1.5)
        playsound.playsound('squeaks.wav', False)
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    elif response_dog_3 == "B" or response_dog_3 == "b" or response_dog_3 == "42":
        playsound.playsound('correct.wav', False)
        print("CORRECT {}!!\nYou now climb onto the dog's back.\n...\nYou now really want to get away\n".format(name))
        time.sleep(1.5)
        dog_escape()
    elif response_dog_3 == "C" or response_dog_3 == "c" or response_dog_3 == "46":
        playsound.playsound('wrong.wav', False)
        print("NOOOOOOOOOOOOOOOO\nWrong answer!!\nYou sacrificed your life to be the cat's tasty meal!")
        time.sleep(1.5)
        playsound.playsound('cat_shreak.wav', False)
        time.sleep(1.5)
        playsound.playsound('squeaks.wav', False)
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    else:
        print("I do not recognise that option. Please check your spelling and try again")
        dog_quiz_3()
#dog_quiz_3()

def dog_quiz_2():
    for char in "Well wellll mousey, I see you have made it to step 2.\nTime for your second question\nYoure so close!!\n ":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")
    print(" ---------------
    print("|     ┏━━━┓     |")
    print("|     ┃┏━┓┃     |")
    print("|     ┗┛┏┛┃     | ")
    print("|       ┃┏┛     |")
    print("|       ┏┓      |")
    print("|       ┗┛      |")
    print(" ---------------
    print("\n")
    response_dog_2 = input("Name the most popular dog breed in the world:\n[A: Corgi]\n[B: Border Collie]\n[C: Labrador]\nAnswer: \n")
    if response_dog_2 == "A" or response_dog_2 == "a" or response_dog_2 == "Corgi" or response_dog_2 == "corgi":
        playsound.playsound('wrong.wav', False)
        print("NOOOOOOOOOOOOOOOO\nWrong answer!!\nYou sacrificed your life to be the cat's tasty meal!")
        time.sleep(1.5)
        playsound.playsound('cat_shreak.wav', False)
        time.sleep(1.5)
        playsound.playsound('squeaks.wav', False)
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    elif response_dog_2 == "B" or response_dog_2 == "b" or response_dog_2 == "Border Collie":
        playsound.playsound('wrong.wav', False)
        print("NOOOOOOOOOOOOOOOO\nWrong answer!!\nYou sacrificed your life to be the cat's tasty meal!")
        time.sleep(1.5)
        playsound.playsound('cat_shreak.wav', False)
        time.sleep(1.5)
        playsound.playsound('squeaks.wav', False)
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    elif response_dog_2 == "C" or response_dog_2 == "c" or response_dog_2 == "Labrador":
        playsound.playsound('correct.wav', False)
        print("Correct Mousey!!\nYou have survived for now\n....\nLast question remaining\n")
        time.sleep(1.5)
        dog_quiz_3()
    else:
        print("I do not recognise that option. Please check your spelling and try again")
        dog_quiz_2()
#dog_quiz_2()

def dog_quiz_1():
    playsound.playsound('gameshow.wav', False)
    for char in "\n\n###############################\n##         DOG QUIZ        ##\n###############################\n\nWelcome to the wonderful world of canine conundrums.\nThink very well and answer wisely.\nThese questions really are a matter of life or death.\nAny wrong answer and you will be a fine dinner.\n\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")
    print(" ---------------
    print("|     ┏━━━┓     |")
    print("|     ┃┏━┓┃     |")
    print("|     ┗┛┏┛┃     | ")
    print("|       ┃┏┛     |")
    print("|       ┏┓      |")
    print("|       ┗┛      |")
    print(" ---------------
    print("\n")
    response_dog_1 = input("Which of these characters is a Disney dog?\n[A: Mickey]\n[B: Pluto]\n[C: Donald]\nAnswer: \n")
    if response_dog_1 == "A" or response_dog_1 == "a" or response_dog_1 == "Mickey":
        playsound.playsound('wrong.wav', False)
        print("NOOOOOOOOOOOOOOOO\nWrong answer!!\nYou sacrificed your life to be the cat's tasty meal!")
        time.sleep(1.5)
        playsound.playsound('cat_shreak.wav', False)
        time.sleep(1.5)
        playsound.playsound('squeaks.wav', False)
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    elif response_dog_1 == "B" or response_dog_1 == "b" or response_dog_1 == "Pluto":
        playsound.playsound('correct.wav', False)
        print("Well done {}, you're a Disney fan I see!\nYou have survived for now. 2 questions left\n".format(name))
        time.sleep(1.5)
        dog_quiz_2()
    elif response_dog_1 == "C" or response_dog_1 == "c" or response_dog_1 == "Donald":
        playsound.playsound('wrong.wav', False)
        print("UH OH...\nWrong answer\nYou sacrificed your life to be the cat's tasty meal!\n\nGULPPPPP\n")
        time.sleep(1.5)
       playsound.playsound('cat_shreak.wav', False)
        time.sleep(1.5)
        playsound.playsound('squeaks.wav', False)
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    else:
        print("I do not recognise that option. Please check your spelling and try again")
        dog_quiz_1()
#dog_quiz_1()

def response_ko_a(): 
    for char in "\nOK\nYou spot a worried looking dog out the room\nGesturing to you with puppy dog eyes..DO YOU NEED HELP!\nIt looks like you have two options...\nYou skate like clappers out of the room..\nHopefully you make it passed the cat to the dog\nor do you run back under the TV where you were safe before?\n\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    response_a= input("Do you skate like the clappers or run beneath the TV?\n[A: Skate like the clappers]\n[B: Run beneath the TV]\n")
    if response_a == "A" or response_a == "a" or response_a == "Skate like the clappers":
        for char in "\nYou run to the wisest most friendly looking dog ever..\nMaybe he will be your savior!!\nYou starting daydreaming about cheese and that lovely mushroom spot\n....\nThe dog barks, waking you up from your head in the clouds\n....\n":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        playsound.playsound('happy_dog.wav', False)
        time.sleep(2)
        print("\n\n")
        print(" --------------------------------------------------------------------------")
        print("|                                                                          |")
        print("|                       .--.             .---.                             |")
        print("|                     /:.  '.         .' ..  '._.---.                      |")
        print("|                   /:::-.  \.-'''-;` .-:::.     .::\                      | ")
        print("|                  /::'|   \/  _ _  \   `\:'   ::::|                       | ")
        print("|              __.'    |   /  (o|o)  \     `'.   ':/                       | ")
        print("|             /    .:. /   |   ___   |        '---'                        | ")
        print("|            |    ::::'   /:  (._.) .:\                                    |")
        print("|            \    .='    |:'        :::|  - Ohh heyyy Squeaks and ".format(name))
        print("|             `""`       \     .-.   ':/                                   | ")
        print("|                        '---`|I|`---'                                     | ")
        print("|                             '-'                                          | ")
        print("|                                                                          |")
        print(" --------------------------------------------------------------------------")
        print("\n")
        time.sleep(3)
        dog_quiz_1()
    elif response_a == "B" or response_a == "b" or response_a == "Run beneath the TV":
        for char in "You are safe for now but there is no sign of the cat\nleaving the room... You wait and wait..\nAND\n...\nwait\n....\n\nYou tummy starts rumbling loudly\n\n....\n":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        playsound.playsound('boo.wav', False)
        time.sleep(2)
        beginning_options()
    else:
        print("I do not recognise that option. Please check your spelling and try again")
        response_ko_a()
#response_ko_a()
# USER IS BEHIND THE TV - THEY NEED TO GET AWAY FROM THE CAT
def option_two():
    playsound.playsound('cat_purr.wav', False)
    for char in "\nYou pop your little head around the side of the Tv\nYou see the lazy plump kitty cat fast asleep snoozing in the sun again.\nThere is no straight escape out the room,\nthe fat cat is lay in front of the doorway\n....\nHMMMMMM...\n....\n'OHHHH..what's that?', you think, as you spot a Tech Deck on the floor..\nMaybe an escape?\nYou know that you are a lot more agile and faster than the cat.\nBut you need to decide if luck is on your side tonight?\n\n":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    response_a = input("Choices choices..Do you smack the cat over its head to KO the cat\nor start practising a pop it - shove it on the Tech Deck?\n[A: Smack the cat over its head to KO the cat]\n[B: Start practising a pop it - shove it]\nAnswer: ")
    if response_a == "A" or response_a == "a" or response_a == "smack the cat over its head to KO the cat":
        print("\n")
        playsound.playsound('attack.wav', False)
        for char in "\nOHHHHH silly mouse!!\nYou may be the prize fighter back in your small mousey world...\nBut your puny rodent arms are not strong enough to KO a Maine Coone!!\nYou start panicking...What do you do NOW?!\n":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        time.sleep(1.5)
        response_ko_a()
    elif response_a == "B" or response_a == "b" or response_a == "start practising a pop it - shove it":
        playsound.playsound('tech_deck.wav', False)
        for char in "\nGO LITTLE MOUSEY, you've got some skills!":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        time.sleep(2)
        for char in "\nOHHHH...Wait\nThis looked like a decent option...\n....\nBut oh dear! This does not end well for you":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        time.sleep(1.5)
        playsound.playsound('cat_shreak.wav', False)
        for char in "\nYou have now woken the cat and he's not happy....\n.......\nUHHHH OH..You have met your brutal demise":
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        time.sleep(1.5)
        playsound.playsound('cat_shreak.wav', False)
        time.sleep(1.5)
        playsound.playsound('squeaks.wav', False)
        time.sleep(1.5)
        playsound.playsound('dead.wav', False)
        print("\n")
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       DEAD!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    else:
        print("Sorry I do not recognise that option. Please check your spelling and try again!")
        option_two()
#OPTION ONE - LINK CODE TO OPTION 2!!
def get_passed_unseen():
    for char in "You slowly.. stealthily... creep past the lady's horrendous bunions.\nThe Stench...... unreal..\nYour tail accidently brushes up on them... EUGHHH!\nShe screams, so now you have to run!\nYou scramble accross the dimly lit landing and head into a child's bedroom.\nIt's dark, except from the light of some UV glowing stars on the ceiling.\nYou can distinguish a glass enclosure ontop of a desk.\nYou can see a gerbil munching on some celery and a tech deck\nnext to the cage ":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    get_passed = input("Press 'T' key to talk to the gerbil:")
    if get_passed == "T" or get_passed == "t":
        for char in "Before you can speak to the Gerbil a dog called\nLenny introduces himself and says you must sit with him to\nwatch Shrek 1 with him and his owner Andy...\nYou hastily agree..":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        playsound.playsound('happy_dog.wav', False)
        dog_escape()
    else: 
        option_two()
def reveal_yourself():
    print("\n")
    playsound.playsound('squeaks.wav', False)
    time.sleep(1.5)
    playsound.playsound('woman_scream.wav', False)
    time.sleep(1.5)
    for char in "You switch on the rodent version of puppy dog eyes and squeak up at the lady.\nSurely she cant resist your charm {}.\nOH NO!!!\nShe HATES mice..\nShe's battered you with her hairbrush.\nR.I.P\n":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    playsound.playsound('splat.wav', False)
    for char in "Farewell my friend..":
        sleep(0.2)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1.5)
    playsound.playsound('squeaks.wav', False)
    time.sleep(1.5)
    playsound.playsound('dead.wav', False)
    print("\n")
    print(" ------------------------------")
    print("|   !!     !           !!      |
    print("|           .  !   .           |")
    print("|       .  /|     /\  ,    !!  |")    
    print("|    !  |\/ |/\__/  \/|___     |")
    print("|     __|                /     |")
    print("|     \       DEAD!      \  !  |")
    print("|!!   /       -----      _\    |")
    print("|    /___  _  _         _\     |")
    print("|       /,' \| \  /\|\ |       |")
    print("|      /'    `  \/  ` \|    !! |")
    print("|  !!          !          !    |")
    print(" ------------------------------")
    print("\n")
    time.sleep(1.5)
    end_game()
def enters_bathroom(): 
    print("\n")
    playsound.playsound('squeaks.wav', False)
    for char in "You take your cheese winnings, and carry on through the hole.\nYou end up in the upstairs bathroom, just in a crevice in the wall by the bath tub.\nThere is a woman removing her makeup in the mirror.\nShe smells of the mezcal, and is swaying slightly.\nBut she looks kind, you wonder that if you squeaked up that she'd help you. ":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n\n")
    playsound.playsound('drunk_woman.wav', False)    
    print(" -------------------------------------------------------- ")
    print("|                     ___                                | ")                    
    print("|                    //)))))        - hicCuPPPP!         |")
    print("|                    )))@_@)                             |")
    print("|                   (((  = )                             |")
    print("|                    ))) -(_   __                        | ")
    print("|                   /   `-'\  /,\ `                      | ")
    print("|                  /__|     )y |                         |   ")
    print("|                  < \     (\_/                          | ")
    print("|                   `.\     \                            |  ")
    print("|                   {>>>`   |                            |  ")
    print("|                  /`-'\____|                            |  ")
    print("|                 /   c  \ /                             |   ")
    print("|                (C \_ _))\                              |   ")
    print("|                 `-'-._/  \                             |   ")
    print("|                    /  /\  \                            |  ")
    print("|                   / ,'  `. \                           |  ")
    print("|                  / /      \ \                          |   ")
    print("|                 <\_\_      \ \                         |  ")
    print("|                  `---`    (_`-\_                       |  ")
    print("|                             `---'                      |")
    print(" --------------------------------------------------------  ")
    print("\n\n")
    ask_for_help_or_run = input ("Do you want to take the risk? [Y/N]\nAnswer: \n")
    if ask_for_help_or_run == "Y" or ask_for_help_or_run == "y" or ask_for_help_or_run == "yes":
        reveal_yourself()
    elif ask_for_help_or_run == "N" or ask_for_help_or_run == "n" or ask_for_help_or_run == "no":
        get_passed_unseen()
#Question 3
def quiz_game3():
    print("\n")
    print(" ---------------
    print("|     ┏━━━┓     |")
    print("|     ┃┏━┓┃     |")
    print("|     ┗┛┏┛┃     | ")
    print("|       ┃┏┛     |")
    print("|       ┏┓      |")
    print("|       ┗┛      |")
    print(" ---------------
    print("\n")
    hole_score = 2
    h_answer_three = input("Which country bored the deepest man made hole in the world?\n[A: Russia]\n[B: Chile]\n[C: Belarus]\nAnswer: \n")
    if h_answer_three == "A" or h_answer_three == "a" or h_answer_three == "Russia" or h_answer_three == "russia":
        hole_score += 1
        playsound.playsound('correct.wav', False)
        print("Correct!")
        print("Score: ", hole_score)
        print("You may continue on your journey through the hole ")
        print("\n")
        enters_bathroom()
    else:
        playsound.playsound('wrong.wav', False)
        print("Incorrect!")
        time.sleep(1.5)
        print("Score: ", hole_score)
        time.sleep(1.5)
        print("You Lose!")
        continue_path()       
#quiz_game3        
#Question 2
def quiz_game2():
    print("\n")
    print(" ---------------
    print("|     ┏━━━┓     |")
    print("|     ┃┏━┓┃     |")
    print("|     ┗┛┏┛┃     | ")
    print("|       ┃┏┛     |")
    print("|       ┏┓      |")
    print("|       ┗┛      |")
    print(" ---------------
    print("\n")
    hole_score = 1
    h_answer_two = input("The Film called Holes' main character is called...\n[A: Stanley Stanley]\n[B: Stanley Yelnats]\n[C: Stan Lee]\nAnswer: \n")
    if h_answer_two == "B" or h_answer_two == "b" or h_answer_two == "Stanley Yalnats" or h_answer_two == "stanley yelnats":
        hole_score += 1
        playsound.playsound('correct.wav', False)
        print("Correct!")
        time.sleep(1.5)
        print("Score: ", hole_score)
        time.sleep(1.5)
        print("\n")
        quiz_game3()
    else:
        print("\n")
        playsound.playsound('wrong.wav', False)
        print("Incorrect!")
        time.sleep(1.5)
        print("Score: ", hole_score)
        time.sleep(1.5)
        print("You Lose!")
        continue_path()
#quiz_game2              
#Question 1
def quiz_game1():
    print("\n")
    print(" ---------------
    print("|     ┏━━━┓     |")
    print("|     ┃┏━┓┃     |")
    print("|     ┗┛┏┛┃     | ")
    print("|       ┃┏┛     |")
    print("|       ┏┓      |")
    print("|       ┗┛      |")
    print(" ---------------
    print("\n")
    hole_score = 0
    h_answer_one = input("In the meal Toad in the hole, what part of the meal is considered the hole\n[A: Yorkshire Pudding]\n[B: Sausage]\n[C:Gravy]\nAnswer: \n")
    if h_answer_one == "a" or h_answer_one == "A" or h_answer_one == "Yorkshire Pudding" or h_answer_one == "yorkshire pudding":
        hole_score += 1
        playsound.playsound('correct.wav', False)
        print("Correct!")
        time.sleep(1.5)
        print("Score: ", hole_score)
        time.sleep(1.5)
        print("\n")
        quiz_game2()
    else:
        playsound.playsound('wrong.wav', False)
        print("Incorrect!")
        time.sleep(1.5)
        print("Score: ", hole_score)
        time.sleep(1.5)
        print("You Lose!")
        print("\n")
        continue_path()
#quiz_game1()
def right_hole():
    print("\n")
    for char in "Your little eyes mistook a grease stain for a hole!\nYou headbutted the wall and KO'd yourself.\nYou lose. ":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n\n")
    print(" --------------------")
    print("|     _   _____      |")
    print("|    | | / / _ \     |   ")
    print("|    | |/ / | | |    |   ")
    print("|    |   <| | | |    |   ")
    print("|    | |\ \ |_| |    |   ")
    print("|    |_| \_\___/     |   ")
    print("|                    |    ")
    print(" --------------------  ")
    print("\n\n")
    playsound.playsound('splat.wav', False)
    time.sleep(1.5)
    playsound.playsound('squeaks.wav', False)
    time.sleep(1.5)
    playsound.playsound('dead.wav', False)
    print("\n")
    print(" ------------------------------")
    print("|   !!     !           !!      |
    print("|           .  !   .           |")
    print("|       .  /|     /\  ,    !!  |")    
    print("|    !  |\/ |/\__/  \/|___     |")
    print("|     __|                /     |")
    print("|     \       DEAD!      \  !  |")
    print("|!!   /       -----      _\    |")
    print("|    /___  _  _         _\     |")
    print("|       /,' \| \  /\|\ |       |")
    print("|      /'    `  \/  ` \|    !! |")
    print("|  !!          !          !    |")
    print(" ------------------------------")
    print("\n")
    time.sleep(1.5)
    end_game()
def left_hole():
    print("\n")
    for char in "Welcome to who wants to be a left hole quiz winner?\nIf you answer correctly, you may carry on up the path\nIf you do not, you await a grave fate. \n":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    listo = input ("Ready? Y/N? ")
    if listo == "Y" or listo == "y" or listo == "yes" or listo == "YES":
        playsound.playsound('gameshow.wav', False)
        time.sleep(1.5)
        print("\n\n")
        for char in "\n\n###############################\n##        HOLE QUIZ        ##\n###############################\n\n":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
        time.sleep(2)
        print("\n\n")
        quiz_game1()
    elif listo == "N" or listo == "n" or listo == "no" or listo == "No":
        print ("SEE YA. ")
        continue_path()   
def feast_path():
    print("\n")
    for char in"'Nothing beats the sugary goodness of a Hob Nob!'You say to yourself\nOH NO!!\nA GIANT DRUNK MALE HUMAN HAS FALLEN ONTOP OF YOU.\nYour stop for a snack has cost you your life.\nYOU LOSE.":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1.5)
    print("\n")
    print(" ------------------------------")
    print("|   !!     !           !!      |
    print("|           .  !   .           |")
    print("|       .  /|     /\  ,    !!  |")    
    print("|    !  |\/ |/\__/  \/|___     |")
    print("|     __|                /     |")
    print("|     \       SPLAT!      \  !  |")
    print("|!!   /       -----      _\    |")
    print("|    /___  _  _         _\     |")
    print("|       /,' \| \  /\|\ |       |")
    print("|      /'    `  \/  ` \|    !! |")
    print("|  !!          !          !    |")
    print(" ------------------------------")
    print("\n")
    end_game()
    playsound.playsound('splat.wav', False)
    time.sleep(0.5)
    playsound.playsound('squeaks.wav', False)
    time.sleep(1.5)
    playsound.playsound('dead.wav', False)
    print("\n")
    print(" ------------------------------")
    print("|   !!     !           !!      |
    print("|           .  !   .           |")
    print("|       .  /|     /\  ,    !!  |")    
    print("|    !  |\/ |/\__/  \/|___     |")
    print("|     __|                /     |")
    print("|     \       DEAD!      \  !  |")
    print("|!!   /       -----      _\    |")
    print("|    /___  _  _         _\     |")
    print("|       /,' \| \  /\|\ |       |")
    print("|      /'    `  \/  ` \|    !! |")
    print("|  !!          !          !    |")
    print(" ------------------------------")
    print("\n")
    time.sleep(1.5)
    end_game()
def continue_path():
    print("\n\n")
    print(" --------------------------------------------------------------------------")
    print("|                                                                          |")
    print("|                                      _.,_                                |")
    print("|        mummMmbliiinggg -          ,-'.' .`-,                             |")
    print("|            BURP!                 ;; '. ' `. ;` - _                       |")
    print("|                               _,-; ' ; `.  ,% .-,  -                     | ")
    print("|                        ,_.,-'`   ';; ; : ;%'  | |   \                    | ")
    print("|            ___  _._,-`'\            `'-`'  _.,' `.   )                   | ")
    print("|      __,--`-,,`'  ,._,.-`-., _.,-.--.-,`''`  |  _|   |___________        | ")
    print("|       `---'////\ /  .-,     `-`-^--`'^`-...,,| | |.,/                    |")
    print("|            //\)(/   `-\.-.                   | `-'                       |")
    print("|                       ( .-;                  |   |    ,.                 | ")
    print("|                        `-~ ~~-.              `._.'  ,/ /                 |")
    print("|                          `~ ~~~ ~~                 /,.`)                 |")
    print("|                                                   //  /                  |")
    print("|                                                  /_ `/                   |")
    print("|                                                 (  `/                    |")
    print("|                                                  `-'                     | ")
    print("|                                                                          |")
    print(" --------------------------------------------------------------------------")
    print("\n\n")
    playsound.playsound('hiccups.wav', False)
    time.sleep(1.5)
    for char in "With the glycogen stores in your muscles depleted, you're safe behind a pair of crocs.\nSuddenly, a male human stumbles into the hall, he stinks of alcohol.\nHe has a bottle of Razvan's favourite Mezcal in his hand.\nIn a split second he collapses right ontop of the precious hob nob crumbs!\nThankfully, you didn't stop for a snack.\nYou see two holes in the wall, one to the right and one to your left...\nWhich way do you want to go?\n[Left]/[Right]\Answer: ":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n\n\n")
    print(" --------------------------")
    print("|                           |")
    print("|           _____           | ")
    print("|          `.___,'          | ")
    print("|           (___)           |")
    print("|           <   >           |")
    print("|            ) (            |")
    print("|           /`-.\           |")
    print("|          /     \          | ")
    print("|         / _    _\         | ")
    print("|        :,' `-.' `:        | ")
    print("|        | RAZVANS |        | ")
    print("|        :  mezcal ;        |")
    print("|         \ ----- /         |")
    print("|          `.___.'          | ")
    print("|                           |         ")
    print("|                           |")
    print(" --------------------------")
    print("\n\n\n")
    playsound.playsound('squeaks.wav', False)
    left_hole_right_hole = input ("Which way? ")
    if left_hole_right_hole == "Left" or left_hole_right_hole == "left" or left_hole_right_hole == "l":
        print("\n")
        left_hole()
    elif left_hole_right_hole == "Right" or left_hole_right_hole == "right" or left_hole_right_hole == "r":
        print("\n")
        right_hole()
    else:
        for char in "It's left or right, there is no up or down\nOr backwards to run to Pret for a coffee Mousey\nTry again! ":
            sleep(0.15)
            sys.stdout.write(char)
            sys.stdout.flush()
    continue_path()
def scurry_for_life():
    print("\n")
    for char in "Well done! You made it out of the room unscathed.\nBut you just ran like you've never ran before.\nYour mousey legs are knackered and you're SO hungry.\nYou notice some delicious hob nob crumbs on the floor.\nWill you continue running across the hall just in case?\nOr will you stay and feast?\n[Continue]\n[Feast]\n":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    continue_or_feast = input("What will you do?")
    if continue_or_feast == "Continue" or continue_or_feast == "continue" or continue_or_feast == "c":
        continue_path()
    else:
        continue_or_feast == "Feast" or continue_or_feast == "feast" or continue_or_feast == "f"
        feast_path()
# BEGINNING THREE ROUTE OPTIONS 
def beginning_options():
    playsound.playsound('squeaks.wav', False)
    time.sleep(1.5)
    print("\n\n")
    print(" ------------------------------------")
    print("|                                     |")
    print("|                                     |")
    print("|         _______________             |")
    print("|        |,----------.  |\            |")
    print("|        ||           |=| |           |")
    print("|        ||    TV    || | |           |")
    print("|        ||       . _o| | | __        |")
    print("|        |`-----------' |/ /~/        |")
    print("|         ~~~~~~~~~~~~~~~ / /         |")   
    print("|                                     |")
    print("|                                     |")
    print(" ------------------------------------")
    print("\n\n")
    time.sleep(1.5)
    for char in "'It looks like we are trapped behind what I think is a TV..\nWhatever are we going to do!!?\nWe've got to find some way out!!'":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1.5)
    print("\n")
    for char in "\n'Im so glad you're helping me, but what should we do?'\n[1: Scurry for your life away from the cat, but who knows if you'll make]\n[2: Collect the Tech Deck and silently creep up to the sleeping cat]\n[3: Climb the curtains for a better vantage point]\nAnswer: \n":
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    route_option = input()
    if route_option == "1" or route_option == "one" or route_option == "One" or route_option == "ONE":
        print("\n")
        scurry_for_life()
    elif route_option == "2" or route_option == "two" or route_option == "Two" or route_option == "TWO":
        option_two()
    elif route_option == "3" or route_option == "three" or route_option == "Three" or route_option == "THREE":
        go_option3()
    else:
        print("\n")
        print("'OOOPS! That's not an option, please try again!'")
        beginning_options()
# CHARACTER SELECTION FOR THE USER 
def characters():
    character_options = ("\n'Oh thank you so much {}, I can tell we're going to be good friends!\nI've gotta say though.. You are kinda funny looking\nI cant quite tell, what sort of animal you are?'\n[Unicorn]\n[Monkey]\n[Frog]\n[Octopus]\n[Scorpion]\n".format(name))
    for char in character_options:
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    character_select = input("Answer: ")
    if character_select == "unicorn" or character_select == "Unicorn" or character_select == "UNICORN":
        print(emoji.emojize("\n'Yay! Of course, thank you {} my :unicorn_face: friend!'".format(name), use_aliases=True))
    elif character_select == "monkey" or character_select == "Monkey" or character_select == "MONKEY":
        print(emoji.emojize("\n'Yay! Of course, thank you {} my :monkey_face: friend!' ".format(name), use_aliases=True))
    elif character_select == "frog" or character_select == "Frog" or character_select == "FROG":
        print(emoji.emojize("\nYay! Of course, thank you {} my :frog: friend!' ".format(name), use_aliases=True))
    elif character_select == "octopus" or character_select == "Octopus" or character_select == "OCTOPUS":
        print(emoji.emojize("\n'Yay! Of course, thank you {} my :octopus: friend!' ".format(name), use_aliases=True))
    elif character_select == "scorpion" or character_select == "Scorpion" or character_select == "SCORPION":
        print(emoji.emojize("\n'Yay! Of course, thank you {} my :scorpion: friend!' ".format(name), use_aliases=True))
    else:
        print("'Sorry that's not a valid animal,\nI think you made it up... please choose again! '")
        print("\n")
        characters()
    beginning_options()
# GAME STARTS
def start_game():
    time.sleep(3)
    playsound.playsound('squeaks.wav', False)
    welcome = "\n'Oh hello, oh wow! Maybe you can help me?! \nWhat is your name?'\nAnswer: \n"
    for char in welcome:
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    global name
    name = input()
    time.sleep(0.15)
    squeaks_intro = "'Nice to meet you {}.\nIm Squeaks, the mouse.' ".format(name)
    for char in squeaks_intro:
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print("\n")
    print("\n")
    print(" --------------------------------------")
    print("|                                       |")
    print("|              /\                       |")
    print("|          )  ( ')                      |")
    print("|         (  /  )                       |")
    print("|          \(__)|     - hi!             |")
    print("|                                       |")
    print(" --------------------------------------")
    print("\n")
    sticky_situation = "\n'Im in a sticky situation!! \nThis mean old cat has dragged me by the tail inside this big scary house!! \nIm so far away from my home under the biggest tree!!\nI dont know what to do!! \nWill you help me {}?'\n[Y]/[N]\nAnswer: \n".format(name)
    for char in sticky_situation:
        sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1.5)
    start = input()
    if start == "Y" or start == "y" or start == "yes" or start == "Yes" or start == "YES":
        characters()
    elif start == "N" or start == "n" or start == "No" or start == "no" or start == "NO":
        playsound.playsound('cat_shreak.wav', False)
        playsound.playsound('squeaks.wav', False)
        print("\n")
        playsound.playsound('boo.wav', False)
        print(" ------------------------------")
        print("|   !!     !           !!      |
        print("|           .  !   .           |")
        print("|       .  /|     /\  ,    !!  |")    
        print("|    !  |\/ |/\__/  \/|___     |")
        print("|     __|                /     |")
        print("|     \       BOOO!      \  !  |")
        print("|!!   /       -----      _\    |")
        print("|    /___  _  _         _\     |")
        print("|       /,' \| \  /\|\ |       |")
        print("|      /'    `  \/  ` \|    !! |")
        print("|  !!          !          !    |")
        print(" ------------------------------")
        print("\n")
        time.sleep(1.5)
        end_game()
    else:
        intro_error = print("'Sorry I dont understand, are you speaking to me in cat?! Eeek! Please try again!'")
# GAME INTRODUCTION SETTING THE SCENE 
def intro():
    custom_fig = Figlet(font='ogre')
    greeting = Figlet(font='small')
    print("")
    # print ("------------------------------------------------------------------------------------")
    # skip_intro = input("Would you like to skip the introduction? [Y]/[N]: ")
    # if skip_intro == "y" or skip_intro == "Y":
    #     print ("------------------------------------------------------------------------------------")
    #     start_game()
    # elif skip_intro == "n" or skip_intro == "N":
    #     print ("------------------------------------------------------------------------------------")
    #     intro()
    # else:
    #     intro()
    playsound.playsound('pitterpatter.wav', False)
    print ("------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------")
    time.sleep(1.5)
    print(custom_fig.renderText("Look at what the cat dragged in!"))
    time.sleep(1.5)
    print("\n")
    print("                                           )\._.,--....,'``.      ")
    print("      .b--.                               /;   _.. \   _\  (`._ ,.")
    print("     `=,-,-'~~~                          `----(,_..'--(,_..'`-.;.'")
    time.sleep(1.5)
    print("------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------")
    time.sleep(3)
    print("[Game built by Chloë, Idonnya, Jalexia, Linda, Matz - 2020]")
    print("------------------------------------------------------------------------------------")
    print("------------------------------------------------------------------------------------")
    time.sleep(3)
    print("\n\n\n")
    print(greeting.renderText("Welcome to the game!"))
    time.sleep(1.5)
    print("")
    print("")
    print("")
    print("")
    print("      ;   :   ; ")
    print("   .   \_,!,_/   , ")
    print("    `.,'     `.,' ")
    print("     /         \ ")
    print("~ -- :         : -- ~ ")
    print("     \         / ")
    print("    ,'`._   _.'`. ")
    print("   '   / `!` \   ` ")
    print("      ;   :   ;  ")
    print("")
    print("")
    time.sleep(1.5)
    for char in "It's a beautiful day on the farm.\nThe sun is shining high in the sky.\nBirds are tweeting as they sit together in the treetops.\nThe wind blows ruffling up some fallen leaves.\nEveryone is busying themselves and there's a sense of urgency in the air.\n\nLay in a perfect sunny spot on the porch theres a plump cat basking,\nlightly snoozing away in the heat.\n\nNear a big tree sits a little mouse cosily under a mushroom top\nnibbling gently on some cheese crumbs found on the steps of \nthe near by house.\n\nHe nibbles and he nibbles until all the cheese is gone,\nand thinks to himself 'Oh how I wish I had more cheese!'\n\nThe mouse hops and jumps ever so quietly over to the steps\nnext to where the plump kitty is sleeping with some crumbs\nright next to his back paw\n\n....\n\nThe mouse gets closer and closer\n\n....\n\nBeing so careful not to make any loud sounds\n\nOH NO!!!\n\nThe cat stirs\n\n....\n\nThe wind has changed and he caught a big wiff\n\n....\n\nHe's now sat staring down at the mouse\nIt's big paw swipes\n\n....":
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)
    print("\n\n")
    print(" ----------------------------------------------")
    print("|                                               | ")
    print("|               xXXXX   xXXX                    |")
    print("|              XXXXXXX XXXXXX                   |")
    print("|              'XXXXXX XXXXXX                   |")
    print("|                XXXXX  XXXXX xXx               |")
    print("|            XXXx XXXXX  XX' XXXX               |")
    print("|            XXXXx 'XX'  '  XXXXXX              |")
    print("|            XXXXX   xXx  XXXXX'                | ")
    print("|              '''  xXXXXXx 'XX'                |")
    print("|                  XXXXXXXXXX                   |")
    print("|                xXXXXXXXXXXXXXx                |")
    print("|                XXXXXXXXXXXXXXX                | ")
    print("|                ''''  '''''''                  |")             
    print("|                                               | ")
    print(" ----------------------------------------------")
    print("\n")
    for char in "\n\n....\n\nEverything goes dark\n\n":
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    playsound.playsound('cat_shreak.wav', False)
    print("___________________________________")
    print("\n\n")
    start_game()
intro()
