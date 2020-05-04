#- - - - - - - - - - - - - - - - - - - - -|
#  Shaniah Blanchard                      |
#  12/1/2014                              |
#  Assignment 10                          |
#- - - - - - - - - - - - - - - - - - - - -|
#  This is a text-based adventure game.   |
#  Please review the possible answers     |
#  to the yes or no questions below.      |
#  THIS IS NOT COMPLETE UNFORTUNATELY.    |
#- - - - - - - - - - - - - - - - - - - - -|

#- - - - - - - - - - - - - - - - - - - - -|
#  POSITIVE ANSWERS                       |
#  yes, ok, fine, alright, sure           |
#  Yes, Ok, Fine, Alright, Sure           |
#  YES, OK, FINE, ALRIGHT, SURE           |
#- - - - - - - - - - - - - - - - - - - - -|
#  NEGATIVE ANSWERS                       |
#  no, never, nah, nope, negatory         |
#  No, Never, Nah, Nope, Negatory         |
#  NO, NEVER, NAH, NOPE, NEGATORY         |
#- - - - - - - - - - - - - - - - - - - - -|

# IMPORTS #

import time
import random

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

# MAIN GAME FUNCTIONS #

def pace(string):
    if (P == "slow"):
        for char in string:
            print(char, end='')
            time.sleep(.1)
        print(" ")
    elif (P == "fast"):
        for char in string:
            print(char, end='')
            time.sleep(.035)
        print(" ")
    elif (P == "extra fast"):
        for char in string:
            print(char, end='')
            time.sleep(.01)
        print(" ")
        

def dot():
    for dot in range(3):
        print(".")
        

def other():
    print(" ")
    print("ERROR: I literally gave you a list of options and you chose to type THAT.")
    print("Try again, " + name + ".")
    print(" ")
    

def GAME_OVER(ending):
    print(" ")
    print("GAME OVER.")
    print("Ending: " + ending)
    G_O = 1
        
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

# PART 1 - INTRODUCTION #

POSITIVE = ["yes", "Yes", "YES", "ok", "Ok", "OK", "Fine", "fine", "FINE", "alright", "Alright", "ALRIGHT", "sure", "Sure", "SURE"]
NEGATIVE = ["no", "No", "NO", "Never", "never", "NEVER", "Nah", "nah", "NAH", "nope", "Nope", "NOPE", "negatory", "Negatory", "NEGATORY"]
        
print(" ")      
print("|- - - - - - - - - - - - - - - - - - - - - - -|")
print("|   ✕ ✄ ☠ ❁ A GROUP OF CROWS ❁ ☠ ✄ ✕    |")
print("|                -  Shane  -                  |")
print("|- - - - - - - - - - - - - - - - - - - - - - -|")
print(" ")

P = "slow"
pace("Would you like your text slow?")

P = "fast"
pace("Or would you like your text fast?")

flag = True

while(flag):
    try:
        a = str(input(" "))
        if (a == "slow"):
            P = "slow"
            flag = False
        elif (a == "fast"):
            P = "fast"
            flag = False
        elif (a == "extra fast"):
            P = "extra fast"
            flag = False
        else:
            print(" ")
            print("ERROR: You. have. no. brain.")
            print("Try again.")
            print(" ")
    except ValueError:
        print(" ")
        print("ERROR: You. have. no. brain.")
        print("Try again.")
        print(" ")
        
    
flag = True

G_O = False

