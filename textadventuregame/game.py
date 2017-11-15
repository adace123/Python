import time
import pygame

tries = 1

def playMusic(filename, volume, loops = 0):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(loops,0.0)
    pygame.mixer.music.set_volume(volume)

def s(t,flag = True):
    if flag:
        time.sleep(t)

def blue_door():
   global tries
   playMusic("creak.mp3",0.45)
   s(5)
   playMusic("flood.mp3",0.45)
   print ("The blue door bursts off its hinges as ice-cold water rushes in and floods the room.\n")
   s(5)
   playMusic("ocean.mp3",0.45,-1)
   print ("You swim to the top of the room, desperate to catch your breath as your body begins to shut down.\n")
   s(5)
   print ("You pass out. It appears to be the end.\n")
   s(10)
   print ("You awaken. The room is dark and you panic as you realize you are underwater.\n")
   s(5)
   print ("You instinctively hold your breath. As you are about to pass out again, you try to take a breath and...\n")
   s(5)
   print ("You can breathe underwater! You are shocked at having become the first human in history to do so but you have no time to contemplate its significance.\nYou have to get out of there.\n")
   s(5)
   print ("You find your flashlight floating in the darkness and turn it on. Amazingly, it is waterproof.\n")
   s(5)
   print ("You swim nervously to the edge of the door and peek around. There are faintly lit floodlights scattered throughout the hallway.\n")
   s(5)
   print ("After a few minutes, you head out and try to get a sense of your surroundings.\n")
   s(5)
   print ("Without warning, the floodlights explode and the hallway is plunged into darkness.\n")
   s(5)
   print ("You remain perfectly still yet incredibly fearful.\n")
   s(5)
   print ("A minute later, you hear a swishing sound in the water. A pair of red, glowing eyes suddenly locks onto you.\n")
   s(5)
   print ("As the predator comes closer, it reveals itself as a huge shark with iron skin and razor-sharp teeth.\n")
   s(5)
   print ("You quickly turn the other direction, knowing you have no hope of defeating the monster.\n")
   s(5)
   print ("As you're swimming for your life, you encounter a friendly dolphin that seems to be beckoning you to ride it.\n")
   s(5)
   ride_dolphin = input("Do you want to ride the dolphin? ")
   while(ride_dolphin.lower() not in ['no','yes']):
       print ("Choose a different answer.")
       ride_dolphin = input("Do you want to ride the dolphin? ")
   if ride_dolphin.lower() == "no":
       s(5)
       print ("You continue on as the dolphin swims in the opposite direction towards the shark.\n")
       s(5)
       print ("You hear the muffled sounds of battle. They quickly fade as you make your seventh turn in what appears to be an intricate labyrinth.\n")
       s(5)
       print ("You suddenly hear the whooshing of the shark monster as it propels itself with incredible speed towards you.\n")
       s(5)
       print ("Having no other weapon, you attempt to bash it with your flashlight but it's no use.\n")
       s(5)
       print ("The shark has caught you and your journey is over.\n")
       tries += 1
       return "You died"
   else:
       s(5)
       print ("You grab onto the dolphin, which squeals in joy. You find a strange button on its head.\n")
       s(5)
       print ("You press the button and an electrified, iron spear shoots out of its mouth.\n")
       s(5)
       print ("You decide to use this newfound advantage and attack the shark. You turn around and head in its direction.\n")
       s(5)
       print ("The shark charges at you and opens its mouth to swallow both you and the dolphin.\n")
       s(5)
       print ("At that very moment you shoot a spear directly into the beast's mouth. It goes numb. Its glowing eyes turn dark and it sinks towards the floor.\n")
       s(5)
       print ("You get off the dolphin and inspect the shark. You find out it's an android and that its circuits are fried.\n")
       s(5)
       print ("You are relieved. You turn around to see the dolphin but it has already disappeared.\n")
       s(5)
       print ("Suddenly, red flashing warning lights descend from the ceiling. The hallway begins to drain.\n")
       s(5)
       print ("All the water has been drained. You hear a clicking noise coming from around the corner.\n")
       s(5)
       print ("You go to inspect it and find that a corridor has opened in one of the walls. There are two doors at the end of it.\n")
       s(5)
       door_choice = input("Do you choose the left or right door? ")
       while(door_choice.lower() not in ['right','left']):
           print ("Not a valid choice.")
           door_choice = input("Do you choose the left or right door? ")
       if door_choice == "right":
           s(5)
           print ("You enter the door on the right and take a few steps. You fall into an ice-cold pool of water.\n")
           s(5)
           print ("You hear the sound of splashing like that of the android shark but multiplied times a thousand.\n")
           s(5)
           print ("You realize you have fallen into a den of vicious sharks with no weapons and no hope of escape.\n")
           s(5)
           print ("As the sharks gather around you you realize your journey is at an end...\n")
           tries += 1
           return "You died"
       else:
           s(5)
           print ("\nYou enter the door on the left and begin descending a flight of stairs.\n")
           s(5)
           print ("You enter a cave with a narrow river running through it. There is a boat waiting for you.\n")
           s(5)
           print ("You step on the boat and let the currents guide you along the river.\n")
           s(5)
           print ("The boat comes to a stop as the water level rises towards the ceiling. You get out and begin to swim.\n")
           return "You won"

