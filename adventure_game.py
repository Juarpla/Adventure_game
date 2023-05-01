"""
Student: Juan Plasencia
*I showed my game to two of my friends and they liked it a lot, and even thought that the computer itself thought of the answers.
*A scenario correctly uses more than two choices in line 85
*Showing Creativity:
-Introduction added
-Endings added to each story 
-Establishing ramdom words to increase the chances
"""
#Establish ramdom words to increase the chances
import random
a_m = random.randint(0, 4)
nouns_match = ["a large grizzly bear 🐻", "a long snake 🐍", "a wild wolf 🐺", "a wild moose 🦌", "a crazed gorilla 🦧"]
a_r = random.randint(0, 2)
nouns_run = ["a forbidden tribe 🌄", "an ancient native civilizatione 🌅", "a lost city 🏰"]
a_h = random.randint(0, 2)
nouns_hide = ["an alien 👽", "a robot 👾", "a UFO 🌌"]
a_f = random.randint(0, 2)
nouns_flashlight = ["the pathway lit up in front of you 🌇", "the road in front of you 🚍", "the train rails in front of you 🚉"]
a_w = random.randint(0, 2)
nouns_follow = ["traveled back in time", "traveled to another dimension", "traveled to another universe"]
a_l = random.randint(0, 2)
nouns_look = ["a government spaceship 🌠", "an alien spacecraft 🚀", "a time travel ship 🗼"]
a_d = random.randint(0, 2)
nouns_radio = ["a genie comes out of it 👻", "a ghost comes out 👻", "an accursed spirit comes out 👻"]
a_m = random.randint(0, 2)
nouns_map = ["the greatest treasure in the world 🤑", "the elixir of eternal youth 🍷", "the cure to death 🍀"]

#Game Introduction
print("\nWelcome to the adventure game! 🛸 ⛺ 👽 👣 🐻 🐾")
ready = input("\nAre you ready for this? (YES/NO) ")

if ready.lower() == "yes":
    print("Let's go! 🤠")
else:
    print("Don't worry, just read and try it! 🦾")

#Asking nested questions and producing outcomes
forest = input("\nNow, you are walking through a dark forest ⛺ and find two items: a MATCH and a FLASHLIGHT. \nWhich one do you want to pick up? ")
if forest.lower() == "match":
    so_match = input(f"\nYou pick up the match and strike it 🗽, and for an instant, the forest around you is illuminated. You see a {nouns_match[a_m]}, and then the match burns out. \nDo you want to RUN, or HIDE behind a tree? ")
    if so_match.lower() == "run":
        so_run = input(f"\nWell done friend, you managed to escape from the animal but now you are in the land of {nouns_run[a_r]}. \nYou need to get money to live, you choose to WORK or STEAL to survive ")
        if so_run.lower() == "work":
            print(f"\nVery well chosen friend, now everything depends on you, working in {nouns_run[a_r]} building weapons is a good start. don't give up!")
        elif so_run.lower() == "steal":
            print(f"\nBe careful my friend, you are now wanted by the authorities, as a fugitive you have to join the gang of thieves of {nouns_run[a_r]}, grim adventures await you!")
        else:
            print(f"\nNothing convinces you, don't worry, in {nouns_run[a_r]} like this you can start creating your own business, let nothing stop you!")
    elif so_match.lower() == "hide":
        so_hide = input(f"\nThat was a close call, you hid but {nouns_hide[a_h]} appeared out of the sky and fought with the animal, you look up and see that it was {nouns_hide[a_h]} invasion. \nDo you UNITE with them or you FIGHT with them? ")
        if so_hide.lower() == "unite":
            print(f"\nYou chose to join them, now they will put cybernetic implants in you, since your body is not strong enough, new adventures await you with your new superpowers!")
        elif so_hide.lower() == "fight":
            print(f"\nWelcome to the resistance, they know you have experience as an engineer, you are in command of the weapons technicians, get ready for new adventures and fights!")
        else:
            print(f"\nI understand, now the only thing left for you to do is to run away and take care of your own survival, good luck there!")
    else:
        so_secret = input(f"\nI see you are someone who doesn't like to be told what to do. \nSo, do you want to ATTACK the animal or do you have a PLAN? 🤔 ")
        if so_secret.lower() == "attack":
            print(f"\nWell then, it is good for you to know that this animal is very ferocious, so try to give it a chance to attack, come on, you can do it!")
        elif so_secret.lower() == "plan":
            print(f"\nIt seems to me the most sensible thing to do, watch their movements well and don't let anything throw you off, your life depends on it!")
        else:
            print(f"\nIt seems that you don't believe anything you see, maybe you discovered that everything is a dream and you are sleeping, it's time to get up!")