if(G_O == False):
    print(" ")
    pace("**WARNING: You may want to make this fullscreen so the text doesn't just run off the page and look awkward like this. Must be ages 5+ to play.**")
    print(" ")
    name = str(input("Please enter your name > "))
    while(flag):
        try:
            age = int(input("Please enter your age > "))
            if (age > 4) and (age < 100):
                flag = False
            elif (age > 0) and (age < 5):
                print(" ")
                pace("YEAH RIGHT, LITTLE BABY.")
                print(" ")
            else:
                print(" ")
                print("ERROR: What kind of age is that? Do you think I am dumb, peasant?")
                print(" ")
        except ValueError:
            print(" ")
            print("ERROR: What kind of age is that? Do you think I am dumb, peasant?")
            print(" ")
    print(" ")
    print("Alright, " + name + ".")
    pace("Before we begin, do you have any questions?(yes or no)")
    ask = input(" ")
    print(" ")

    flag = True

    while(flag):
        if ask in POSITIVE:
            print("Enter 0 to exit.")
            print("Enter 1 for the list of okay answers to questions.")
            print("Enter 2 for 'Why am I here?'")
            print("Enter 3 for 'How do I win the game?'")
            print("Enter 4 for other question.")
            print("Enter hidden code to view game endings.")
            pace("Ask away.")
            question = input(" ")
            print(" ")
            if (question == "1"):
                print("""
                |- - - - - - - - - - - - - - - - - - - - -|
                |  POSITIVE ANSWERS                       |
                |  yes, ok, fine, alright, sure           |
                |  Yes, Ok, Fine, Alright, Sure           |
                |  YES, OK, FINE, ALRIGHT, SURE           |
                |- - - - - - - - - - - - - - - - - - - - -|
                |  NEGATIVE ANSWERS                       |
                |  no, never, nah, nope, negatory         |
                |  No, Never, Nah, Nope, Negatory         |
                |  NO, NEVER, NAH, NOPE, NEGATORY         |
                |- - - - - - - - - - - - - - - - - - - - -|""")
                print(" ")
            elif (question == "2"):
                pace("Probably because you are grading this assignment.")
                print(" ")
            elif (question == "3"):
                pace("Wow you think I would just tell you that?")
                pace("Find out for yourself.")
                pace("Just make the right choices.")
                print(" ")
            elif (question == "hidden code"):
                pace("Nice try, nerd.")
                print(" ")
            elif (question == "0"):
                flag = False
            elif (question == "4"):
                eight_ball = 0
                print("Enter 0 to go back.")
                print("(This works like a magic 8-ball.)")
                while (eight_ball is not "0"):
                    pace("What would you like to ask me?")
                    eight_ball = input(" ")
                    yay_nay = random.randint(1, 4)
                    if (eight_ball is not "0"):
                        if (yay_nay == 1):
                            print("Yes")
                        elif (yay_nay == 2):
                            print("No")
                        elif (yay_nay == 3):
                            print("Maybe")
                        else:
                            print("Try asking again.")
                        print(" ")
                            
            else:
                print("ERROR: How did you mess that up, " + name + ", there are only 5 options.")
                print("I suppose I can grant you a do-over.")
                print(" ")
        elif ask in NEGATIVE:
            pace("Your loss.")
            flag = False
            print(" ")
        else:
            pace("ERROR: Get with the program.")
            print(" ")
            pace("Before we begin, do you have any questions?")
            ask = input(" ")
            print(" ")

    flag = True

    pace("Then let us begin.")
    dot()
    pace("You sit alone in a room.")
    pace("But not just any room.")
    pace("It's a significant room for you humans.")
    pace("It's your bedroom.")
    pace("The walls are that familiar color.")
    pace("Perhaps you chose the color, perhaps you didn't.")
    pace("But such pleasantries are not important right now.")
    pace("You have been invited to one of those nonsensical social human 'get-togethers' by your best mate.")

    while(flag):
        print("Accept the invite? ")
        choice1 = input(" ")
        print(" ")
        if choice1 in NEGATIVE:
            while(flag):
                pace("Wow.")
                pace("You really want to flake out?")
                flake = input(" ")
                if flake in POSITIVE:
                    while(flag):
                        pace("Seriously? Just go to the dumb social event, ok?")
                        a = input(" ")
                        if a in POSITIVE:
                            pace("That's a good human.")
                            flag = False
                        elif a in NEGATIVE:
                            while(flag):
                                pace("Listen, you have to go or the game will end.")
                                b = input(" ")
                                if b in NEGATIVE:
                                    GAME_OVER("You Knew What You Were Doing.")
                                    flag = False
                                    G_O = True
                                elif b in POSITIVE:
                                    pace("That's a good human.")
                                    flag = False
                                else:
                                    other()
                        else:
                            other()
                elif flake in NEGATIVE:
                     pace("That's a good human.")
                     flag = False
                else:
                    other()
        elif choice1 in POSITIVE:
            pace("Good, you didn't make that too painful.")
            flag = False
        else:
                other()
                
flag = True