def red_door():
   global tries
   s(5)
   print ("You step out into the hallway as the cold, musty air of the starting room becomes stinging, burning mass of unbearable heat.\n")
   s(5)
   print ("The paintings on the walls begin to drip and the worn carpet in the hallway begins to catch fire.\n")
   s(5)
   print ("You begin to panic as every lungful of air draws super-concentrated heat into your body. The temperature continues to climb.\n")
   s(5)
   print ("After several minutes you pass out from heat exhaustion.\n")
   s(10)
   print ("You awaken with your clothes a sweaty clump and the soles of your shoes a mess of liquid rubber. You estimate the temperature to be well above boiling point yet you are strangely alive.\n")
   s(5)
   print ("You breath becomes steady again and you begin to plan your next move.\n")
   s(1)
   print ("Do you turn right or ...\n")
   s(2)
   print ("You suddenly hear a constant metal clanging sound coming from around the corner. It's growing louder by the minute. You try to use the key to reopen the door to the starting room but it's no good.\n")
   s(5)
   print ("As the lumbering footsteps and sharp metal grinding noise grows louder, it suddenly stops and you see a pair of green, glowing eyes staring menacingly at you from the other end of the hallway.\n")
   s(5)
   print ("As the figure approaches, you can see it has only a shadow for a face. It wields a gigantic sword and wears heavy, fireproof armor. It stares at you for a moment, raises its sword and begins to charge...\n")
   s(1)
   run_or_fight = input("Do you run or fight? ")
   s(5)
   while(run_or_fight.lower() not in ['run','fight']):
       print ("You are paralyzed with fear and have made an invalid choice.\n")
       run_or_fight = input("Do you run or fight? ")
   if run_or_fight.lower() == "run":
       print ("You run away as fast as your body will take you through the scorching heat.\n")
       s(5)
       print ("You hurriedly try all the doors but none respond to your key.\n")
       s(5)
       print ("You're out of breath and collapse to the floor. The demon catches up, lets out an inhuman growl and raises his sword. It is the end of your journey.\n")
       return "You died"
   else:
       print ("You run at the demonic figure, trying desperately to dodge its blows.\n")
       s(5)
       print ("Your hands start to shake and glow a brilliant white. Suddenly, flames erupt from them and, in your panic, you send them hurtling at the figure.\n")
       s(5)
       print ("The figure laughs and is unaffected by your newfound powers. You continue in vain to attack him until it uses the hilt of his sword to knock you to the ground.\n")
       s(5)
       print ("As the figure raises his sword to deliver the finishing blow, you notice a sparkling crack in its armor.\n")
       s(5)
       print ("You blast the crack with a furious fireball attack and the creature recoils in pain.\n")
       s(5)
       print ("The creature, its armor disintegrating from the inside, begins to burn and retreats the way it came.\n")
       s(5)
       print ("It retreats the way it came, its howls growing fainter until the hallway is eerily quiet.\n")
       s(2)
       print ("The temperature rapidly drops to normal.\n")
       s(5)
       print ("The hallway suddenly flood with light. A corridor to your right is revealed with two doors.\n")
       door_choice = input("Which door do you choose? Left or right? ")
       s(5)
       if(door_choice.lower() in ['left','l']):
           print ("You choose the left door and plunge head first into an army of vicious monsters.\n")
           s(5)
           print ("You attempt to activate your fireball powers but in your weakened state you can only generate a puny flame.\n")
           s(5)
           print ("You are quickly overwhelmed and your journey comes to an end.\n")
           return "You died"
       else:
           print ("You choose the door on the right. You ascend a flight of stairs.\n")
           s(5)
           print ("After several minutes you are still climbing the stairs. As you near the end, you see a bright light and the temperature begins to rise exponentially.\n")
           s(5)
           return "You won"