elif forest.lower() == "flashlight":
    so_flashlight = input(f"\nYou pick up the flashlight and turn it on. You see {nouns_flashlight[a_f]}, but you thought you also heard something off to the side. \nDo you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ")
    if so_flashlight.lower() == "follow":
        so_follow = input(f"\nVery good friend, you have taken a path that led you to the nearest town 🌃, but you get there and you see that it is different from normal, you have actually {nouns_follow[a_w]}. \nNow you decide whether to look for ANSWERS or ADAPT yourself ")
        if so_follow.lower() == "answers":
            print(f"\nWell now you have to go to the leader of the place, who is known to be very wise and even to see the future, good luck adventurer!")
        elif so_follow.lower() == "adapt":
            print(f"\nI think it's very brave of you my friend, the first thing you have to do is to examine the whole place and see where you will spend the night, this is where your great adventures begin!")
        else:
            print(f"\nIf this does not seem right to you, I recommend you to look at your pocket, there you have a compass that guides you to what you most want, for sure you will find many surprises, good luck!")
    elif so_flashlight.lower() == "look":
        so_look = input(f"\nYou look through the trees and see that what was making noise was {nouns_look[a_l]}, you enter it and find a young girl asking for help, you save her and now she asks you to go with her to the space center, because you are the only hope. \nDo you ACCEPT or do you tell her that you will NOT go? ")
        if so_look.lower() == "accept":
            print(f"\nYou are already in the space center, she confesses her love and says she was always watching you, now she wants you to help her recover her father who was kidnapped in space, good luck my friend!")
        elif so_look.lower() == "not":
            print(f"\nWell she tells you that it was all a test, now you will be imprisoned for not wanting to help the secret forces of space, but you have super powers, so you escape, now start your escape adventure!")
        else:
            print(f"\nOk ok, take it easy, it's an important decision, even more so when you know that your powers have awakened, it's time to conquer the galaxy!")
    else:
        so_robot = input(f"\nYou don't choose from what I showed you and suddenly a robot 👾 appears in front of you, and tells you that he was the one making noise and puts you in a suit to travel to his dimension, Your choice. \nDo you TRAVEL with him, SHOOT the laser from your suit or ask him to answer your QUESTIONS first? ")
        if so_robot.lower() == "travel":
            print(f"\nGood choice, he explains you in the past life were very good friends and now he is taking you back home to continue his adventures.")
        elif so_robot.lower() == "shoot":
            print(f"\nPerfect, you were saved it was all a trap, now with this new suit you have superpowers, new adventures are coming for you!")
        elif so_robot.lower() == "questions":
            print(f"\nIt seems very sensible to me, but before that he calls you by name and tells you that you are himself, but in the past!")
        else:
            print(f"\nI see you don't want any of that, that's fine you can just run away, but I warn you it's very dangerous!")
else: 
    so_unpredictable = input(f"\nYou did not choose any of the options, I see that you are unpredictable 😎. \nSo I give you these two secret items RADIO or MAP, you choose! ")
    if so_unpredictable.lower() == "radio":
        so_radio = input(f"\nVery well, now you listen to the radio and they speak to you in a language you don't understand, you hit the radio and {nouns_radio[a_d]}. \nHe asks you for three wishes but first you must choose to give something in return, all your MEMORIES or all your YOUTH, which do you choose? ")
        if so_radio.lower() == "memories":
            print(f"\nYou decided to give away all your memories, now you won't remember anything, it's a new beginning, let's see what wishes you manage to ask for like this!")
        elif so_radio.lower() == "youth":
            print(f"\nInteresting choice, now you are older, wiser but it was all a plan to take away your strength and banish you, you still have three wishes, let's see what you will do!")
        else:
            print(f"\nAs you don't want to do anything about it you will be eliminated! Wait, you have a genie-killing weapon, you really are someone very mysterious.")
    elif so_unpredictable.lower() == "map":
        so_map = input(f"\nGood choice, a map always helps us to know where we can go, but this is different, there is only an arrow and a point that indicates {nouns_map[a_m]}. \nWill you SEEK it or SELL the map? ")
        if so_map.lower() == "seek":
            print(f"\nGood choosing, that denotes an adventurous spirit in you, many successes and may you do great!")
        elif so_map.lower() == "sell":
            print(f"\nFor sure many people would pay a lot of gold for it, this is a great opportunity to start a business, let's go all in!")
        else:
            print(f"\nI think it's time for you to make decisions my friend, it's not good to run away from responsibilities.")
    else:
        so_zombie = input(f"\nUhmmm you are a free soul! But be careful, a zombie epidemic has just started and you are the only one immune but not immortal 🦠. \nWhat will you do go to the nearest government LABORATORY or try to SAVE humanity on your own? ")
        if so_zombie.lower() == "laboratory":
            print(f"\nGood choice, now you have to walk 5 kilometers to the nearest laboratory, good luck!")
        elif so_zombie.lower() == "save":
            print(f"\nUhmm, I'm sure it's because you are a chemical engineer, we trust your knowledge, we are going to save the world!")
        else:
            print(f"\nSeriously! I don't think it's a good time not to choose anything, especially now that you know that 5,000 zombies are coming for you!")