if(G_O == False):
    pace("Now that you have made your decision to go you cannot change it.")
    pace("So you accept your fate,")
    pace("and go slip on your favorite human feet coverings, making your way out the front threshold.")
    pace("Luckily the address of the party's location is only 1 street-length away from where you live.")
    pace("Although it is a little rainy now, you don't think you need a jacket.")
    while(flag):
        pace("Go back inside to grab a jacket?")
        a = input(" ")
        if a in POSITIVE:
            pace("Are you kidding? You just said you don't think you need a jacket.")
            while(flag):
                pace("Go back for the jacket anyways?")
                b = input(" ")
                if b in POSITIVE:
                    while(flag):
                        pace("Just try the door, I dare you.")
                        c = input(" ")
                        if c in POSITIVE:
                            pace("You twist at the door handle but it is jarred.")
                            pace("Now you feel INCREDIBLY STUPID for not just continuing on with the story.")
                            while(flag):
                                pace("Try the handle again?")
                                d = input(" ")
                                if d in POSITIVE:
                                    pace("Nope, it is still locked, poopbrain.")
                                    pace("Onward.")
                                    flag = False
                                elif d in NEGATIVE:
                                    pace("Thank blinking science!")
                                    flag = False
                                else:
                                    other()
                        elif c in NEGATIVE:
                            pace("Thank Science!")
                            pace("The door was locked anyways.")
                            flag = False
                        else:
                            other()
                elif b in NEGATIVE:
                    pace("Thank Science!")
                    pace("The door was locked anyways.")
                    flag = False
                else:
                    other()
        elif (a in NEGATIVE):
            pace("Thank Science!")
            pace("The door was locked anyways.")
            flag = False
        else:
            other()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

# PART 2 - THE MAN #

    flag = True
    print(" ")
    pace("Peering down the dimly lit road, the streetlamps emit the only light.")
    pace("Other than, of course, the big rock in the sky that hovers around your pathetic life-sphere.")
    pace("You stare up at it's cratered surface.")
    print(" ")
    pace("When you look back up at the street, there is a man standing 5 feet away from you.")
    while(flag):     
        print("1- Greet the man.")
        print("2- Mug him.")
        print("3- Keep walking.")
        a = input(" ")
        if (a == "1") and (age < 13):
            pace("You are literally " + str(age) + ".")
            pace("Didn't your mother teach you not to talk to strangers?")
            while(flag):
                pace("Disregard, Mother. Talk to the man.")
                b = input(" ")
                if b in POSITIVE:
                    pace("You poke the man in the arm.")
                    pace("Man: What the heck, kid.")
                    input("You: ")
                    pace("Man: Didn't your mother teach you not to talk to strangers? Sheesh.")
                    print(" ")
                    pace("The man walks away.")
                    pace("You are so lucky you didn't get MURDERED.")
                    flag = False
                elif b in NEGATIVE:
                    pace("You keep walking.")
                    pace("Good thing, too.")
                    pace("He might have MURDERED you.")
                    flag = False
                else:
                    other()
        elif (a == "1") and (age > 12):
            pace("You speak to the man.")
            pace("Man: Good Evening.")
            input("You: ")
            pace("Man: I've got... Somewhere to be.")
            print(" ")
            pace("That was highly suspicious.")
            pace("Maybe you should be more careful of who you talk to.")
            pace("There could be a MURDERER out there.")
            flag = False
        elif (a == "2") and (age < 13):
            pace("You're like " + str(age) + ".")
            while(flag):
                pace("You think you can mug this guy?")
                b = input(" ")
                if b in POSITIVE:
                    pace("You attempt to mug the man.")
                    pace("Man: Hahaha you are just a child, did you think you could really do that.")
                    flag = False
                    G_O = True
                    GAME_OVER("Mugging People Is Wrong.")
                elif b in NEGATIVE:
                    pace("That's right, human child, make good choices.")
                    pace("He could've MURDERED you for mugging him.")
                    flag = False
                else:
                    other()
        elif (a == "2") and (age > 12):
            while(flag):
                pace("Do you really wanna mug someone?")
                pace("You could get MURDERED.")
                b = input(" ")
                if b in POSITIVE:
                    pace("You succeed in mugging the man without struggle.")
                    flag = False
                    G_O = True
                    GAME_OVER("Mugging People Is Wrong.")
                elif b in NEGATIVE:
                    pace("That's right, human, make good choices.")
                    flag = False
                else:
                    other()
        elif (a == "3"):
            pace("Good, human.")
            pace("The passive option is always the best.")
            pace("No need for conflict.")
            pace("He could have MURDERED you.")
            flag = False
        else:
            other()

    flag = True
    
