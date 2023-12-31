keepPlaying = "yes"
while keepPlaying.lower() == "yes":
    print(f" Greetings! I have an amazing story for you about a defiant teenage alien. I can't wait to tell you!")
    print(f" Before I tell you my story I'd like to ask you a few questions.")
    print(f" After typing your answer please press enter to move ahead")
    # 5 Questions before the story begins 
    childName =input("\nWhat is your favorite boy's name?")
    while len(childName) == 0:
        childName =input("\nPlease enter a name")
    print(f" {childName}, That's a great name.")
    shipColor =input("\nWhat is your favorite color?")
    while len(shipColor) == 0:
        shipColor =input("\nPlease enter a color.")
    print(f" Wow,{shipColor} is so pretty. My favorite is pink.")
    snackType =input("\nWhat is your least favorite snack?")
    while len(snackType) == 0:
        snackType =input("\nPlease enter a snack.")
    print(f" Yeah, {snackType} are gross. I don't like them either.")
    minutesWaited =input("\nPick a number between 1 and 59.")
    while not minutesWaited.isdigit():
        minutesWaited =input(f"Value not recognized. Please enter a numeric value: ")
    print(f" {minutesWaited}, Are you a mind reader? That's the exact number I had in mind!")
    pizzaPlace =input("\nWhat is your favorite pizza place?")
    while len(pizzaPlace) == 0:
        pizzaPlace =input("Please enter a pizza place.")
    print(f"{pizzaPlace} is amazing. Let's start the story!")
    #Story begins   
    print(f"Our story begins far far away on the planet Mars,")
    print(f"where we meet a defiant teenage alien named Loni, who just turned 18.")
    print(f"In case you don't know on Mars teenagers are finally able to drive a flying saucer.")
    print(f"So Loni got a brand new top of the line {shipColor} flying saucer.")
    print(f"He wanted so badly to fly his new saucer around for a spin but his parents said no.")
    print(f"So after his mom and dad went to sleep in their sound proof cryopods, Loni snuck to the gargage.")
    print(f"Loni knows his parents won't hear the flying saucer start. 'It's just a quick spin', He thinks as he starts his new {shipColor} saucer.")
    print(f"Loni sets off for an adventure zooming through space, going faster than he was ever allowed with his mom.")
    print(f"When out of no where there's a sattelite hurdling toward his new saucer")
    print(f"Loni steers hard to the left and the sattelite just misses him.")
    print(f"Loni exclaims'Wow, that was close.' and corrects his path only to see the Earth getting larger and larger as he is now way off course.")
    print(f"Loni starts to cry as he is unable to slow the saucer down in time and he knows he is headed for a crash.")
    print(f"The saucer slams into the ground with a loud wobble.")
    print(f"Alone, the young alien, collects hisself and starts to exit the saucer to decide if he can just fly home.")
    print(f"He hears a small boy in the distance but the boy is slowly approaching.")
    print(f"Loni has never met a human before and he is scared of the small boy.")
    #Decision one
    meetBoy = input(f"\nShould Loni speak to the human child? Type yes or no  ")
    while meetBoy.lower() != "yes" and meetBoy.lower() !="no":
        meetBoy =input("Please type yes or no:  ")
    if meetBoy == "yes":
        print(f"\nA frightened Loni slowly crawls out of his saucer to stand face to face with a small human child.")
        print(f"The small human boy greets Loni. 'Hi, my name is {childName}.Are you okay?' he said.")
        print(f"Loni responds,'Hi, I am Loni and I think I am okay but I can't fly home in the saucer.'")
        print(f"{childName} asks Loni if he wants to call his mother for help with his saucer.")
    else:
        print(f"The frightened Loni crawls to the farther part of the ship away from the noise to hide until it leaves")
        print(f"After the small human boy left the area Loni waited a while longer until he thought it was safe.")
        print(f"Loni inspects his saucer and knows it is broken beyond being flyable.")
        print(f"'Maybe I should call my mom', Loni thinks.")
    #Decision two
    callMom = input(f"Should Loni call his mom? Type yes or no: ")
    while callMom.lower() != "yes" and callMom.lower() != "no":
        callMom =input("Please type yes or no: ")
    if callMom == "yes":
        print(f"Loni decided to call his mom")
    else:
        print(f"Loni was too scared of getting in trouble to call his mom")
    # Alternative Endings
    if meetBoy == "yes" and callMom == "yes":
        print(f"Loni says, 'Yeah ,{childName} I think I probably should. Do you know where I can find a phone?'")
        print(f"{childName} says,'As a matter of fact, I do. Let's walk to the store to get some {snackType} and we can use their phone.'")
        print(f"So Loni and {childName} head to the store and call Loni's mom.") 
        print(f"Loni spoke with his mother who said she was on her way with a tow saucer.")
        print(f"The boys ate their {snackType} and Loni's mom showed up after {minutesWaited} with a tow waucer.")
        print(f"Loni and his mom stopped for pizza at {pizzaPlace} and got decontaminated on their way home.")
        print(f"Loni's new {shipColor} saucer was totaled but his mom was just happy to have him home safely.")
        print(f"THE END")
    elif meetBoy == "yes" and callMom == "no":
        print(f"'No, she's gonna be so mad at me. Her and dad told me I couldn't go flying tonight.'Loni admits")
        print(f"{childName} suggests' okay well let's go get pizza and then go to my house. Then we can figure out how to get you home.'")
        print(f"Loni says'Can we go to {pizzaPlace}? It is the only Earth pizza place I know.'")
        print(f"{childName} says'sure, let's go' and off they head toward {pizzaPlace}.")
        print(f"The boys eat some pizza and sodas. Soon {childName}'s mom shows up to get her son.")
        print(f"{childName} asks about taking his friend and his mom won't allow it, but calls the FBI to report the alien encounter.")
        print(f"The FBI agents come pick up Loni and take  him back to his ship where they call his mom.")
        print(f"His mother makes a deal that they can keep his saucer in exchange for allowing her to take him home.")
        print(f"His mom was so relived he was okay that she didn't even scold him, just hurriedly got him back home.")
        print(f"THE END")
    elif meetBoy == "no" and callMom == "yes":
        print(f"Loni cowered in the back of his ship decided to use the ships sattelite phone to call his mother.")
        print(f"Loni dialed the phone number for his mom's cryopod and she picked up panicked on the first ring.")
        print(f"He told her what had happened and how scared he was and she told him she was on her way to just sit tight.")
        print(f"Loni stayed in his ship waiting for his mom for {minutesWaited} and she showed up ready to save her baby.")
        print(f"Loni spoke with his mother who said she was on her way with a tow saucer.")
        print(f"Loni and his mom stopped for pizza at {pizzaPlace} and got decontaminated on their way home.")
        print(f"Loni's new {shipColor} saucer was totaled but his mom was just happy to have him home safely.")
        print(f"THE END")
    elif meetBoy == "no" and callMom == "no":
        print(f"Loni crawls out of his ship and decides to go exploring instead of calling his mom.")
        print(f"Loni walks around a bit until he stumbles upon {pizzaPlace} where he decides to go in since he is starving.")
        print(f"Loni sits down to eat a pizza and have a soda while he decides how to get home.")
        print(f"One of the workers called and reported the alien customer to the FBI.")
        print(f"The FBI agents come pick up Loni and take  him back to his ship where they call his mom.")
        print(f"His mother makes a deal that they can keep his saucer in exchange for allowing her to take him home.")
        print(f"His mom was so relived he was okay that she didn't even scold him, just hurriedly got him back home.")
        print(f"THE END")
    keepPlaying = input(f"\nDo you want to play again? Enter yes or no: ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying =input(f"Please type yes or no: ")