def begin_game():
    playMusic("dark.mp3",0.75)
    print ("You awaken in a dark room. Your have a lingering headache and struggle to find the light switch.\n")
    s(5,False)
    print ("The lights go on suddenly and you hear a voice coming through the walls. The air is thick with moisture and there's a lingering stale odor.\n")
    s(5,False)
    print ("There are two doors, one blue and one red. Both are locked.\n")
    s(5,False)
    print ("The voice is faint and it seems to be emanating from a crack in the wall. It repeats 'Choose your potion. Escape or die.'\n")
    s(5,False)
    print ("You hear a creaking sound coming from the wall opposite you as a hidden compartment opens to reveal a key and flashlight.\n")
    s(5,False)
    print ("The room is plunged into darkness once again and you turn on the dimly lit flashlight. You estimate it only has about 25% power.\n")
    s(5,False)
    print ("You suddenly feel the ground move beneath your feet and hastily retreat into a corner.\n")
    s(5,False)
    print ("The newly-formed crack in the ground gives off an eerie blue glow. You cautiously approach it.\n")
    s(5,False)
    print ("You inspect the crack and find it's a small door. You open the door and are presented with two mysterious potions: one red and one blue.\n")
    story_choice = input("Which do you choose? ")
    while(story_choice.lower() not in ['red','blue']):
        print ("You cannot pass until you pick either blue or red.\n")
        story_choice = input("Which do you choose? ")
    print ("\nThe room rumbles violently as the cabinet recedes and the",story_choice,"door opens.\n")
    pygame.mixer.music.stop()
    if story_choice == "red":
        if red_door() == "You died":
            play_again = input("Would you like to play again? ")
            s(5)
            if play_again.lower() in ['yes','Y']:
                begin_game()
            else:
                print ("Thank you for playing. Better luck next time.")
        else:
            print ("You have passed your trials and emerged a true warrior. You emerge from the labyrinth to find yourself on top of a volcano.\n")
            s(5)
            print ("With your fireproof power, you slide down the volcano screaming with joy. You can't wait to show your friends your new abilities.\n")
            s(5)
            game_ending()
    else:
        if blue_door() == "You died":
            play_again = input("Would you like to play again? ")
            if play_again.lower() in ['yes','y']:
                begin_game()
            else:
                print ("Thank you for playing. Better luck next time.")
                return
        else:
            print ("You have passed your trials and emerged a true warrior. You emerge from the labyrinth to find yourself at the bottom of a lake.\n")
            s(5)
            print ("You swim to the top of the lake and emerge to see a clear, blue sky and a massive volcano in the background.\n")
            s(5)
            game_ending()
           
def game_ending():
     global tries
     print ("You arrive home and find that you've been called the '8th Wonder of the World' and the nation's scientists are eager to discover the secret to your powers.\n")
     s(5)
     print ("You go to the lab where you're stopped cold as you hear the same creepy voice from before.\n")
     s(5)
     print ("You turn around and find it's one of the scientists. He tells you it was all a fear response test as the monitors in the background play your adventure in the Labyrinth.\n")
     s(5)
     print ("The scientist says, 'Welcome to the Labyrinthtory. I hope you'll stay with us for a while. We've got so much more to show you...'\n")
     s(5)
     print ("Two scientists welcome you to a room and tell you to have a seat.\n")
     s(5)
     print ("The main scientist grabs the key you collected from your pocket and walks over to a nearby cabinet.\n")
     s(5)
     print ("He unlocks the cabinet, saying 'You have done very well. My potions were a spectacular success. Now it is time for you to see what else I have in store...'\n")
     s(5)
     print ("Inside the cabinet is five potions, all of different colors. The scientist says 'Now which one would you like to try first?'\n")
     s(5)
     print (f'The end. You completed the game in {tries} round(s). Until next time...\n')
pygame.mixer.init()
begin_game()