if(G_O == False):        
    print(" ")
    pace("Well, even if he was a MURDERER.")
    pace("He didn't want you.")
    pace("Hopefully he doesn't change his mind.")
    dot()
    pace("Luckily for you, you have made it to the front walkway of the address your human best friend gave you.")
    pace("Without skipping a beat you take your steps up to the very welcoming front door.")
    knock = 1
    ding = 1
    while(flag):
        print("1- Knock on the door.")
        print("2- Ring the doorbell.")
        print("3- Just go in.")
        a = input(" ")
        if (a == "1") and (age < 13):
            pace("You really think your little " + str(age) + "-year-old knuckles can combat such a mighty door?")
            print(" ")
        elif (a == "1") and (age > 12) and (knock < 3):
            pace("You give it a good knock.")
            pace("But no one comes to the door.")
            print(" ")
            knock = knock + 1
        elif (a == "2") and (ding < 3):
            pace("You click the button but you don't hear the ding-dong.")
            pace("You are not sure if you pressed it hard enough.")
            pace("But you don't want to try it again.")
            print(" ")
            ding = ding + 1
        elif (a == "3"):
            pace("That is incredibly rude in human culture.")
            pace("I can't believe you even think that is acceptable.")
            flag = False
        elif (knock >= 3) and (a == "1"):
            pace("You give it a good knock.")
            pace("But NO ONE COMES to the door.")
            print(" ")
        elif (ding >= 3) and (a == "2"):
            pace("You click the button but you don't hear the ding-dong.")
            pace("You are not sure if you pressed it hard enough.")
            pace("But you DON'T WANT TO TRY IT AGAIN")
            print(" ")
        else:
            other()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#

# PART 3 - JEREMY #

    flag = True

    pace("You just invite yourself in anyway instead of waiting patiently at the door.")
    pace("As you step on to the wooden surface of their foyer floor, the faint sound of background music begins to play.")
    while(flag):
        pace("Should you say something to alert them of your presence?")
        a = input(" ")
        if a in POSITIVE:
            pace("What would you like to say?")
            input("You: ")
            dot()
            pace("Jeremy: " + name + "?")
            pace("Jeremy: Is that you?")
            print(" ")
            pace("Jeremy enters the foyer from the hallway in front of you.")
            pace("He is wearing his signature sweater vest.")
            if (age < 13):
                print(" ")
                pace("Jeremy: Oh thank Science! Your parents have been worried sick.")
                pace("Jeremy: They called everyone on the block.")
                pace("Jeremy: Why would you leave home without permision?")
                pace("Jeremy: Your parents are gonna MURDER you.")
                flag = False
                G_O = True
                GAME_OVER("Don't Disobey Your Parents.")
            elif (age > 12):
                print(" ")
                pace("Jeremy: Glad you could make it.")
                input("You: ")
                pace("Jeremy: That's interesting and all but the others are all upstairs if you want to join them.")
                print(" ")
            while(flag):
                pace("Join them?")
                b = input(" ")
                if b in POSITIVE:
                    pace("You head down the hallway Jeremy came from and take a right up the stairs.")
                    flag = False
                elif b in NEGATIVE:
                    pace("You choose to stay with your human friend, who you follow down the hallway into to the kitchen.")
                    print(" ")
                    pace("Jeremy: Oh, " + name + " you're still here?")
                    pace("Jeremy: I was just choppin' up some fresh cucumbers for the salad.")
                    pace("Jeremy: I guess you can help me out.")
                    input("You: ")
                    pace("Jeremy: Look, " + name + " I know you really don't wanna sit around and chop vegetables so why don't you head on up.")
                    print(" ")
                    pace("Jeremy ushers you to the stairs.")
                    flag = False
                else:
                    other()
        elif a in NEGATIVE:
            pace("Okay, weirdo.")
            pace("Just creep through other human's life-cubes for all I care.")
            flag = False
            G_O = True
            GAME_OVER("Use Your Manners.")
        else:
            other()

flag = True
special_flag = True
    
if (G_O == False):
    print(" ")
    pace("Jeremy sure is acting kind of weird. Why didn't he want you to stay down there?")
    dot()
    o1 = "1- Go back to Jeremy."
    o2 = "2- The room on the right."
    o3 = "3- The room straight ahead."
    #o4 = "4- The room to the left."
    while(special_flag):
        pace("Up the stairs there are two rooms. Which one would you like to enter?")
        print(o1)
        print(o2)
        print(o3)
        #print(o4)
        a = input(" ")                
        if (a == "1") and (o1 is not " "):
            while(flag):
                pace("Do you really wanna go back down and bother the Jeremy human?")
                b = input(" ")
                if b in POSITIVE:
                    pace("You make your way down the stairs and into the kitchen.")
                    pace("Jeremy is busy chopping cucumbers and does not seem to notice you.")
                    while(flag):
                        pace("Stay here?")
                        c = input(" ")
                        if c in POSITIVE:
                            pace("Jeremy is still chopping cucumbers and still does not seem to notice you.")
                        elif c in NEGATIVE:
                            pace("Good, Jeremy is kind of boring.")
                            pace("You turn around and go up the stairs, AGAIN.")
                            o1 = " "
                            flag = False
                        else:
                            other()
                elif b in NEGATIVE:
                    pace("He doesn't want to talk right now anyways.")
                else:
                    other()
        if (a == "2") and (o2 is not " "):
            pace("You enter the room on the right.")
            pace("The first thing you notice as you enter is the large game-table coated with green velvet at the center.")
            pace("There are poles with little soccer humans that spin and flip around with ease.")
            pace("You believe it is called foosball.")
            pace("Two players stand on each side, one with short dark hair, the other with long blonde.")
            flag = True
            while(flag):
                pace("Speak to them?")
                b = input(" ")
                if b in POSITIVE:
                    print(" ")
                    input("You: ")
                    pace("Eileen: Oh! Look Gregg, it's Jeremy's friend!")
                    pace("Eileen: Could you remind me of your name again?")
                    name2 = input("You: ")
                    pace("Gregg: Nice to meet you, " + name2 + ". The name's Gregg.")
                    pace("Eileen: " + name2 + "? What a nice name! I'm Eileen.")
                    pace("Jeremy: Hey " + name + "! I just realized I forgot to ask if you wanted anything to drink?")
                    pace("Jeremy: I am such a bad host.")
                    if (name != name2):
                        pace("Eileen: " + name + " said their name was " + name2 + "! What a joker!")
                        pace("Jeremy: Haha " + name + ", you loser.")
                        print(" ")
                    pace("Jeremy: What can I get for all you guys? Soda, juice, beer?")
                    pace("Gregg: I'll take a beer.")
                    pace("Eileen: Could I have just have a soda?")
                    print(" ")
                    while(flag):
                        print("1- Soda")
                        print("2- Juice")
                        print("3- Beer")
                        c = input(" ")
                        if (age < 21) and (c == "3"):
                            pace("You are only " + str(age) + "!")
                            pace("That's illegal!")
                            G_O = True
                            flag = False
                            special_flag = False
                            GAME_OVER("Drinking Age Is 21 In America.")
                        elif (c == "3") or (c == "1") or (c == "2"):
                            pace("Jeremy: No problem, buddy.")
                            pace("Jeremy: I'll be right back.")
                            o2 = " "
                            flag = False
                        else:
                            other()
                elif b in NEGATIVE:
                    pace("Don't be such an introvert.")
                    pace("You need to meet all the characters, human.")
                    print(" ")
                else:
                    other()
        elif (a == "3") and (o3 is not " "):
            pace("You enter the room straight ahead.")
            pace("It's a bathroom.")
            pace("You should've known that, seeing as you can peer right into it.")
            pace("This room is boring.")
            o3 = " "
        #elif (a == "4") and (o4 is not " "):
            #("You enter the room on the left.")
            #("Inside there is someone asleep on a small couch.")
            #("The TV flickers as the scenes change.")
            #flag = True
            #while(flag):
                #("Wake up the girl?")
                #b = input(" ")
                #if b in POSITIVE:
                    #pace("Bonnie: Dude, what the heck.")
                    #pace("Bonnie: I was trying to sleep.")
                    #pace("Bonnie: What do you want?")
                    #input("You: :")
                    #pace("Bonnie: ZZzzzZzzzZzzzzzzz.")
                    #dot()
                    #pace("She fell asleep.")
                    #flag = False
                    #o4 = " "
                #elif b in NEGATIVE:
                    #pace("Bonnie remains asleep on the couch.")
                    #flag = False
                    #o4 = " "
                #else:
                    #other()
        elif (o1 == " ") and (o2 == " ") and (o3 == " "):
            special_flag = False
            pace("Well now you've exhausted all of your options.")
        else:
            other()

if (G_O == False):
    pace("And Jeremy still hasn't brought you that drink yet.")
    pace("Maybe it's a good idea to go check on him.")
    pace("And we have also reached the stopping point, for now.")
    dot()
    pace("To be continued...")
    G_O = True
