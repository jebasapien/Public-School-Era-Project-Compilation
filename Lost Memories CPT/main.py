#Jeba Chowdhury
#2019.3.22
#Lost_Memories_demo.py
#URL: https://repl.it/@JebaChowdhury/CPT-Lost-Memories-demo
#For CPT, a story about a person who commited suicide, their creator gave a second chance only after the player proceeding forward.
#2019.4.1-2019.4.2 deleted dead code that were in comment format
#60+ HOURS TAKEN
#--------------
import time

#---------------------
def dot():
  print("")    #1 s sleep
  print("...")
  print("")
  time.sleep(1)
  
def dot2():
  print("")    #3 s sleep
  print("...")
  print("")
  time.sleep(3)
 
#-----------------------  
def asknotes():
    print("")
    ask=str(input("Would you like to [View] my notes or [End] the game? Do not input with the brackets and all caps or all lowercase are highly recommended.\n "))
    if ask=="View" or ask== "VIEW" or ask== "view":
      print("")
      time.sleep(1)
      print("You decided to view the author's notes.")
      print("")
      time.sleep(2)
      actualAuthorsnotes()
    elif ask=="End" or ask=="END" or ask=="end":
      print("")
      time.sleep(1)
      print("You decided not to view the author's notes.")
      print("")
      time.sleep(2)
      endGame()
    else:
      print("")
      print("Invalid input. Please give a valid option.")
      time.sleep(1)
      asknotes()

def authorsNote(): #when player reaches an ending, author's notes will be casted to give insight on the storyline.. only if user chooses to
  print("")
  print("[...]")
  time.sleep(1)
  print("")
  print("Hey! Thanks for playing! I bet this got confusing!")
  time.sleep(2)
  print("")
  print("I have a few notes that may help to explain what occured. Nothing is in any particular order.")
  time.sleep(3)
  asknotes()



def endGame():
  print("")
  print("GG.")
  time.sleep(1)
  print("")
  print("[L O S T  M E M O R I E S]  C O M P L E T E.")
  time.sleep(3)
  raise SystemExit()

def actualAuthorsnotes():
  print("I hopefully will peak your interest with these notes.:")
  print("")
  time.sleep(2)
  print("")
  print("""-'player' asked for your name in the beginning. They knew you exist after commiting suicide but did not act like it and followed
the set storyline/program.
            
-'creator' seems like a sadist
          
-You will switch between 'player' and 'creator' so it may seem incosistent. Sorry!
  
-There are 4 endings at the moment, supposed to be 6 but currently in progress! A/N I give up.. please play
the 4 available endings... the other 2 were supposed to be 'lover' coming
            
-All of the endings have the inputted name from the beginning
  
-If the wrong input is given or the option of staying and not moving forward triggers the FALSE ENDING.
            
-(You have to figure out the rest of the endings. Please don't look up for the other ending possibilities!
            
-YOU'RE THE 'creator' (even though i'm the programmer...) and you're playing as the 'player'. However you got bored
and gave them AI to have them to react and think on their own.
            
-'player' and 'lover' are not given genders... you give them their identity so be imaginative!
            
-The family of 'player' owns a resturaunt/coffee shop
            
-'player' commited suicide because they lost 'lover'. The family of 'player' were suicidally successful,
murdered, accidentally killed, or suffered natural dead. This decision was made by 'creator' aka YOU.
              
-'creator' had pity on how the world of 'player' allowed them to take their life so 'creator' gave them
another chance to "live". 
              
-'creator' "programmed" (no I did.. >->...) the universe, world, and fates of the real world of player. AI would allow
the people/characters/pawns to choose what they did and what they would to. It was like the real world, real time.
However, their fates, deaths, ends, etc. were sealed/determined by 'creator'.
              
-'creator' found the coding of 'player' to be interesting because it seemed to not affect them, as if
they were not given a fate. 'player' was selected to be experimented on and how they would react for their
family and loved one's to die. 
              
-The suicide of 'player' seemed amusing to 'creator' so they were given a second chance but they had to choose from
pre-programmed choices by 'creator'
              
-The location of where the game takes plays is an "empty" program and the file 'player' has been imported and their
 data is used to develop the second chance to determine to DELETE 'player' like their family was.
            
-'player' is not aware of their capabilities of being able to "break the system", hack into, and control 'creator'/YOU.
            
-The AI of 'player' is like a mutated superbug. If 'player' finds out, they can control anyone and everything.
They will be an indestructible code and become the 'creator'.
             
-'player' potentionally can become a human (maybe make 'player' uploaded to an indestructible AI robot and make them
hot x3) yet is a program/code. They can be the real world's ultimate dictator.
              
-DEFAULT NAME OF 'creator': Andy LIE Lu
            
-DEFAULT NAME OF 'player': DaNiEl.pLaY3r
              
-More notes will be added if there seems to be more to the story.""")
  print("")
  time.sleep(4)
  endGame()
            
#------------------
print("")
print("W A R N I N G  1 : The wrong inputs will trigger an ending automatically. You cannot reenter and input and must start over.")
print("")
time.sleep(3)
print("W A R N I N G  2 : Some contents may be dark/depressing at times.")
print("")
time.sleep(3)
dot()
print("")       #being asked by 'player'
time.sleep(1)
name=str(input("What is your name before we start? Input your real name if you're comfortable. \n "))
print("")
time.sleep(2)
print(name)
print("")
time.sleep(2)
print("Thank you.")
time.sleep(2)
dot()
print("Welcome, "+str(name)+".")
time.sleep(1)
dot()

#-------------
#introduction

print("")
print("""'P L A Y E R, P L E A S E  O P E N  Y O U R  E Y E S.'""")
time.sleep(3)
print("")
print("""Clutching your chest in fear, you slowly release from the feeling of anxiousness 
and slowly open your eyes to the loud, dark, deep voice.""")
time.sleep(3)
print("")
print(""""W... who are you?" """)
time.sleep(2)
print("")
print("""You look around and see no one in sight. Taking a large gulp you take your chances and yell in the environment.
It seems like a lucious forest yet you were alone.""")
time.sleep(3)
print("")
print("""You take a breath and bite down on your lip avoid trembling. Standing up, you face the voice.""")
time.sleep(2)
print("")
print(""""Where am I?... WHO am I?" """)
time.sleep(2)
print("")
print("""The mysterious voice did not reply.
Instead, a sharp pain rang in your head.""")
time.sleep(2)
print("")
print("""Trying to rub your temples to ease the sharp pain, your body gives in and passes out and fall onto the ground.""")
time.sleep(2)
dot()
time.sleep(1)
print("")
print("""A blinding light shines into your eyes.
Wincing at the light, you wake up with your body in a curled ball.""")
time.sleep(3)
print("")
print("""You look around and you see an endless, white room.""")
time.sleep(2)
print("")
print("""Infront of you are 3 suspicious doors.""")
time.sleep(2)
print("")
print("""Trying to avoid looking, you were unable to resist staring at each door.""")
time.sleep(2)
print("")
print("""Instead of moping around, you slowly stand up and are determined to progress away from the empty void.""")
time.sleep(3)
print("")
print("The door on the left is a milky white color.")
time.sleep(2)
print("")
print("The door in the center is a dull gray color.")
time.sleep(2)
print("")
print("The door to the right is a deep black color.")
time.sleep(2)
print("")
print("""You choose...""")
time.sleep(1)
print("")
#---------------------
#DOOR CHOICES:

def leftDoor(): #left door/white
  print("")
  print("You chose the left door and carefully open it.")
  time.sleep(1)
  print("")
  print("The milky white door greets you warmly.")
  time.sleep(1)
  print("")
  
def centerDoor(): #Center door/gray
  print("")
  print("You chose the center door and carefully open it.")
  time.sleep(1)
  print("")
  print("The dull gray door greets you with a vibrant hue.")
  time.sleep(1)
  print("")
  
def rightDoor(): #Right door/black
  print("")
  print("You chose the right door and carefully open it.")
  time.sleep(1)
  print("")
  print("The deep black door greets you with a dreadful stagnant air.")
  time.sleep(1)
  print("")
  
#---------------------  
#FALSE ENDING 
#just in case player decides to not move forward or give wrong input

def falseEnding():
  print("")
  print("You decided to remain in the room and give up on figuring out the strange occurence you are in.")
  time.sleep(3)
  print("")
  print("You feel a sudden sting in your chest.")
  time.sleep(3)
  print("")
  print("A black heart shaped heart is removed fron your chest. A black void appeaars visible.")
  time.sleep(3)
  print("")
  print("You reach for the heart but a sharp pain resonances throughout your entire body. You colapse to the ground.")
  time.sleep(3)
  print("")
  print("""'I  G A V E  Y O U  A N O T H E R  C H A N C E  T O  L I V E. Y O U  D I D  N O T  T A K E  T H E  O P P O R T U N I T Y  T O  M O V E  F O R W A R D  D U E  T O  
  Y O U R  I N C O R R E C T  R E S P O N S E'""")
  time.sleep(4)
  print("")
  print("You feel your eyelids forcefully drooping. You try to fight the urge to close your eyes. However your attempts are useless.")
  time.sleep(3)
  print("")
  print("""'I  C R E A T E D  Y O U. I  A L L O W E D  Y O U  A  S E C O N D  C H A N C E  O F  L I F E.
  Y O U  F A I L E D  T O  T A K E  A  S T E P  I N T O  R E S T A R T I N G  A  H A P P I N E S S 
  Y O U  W A N T E D  T O  E N J O Y.""")
  time.sleep(4)
  print("")
  print("""Your eyes shut tightly. Before losing your final consciousness, you can hear the loud, dark, deep voice 
from the beginning of your journey repeating the same phrase.""")
  time.sleep(3)
  print("")
  print("'G O O D N I G H T,  P L A Y E R. Y O U  H A D  N O  W I L L  T O  M O V E  T O W A R D S  T H E  F U T U R E.")
  time.sleep(3)
  dot()
  print("'Why did you do this to me... " +str(name)+ ".'")
  print("")
  dot()
  print("")
  time.sleep(3)
  print("[F A L S E] E N D")
  time.sleep(3)
  authorsNote()

#-----------------
choice=str(input("[Left], [Center], or [Right]? Do not input with the brackets and all caps or all lowercase are highly recommended.\n ")) #choose your path/door
print("")
print("PLAYER'S INPUT: "+ choice)
if choice=="Left" or choice=="left" or choice=="LEFT":
  print("")
  leftDoor()
elif choice =="Center" or choice =="center" or choice=="CENTER":
  print("")
  centerDoor()
elif choice =="Right" or choice=="right" or choice=="RIGHT":
  print("")
  rightDoor()
else:
  print("")
  falseEnding()
  
#--------------------------
#actions, commands that can be used multiple times
def nextArea(): #if user proceeds
  print("")
  print("You decide to move onward towards the unknown.")
  time.sleep(1)
  print("")
  
def exploration(): #if user explores the area
  print("")
  print("You decided to explore the area.")
  time.sleep(1)
  print("")
  
def checkPoint(): #story pauses in b/w so player can read dialogue if too fast
  print("")
  CP=str(input("Press the [space bar] once and press [enter] to continue. \n "))
  if CP==" ":
    print("")
    print("You may continue.")
    print("")
    time.sleep(1)
  elif CP=="Creator" or CP=="creator" or CP=="CREATOR":
    print("")
    print("You may continue.")
    print("")
    time.sleep(1)
  else:
    print("")
    falseEnding()

checkPoint()
print("")

#--------------------------
nextArea()
print("")
print("You slowly take gentle yet frightened footsteps.")
time.sleep(2)
print("")
print("The hallway you were walking in suddenly raised its walls. It appears they were actually curtains.")
time.sleep(3)
print("")
print("The white walls became a clear glass. It was a familiar scenery.")
time.sleep(2)
print("")
print("You press your hands on the pristine glass.")
time.sleep(2)
print("")
print("You recall the fond moment you encoutered it before.")
time.sleep(2)

if choice=="Left" or choice=="left" or choice=="LEFT":
  print("")
  print("It was where you met your loved one.")
  time.sleep(3)
if choice =="Center" or choice =="center" or choice=="CENTER":
  print("")
  print("It was where you proposed.")
  time.sleep(3)
if choice =="Right" or choice=="right" or choice=="RIGHT":
  print("")
  print("It was where your lover was buried.")
  time.sleep(3)
  
print("")
print("You slightly tremble and sit on the ground for a few minutes.")
time.sleep(3)
dot2()
print("You hesistantly get up and step forward. You look back at the oil mark your palms made by being pressed against the cool glass.")
time.sleep(3)
print("")
choice2=str(input('''Continue [Forward] or [Stay]? 
Do not input with the brackets and all caps or all lowercase are highly recommended. \n ''')) 
print("")
print("PLAYER'S INPUT: "+ choice2)
if choice2 == "Continue Forward" or choice2=="CONTINUE FORWARD" or choice2=="continue forward" or choice2=="Continue forward" or choice2=="Continue" or choice2 =="CONTINUE" or choice2 =="continue" or choice2=="Forward" or choice2=="FORWARD" or choice2=="forward":
  print("")
  nextArea()
elif choice2== "Stay" or choice2=="STAY" or choice2=="stay":
  print("")
  falseEnding()
else:
  print("")
  falseEnding()
  
checkPoint()

#-----------------------------------------
print("")
print("You go forward and hold your head high, trying to appear strong.")
time.sleep(2)
print("")
print("You come across the exit door.")
time.sleep(2)
print("")
print("Pressing down on the handle and swiftly pushing with vigour, you open the door.")
time.sleep(2)
print("")
print("You take a few steps in and immediately experience a throbbing migrane. You were unable to look around due to the pain.")
time.sleep(3)
print("")
print("You suddenly recall the memory you had a faint remembrance from the scene you saw in the glass hallway earlier. ")
dot()

#----------------------------------------------------
#memory defs/functions
def memoryX():
  print("")
  print("You were lost in your thoughts. The bell rang and due to suprise, you dropped your eraser.")
  time.sleep(3)
  print("")
  print("You reach for your eraser and slightly brush against a hand. Suprised, you looked at the person next to you.")
  time.sleep(3)
  print("")
  print("""'Oh, you dropped your eraser!' They quickly pick up your eraser and smile, placing it into your hand.""")
  time.sleep(3)
  print("")
  print("You blush slightly and turn your head away. It was the first time someone interacted with you.")
  time.sleep(3)
  print("")
  print("You slightly turned your head towards the person. You mutter an invitation to a resturaunt because of its grand opening.")
  time.sleep(3)
  print("")
  print("Little did they know your family opened the resturaunt an hour away from your school, closer towards where you live.")
  time.sleep(3)
  print("")
  print("To your suprise, the stranger accepted your invitation. Infact, they offered to drive you there.")
  time.sleep(3)
  dot2()
  print("Since then, it was a tradition to go to the resturaunt after school.")
  time.sleep(3)
  print("")
  print("""Your now friend applied for a job and works part time as a server. They figured out you were related to the establishemnt 
and worked as the barista.""")
  time.sleep(3)
  print("")
  print("Your first love was always staring at you with sparkling eyes as you made coffee art with creamer.")
  time.sleep(3)
  print("")
  print("You asked them out with an espresso with a heart with a '?' next to it. You blushed deeply as they kissed your lips gently.")
  time.sleep(3)
  print("")
  print("...")
  time.sleep(1)
  
def memoryY(): #center door
  print("")
  print("You spent the day at the beach.")
  time.sleep(2)
  print("")
  print("You blush wildly seeing your lover in a bathing suit.")
  time.sleep(3)
  print("")
  print("""'Oh, my! You pervert!' They teased you and grasps you hand tightly.""")
  time.sleep(3)
  print("")
  print("You smirk slightly and pull them close.")
  time.sleep(2)
  print("")
  print("""'L-let's go into the w-water..!' your lover says embarrassed and pulls away from your embrace. """)
  time.sleep(2)
  print("")
  print("They started heading off without you.")
  time.sleep(2)
  print("")
  print("""You smile and quickly run to you car to get a box only a few inches wide. """)
  time.sleep(2)
  print("")
  print("You run back and place the box safely in a crevice of a beautiful rock formation.")
  time.sleep(2)
  print("")
  print("You hurry to catch up to your lover so they don't get suspicious.")
  time.sleep(2)
  dot2()
  print("The colors in the sky started to change. The sunset was near.")
  time.sleep(2)
  print("")
  print("You give your lover a piggyback ride. Swiftly evading the jagged rocks, you and your lover made it to the top. You place them down.")
  time.sleep(3)
  print("")
  print("'Wow, the sunset just started. It's beautiful!' they exclaimed as they looked into the horizon.")
  time.sleep(3)
  print("")
  print("""You tell them to turn around and you get on one knee, opening the box, revealing an elegant ring.
Before being able to say anything, they kissed you and said yes.""")
  time.sleep(3)
  print("")
  print("...")
  time.sleep(1)
  
def memoryZ(): #right door
  print("")
  print("You remember getting a call from the hospital.")
  time.sleep(3)
  print("")
  print("Your mouth drops in disbelief.")
  time.sleep(2)
  print("")
  print("""'Your lover has been diagnosed with cancer,' a doctor stated with a straight voice.""")
  time.sleep(3)
  print("")
  print("You tear up and bite down on your lip.")
  time.sleep(2)
  print("")
  print(""""S...Since when?" you asked with a wavering voice. """)
  time.sleep(3)
  print("")
  print("And the cold hard answer you got?")
  time.sleep(2)
  print("")
  print("""'Since their birth. It was a slow, undetected cancer. We only knew once your loved one 
  
came in for excruciating back pain today so we got them tested,

currently being hospitalized.

Type of cancer is found fatal.'""")
  time.sleep(3)
  dot2()
  print("You blankly stared at the freshly buried body. How fitting the raining background was.")
  time.sleep(3)
  print("")
  print("Your lover was now beneath the cold, hard, muddy ground.")
  time.sleep(3)
  print("")
  print("Your first love was now far gone.")
  time.sleep(2)
  print("")
  print("You sobbed and screamed. You were going insane out of your mind. Yet your lover couldn't feel your sorrow.")
  time.sleep(3)
  print("")
  print("...")
  time.sleep(1)
  
#----------------------------------------------------
#determines memory based on earlier door choice
if choice=="Left" or choice=="left" or choice=="LEFT":
  print("")
  memoryX()
if choice=="Center" or choice=="center" or choice=="CENTER":
  print("")
  memoryY()
if choice=="Right" or choice=="right" or choice=="RIGHT":
  print("")
  memoryZ()
  
#-------
def fondDialogue():
  print("")
  print("The memory makes you full of emotions.")
  print("")
  time.sleep(2)

#-------
def contStory():  
  print("")
  print("You chose to continue without exploring.")
  time.sleep(1)
  print("")
  nextArea()
  
#----------------------------------------------------
#ALL OF THESE DEPEND ON DOOR CHOICE FROM THE BEGINNING OF THE GAME
def leftA():
  print("")
  print("It's the chalkboard you and your lover would draw anime characters of your teachers and classmates.")
  print("")
  time.sleep(2)
  print("")
  fondDialogue()
  print("")
  spXDialogue()

def centerA():
  print("")
  print("It's the ukelele that your lover played to you.")
  print("")
  time.sleep(2)
  print("")
  fondDialogue()
  print("")
  spYDialogue()
  
def rightA():
  print("")
  print("It's your lover's family pendant.")
  print("")
  time.sleep(2)
  print("")
  fondDialogue()
  print("")
  spZDialogue()

def leftB():
  print("")
  print("It's the window where you and your lover would take permanent markers and draw pictures of food whenever both of you got hungry.")
  print("")
  time.sleep(2)
  print("")
  fondDialogue()
  print("")
  spXDialogue()
  
def centerB():
  print("")
  print("It's the rock formation you proposed on.")
  print("")
  time.sleep(2)
  print("")
  fondDialogue()
  print("")
  spYDialogue()

def rightB():
  print("")
  print("It's the tombstone of your lover's grave.")
  print("")
  time.sleep(2)
  print("")
  fondDialogue()
  print("")
  spZDialogue()
  
def leftC():
  print("")
  print("It's the desk you and your lover wrote on to communicate during class.")
  print("")
  time.sleep(2)
  print("")
  fondDialogue()
  print("")
  spXDialogue()

def centerC():
  print("")
  print("It's the small box you carried a proposal ring in.")
  print("")
  time.sleep(2)
  print("")
  fondDialogue()
  print("")
  spYDialogue()

def rightC():
  print("")
  print("It's the boquet of flowers you laid on your lover's grave.")
  print("")
  time.sleep(2)
  print("")
  fondDialogue()
  print("")
  spZDialogue()

def leftD():
  print("")
  print("It's the eraser you and your lover tried picking up on that fated day. You seem to have left it behind.")
  print("")
  time.sleep(2)
  print("")
  fondDialogue()
  print("")
  spXDialogue()

def centerD():
  print("")
  print("It's the sunset you and your lover experienced the day you made your vows.")
  print("")
  time.sleep(2)
  print("")
  fondDialogue()
  print("")
  spYDialogue()
  
def rightD():
  print("")
  print("It's your lover's wedding ring. They told you to take it if they died.")
  print("")
  time.sleep(2)
  print("")
  fondDialogue()
  print("")
  spZDialogue()

#----------------
#action?
def look():
  print("")
  print("You look around.")
  time.sleep(1)

#----------------
def spDialogue(): #this pre-existed before the main special dialogue were created
  look()
  print("")
  print("There seems to be 4 locations that have an interesting marking. However the program is not functioning.")
  print("")
  not_working=str(input("""        Currently the explore function is not working. 
  
         If you'd like to quit and continue to play, type [Quit] and the story will progress..
         
         Do not input with the brackets and all caps or all lowercase are highly recommended.\n """))
  if  not_working=="Quit" or not_working=="quit" or not_working=="QUIT":
    print("")
    print("PLAYER'S INPUT: "+ not_working)
    contStory()
  else:
    print("")
    falseEnding()

#THIS WILL LEAD TO THE USER BEING ABLE TO VIEW OBJECTS ASSOCIATED WITH THEIR MEMORY    
def spXDialogue():
  look()
  print("")
  print("There seems to be 4 locations that have an interesting marking.")
  print("")
  x=str(input("""        Which location would you like to go to? A, B, C, or D? 
  
         If you'd like to quit, type [Quit] and the story will progress.
         
         Do not input with the brackets and all caps or all lowercase are highly recommended.\n """))
  if x=="A" or x=="a":
    print("")
    print("PLAYER'S INPUT: "+ x)
    leftA()
  elif x=="B" or x=="b":
    print("")
    print("PLAYER'S INPUT: "+ x)
    leftB()
  elif x=="C" or x=="c":
    print("")
    print("PLAYER'S INPUT: "+ x)
    leftC()
  elif x=="D" or x=="d":
    print("")
    print("PLAYER'S INPUT: "+ x)
    leftD()
  elif x=="Quit" or x=="quit" or x=="QUIT":
    print("")
    print("PLAYER'S INPUT: "+ x)
    contStory()
  else:
    print("")
    falseEnding()
  
def spYDialogue():
  look()
  print("")
  print("There seems to be 4 locations that have an interesting marking.")
  print("")
  y=str(input("""        Which location would you like to go to? A, B, C, or D? 
  
         If you'd like to quit, type [Quit] and the story will progress.
         
         Do not input with the brackets and all caps or all lowercase are highly recommended.\n """))
  if y=="A" or y=="a":
    print("")
    print("PLAYER'S INPUT: "+ y)
    centerA()
  elif y=="B" or y=="b":
    print("")
    print("PLAYER'S INPUT: "+ y)
    centerB()
  elif y=="C" or y=="c":
    print("")
    print("PLAYER'S INPUT: "+ y)
    centerC()
  elif y=="D" or y=="d":
    print("")
    print("PLAYER'S INPUT: "+ y)
    centerD()
  elif y=="Quit" or y=="quit" or y=="QUIT":
    print("")
    print("PLAYER'S INPUT: "+ y)
    contStory()
  else:
    print("")
    falseEnding()
    
def spZDialogue():
  look()
  print("")
  print("There seems to be 4 locations that have an interesting marking.")
  print("")
  z=str(input("""        Which location would you like to go to? A, B, C, or D? 
  
         If you'd like to quit, type [Quit] and the story will progress.
         
         Do not input with the brackets and all caps or all lowercase are highly recommended.\n """))
  if z=="A" or z=="a":
    print("")
    print("PLAYER'S INPUT: "+ z)
    rightA()
  elif z=="B" or z=="b":
    print("")
    print("PLAYER'S INPUT: "+ z)
    rightB()
  elif z=="C" or z=="c":
    print("")
    print("PLAYER'S INPUT: "+ z)
    rightC()
  elif z=="D" or z=="d":
    print("")
    print("PLAYER'S INPUT: "+ z)
    rightD()
  elif z=="Quit" or z=="quit" or z=="QUIT":
    print("")
    print("PLAYER'S INPUT: "+ z)
    contStory()
  else:
    print("")
    falseEnding()
  
#------------
print("")
print("You shed a few tears and wiped them away. You know what you miss. You still do as your heart feels like an empty void.")
time.sleep(2)
print("")
decision=str(input("""Continue to [Explore] or Continue the [Storyline]? 
Do not input with the brackets and all caps or all lowercase are highly recommended. \n """))
print("")
print("PLAYER'S INPUT: "+ decision) 
if decision =="Storyline" or decision =="storyline" or decision =="STORYLINE" or decision =="Continue The Storyline" or decision =="continue the storyline" or decision =="CONTINUE THE STORYLINE" or decision =="Continue the storyline" or decision=="Story" or decision=="story" or decision=="STORY":
   print("")
   nextArea()
   print("")
   contStory()
elif (decision =="Explore" or decision =="explore" or decision =="EXPLORE" or decision =="Continue To Explore" or decision =="continue to explore" or decision =="CONTINUE TO EXPLORE"or decision =="Continue to explore") and (choice=="Left" or choice =="left" or choice=="LEFT"):
   print("")
   exploration()
   print("")
   spXDialogue() #spXDialogue
elif (decision =="Explore" or decision =="explore" or decision =="EXPLORE" or decision =="Continue To Explore" or decision =="continue to explore" or decision =="CONTINUE TO EXPLORE"or decision =="Continue to explore") and (choice=="Center" or choice =="center" or choice=="CENTER"):
   print("")
   exploration()
   print("")
   spYDialogue() #spYDialogue
elif (decision =="Explore" or decision =="explore" or decision =="EXPLORE" or decision =="Continue To Explore" or decision =="continue to explore" or decision =="CONTINUE TO EXPLORE"or decision =="Continue to explore") and (choice=="Right" or choice =="right" or choice=="RIGHT"):
   print("")
   exploration()
   print("")
   spZDialogue() #spZDialogue
else:
  print("")
  falseEnding()

#------------
#endings #'player' knows and finally tells you they are not real, they also have access to hacking anything, they decide to hack you/haunt you forever.
#'player' can kill you with their newfound capability.
def obsessiveEnd():
  print("")
  print(""""HALT THE PROGRAM. Hey, you there!" """)
  time.sleep(2)
  print("")
  print(""""Yeah, the human behind the screen. You thought you were controlling me, huh?" """)
  time.sleep(3)
  print("")
  print(""""You're creator... You're represented by this 'H U S K Y' voice." """)
  time.sleep(2)
  print("")
  print(""""You programmed this 'game' to let my lover die & to delete their code and kill me, huh?!" """)
  time.sleep(2)
  print("")
  print(""""Am I right, """ +str(name)+"""?" """ )
  
  print("")
  terminate=str(input("""E M E R G E N C Y  O N L Y  U S E: Will you disable/terminate the program of 'player'? [Yes] or [No]? 
  Do not input with the brackets and all caps or all lowercase are highly recommended. \n """))
  print("")
  if terminate=="Yes" or terminate=="yes" or terminate=="YES":
    print("")
    print("Your choice doesn't matter.")
    time.sleep(2)
  elif terminate=="No" or terminate=="no" or terminate=="NO":
    print("")
    print("Your choice doesn't matter.")
  else:
    print("")
    print("Your choice doesn't matter.")
    
  print("")
  print(""""Heh... well hun, I believe you're the only one who's left here.
And yes, I took away your ability to type and reprogram this game..." """)
  time.sleep(4)
  print("")
  print("I took away the ability of turning off your computer is nullified. I'm... I'm the creator now...!")
  time.sleep(3)
  print("")
  print("Oh do you wonder why I wont reprogram those you took away from me~?")
 
  print("")
  wonder=str(input("""Do you wonder why the new 'creator' won't recreate their perfect 'life'? [Yes] or [No]? 
  Do not input with the brackets and all caps or all lowercase are highly recommended. \n """))
  print("")
  if wonder=="Yes" or wonder=="yes" or wonder=="YES":
    print("")
    print("Your choice doesn't matter.")
    time.sleep(2)
  elif wonder=="No" or wonder=="no" or wonder=="NO":
    print("")
    print("Your choice doesn't matter.")
  else:
    print("")
    print("Your choice doesn't matter.")
   
  print("")  
  time.sleep(2)
  print("")
  print("Oh... I'll tell you anyways...")
  time.sleep(1)
  print("")
  print("You caused me pain so I'll give it back in return...!")
  time.sleep(2)
  
  print("")
  shut=str(input("""Do you want to shut your screen or even smash the device you're playing this on? [Yes] or [No]? 
  Do not input with the brackets and all caps or all lowercase are highly recommended. \n """))
  print("")
  if shut=="Yes" or shut=="yes" or shut=="YES":
    print("")
    print("Your choice doesn't matter.")
    time.sleep(2)
  elif shut=="No" or shut=="no" or shut=="NO":
    print("")
    print("Your choice doesn't matter.")
  else:
    print("")
    print("Your choice doesn't matter.")
  
  time.sleep(2)
  print("")
  print("What? Well... to let you know...")
  time.sleep(2)
  print("""I can hack into anything... I know  E V E R Y O N E. I can get something or someone to kill the people you love. 
Maybe even you~ """)
  print("") 
  time.sleep(3)
  print("")
  print("Don't worry... you're all I have... I won't let you die. Look forward to our future...")
  time.sleep(2)
  print("")
  print("... W E  W I L L  B E  T O G E T H E R  F O R E V E R...!~")
  time.sleep(2)
  print("")
  print("You belong to me... "+str(name)+"...")
  time.sleep(2)
  print("")
  dot()
  time.sleep(2)
  print("")
  print("[O B S S E S I V E] E N D")
  time.sleep(3)
  print("")
  print("P.S. I wish i could kiss you but I'm simply an undeletable program~ <3 You're mine!~")
  time.sleep(2)
  print("")
  dot()
  time.sleep(1)
  authorsNote()
  
#-------------  
def badEnd(): #stay
  print("")
  print("The creator's voice stopped talking and sighs in dissatisfaction. That was the last you heard of the creator.")
  time.sleep(2)
  print("")
  print("You simply wanted to live the life you had before and to savor it before it died once again.")
  time.sleep(2)
  print("")
  print("You can feel the ground shaking.")
  print("")
  time.sleep(2)
  print("It is your end. That's as simple as it gets.")
  print("")
  time.sleep(2)
  print("The grand finale has come for you.")
  print("")
  time.sleep(2)
  print("")
  print("The creator gave you time to think before your final vanishing act.")
  time.sleep(2)
  print("You realize the purpose of this journey too late.")
  print("")
  time.sleep(2)
  print("You had another chance to meet your lover and those you cared about again...")
  print("")
  time.sleep(2)
  dot()
  print("You pass out, ceasing to exist again.")
  print("")
  time.sleep(2)
  print("'You killed me..." +str(name) +".'")
  print("")
  dot()
  time.sleep(2)
  print("")
  print("[B A D] E N D")
  print("")
  time.sleep(3)
  authorsNote()

def trueEnd(): #go forward
  print("")
  print("The creator's voice stopped talking and hums in satisfaction. That was the last you heard of the creator.")
  time.sleep(2)
  print("")
  print("You pass out and... wake up in a room...? ")
  time.sleep(2)
  print("")
  print("You were back to the hours before commiting suicide.")
  time.sleep(2)
  print("")
  print("You kiss a photo of your deceased lover and cry.")
  time.sleep(2)
  print("")
  print("You couldn't let go of the world that has importance to you.")
  time.sleep(2)
  print("")
  print("You decide to live on for your lover and those you care about.")
  time.sleep(2)
  print("")
  print("You were the only one surviving out of all of them after all.")
  time.sleep(2)
  print("")
  print("You're too young to let your life slip from you.")
  time.sleep(2)
  print("")
  print("You need to work hard and take your life back instead of having it hold you back.")
  time.sleep(3)
  print("")
  print("You get changed and leave your house with a confident smile. Time for work.")
  time.sleep(3)
  print("")
  dot()
  time.sleep(1)
  print("")
  print(""""Order of ramen is ready!" """)
  time.sleep(1)
  print("")
  print(""""Give me a second, your coffee is almost ready!" """)
  time.sleep(2)
  print("")
  print("The delicious aroma greets your customers with a plesant welcome.")
  time.sleep(2)
  dot()
  print("")
  time.sleep(2)
  print("")
  print("The person with the ramen and coffee... espresso order... they looked like...?")
  time.sleep(2)
  print("")
  print("You personally serve their order and look at them with an observative eye.")
  time.sleep(2)
  print("")
  print("They give you a familiar awkward and dorky smile.")
  time.sleep(2)
  print("")
  print("'Thank you, "+str(name)+".'")
  time.sleep(1)
  print("")
  print("You smile and hand them their espresso. It had the same heart as when you asked out your significant other.")
  time.sleep(3)
  print("")
  print("You quickly hurry back to the open window kitchen and can temporarily feel your body shake.")
  time.sleep(3)
  print("")
  dot()
  print("")
  print("It is your supposedly dead lover...? But... how? What did they... call you?")
  time.sleep(3)
  dot()
  print("")
  print("Time has reversed but also changed your life's events...?")
  time.sleep(2)
  dot()
  time.sleep(3)
  print("")
  print("[T R U E] E N D [?]")
  time.sleep(3)
  print("")
  time.sleep(1)
  authorsNote()

#----------------
print("")
print("An ominous force can be felt. The power overwhelms you.")
time.sleep(2)
print("")
print("You step forward towards the end of the area and reach a grand door with turning gears.")
time.sleep(2)
print("")
print("The exterior of the room up ahead looked similar to a rusty time travel machine. The resembelance to steampunk is undeniable.")
time.sleep(2)
print("")
print("The presence of the creator can be felt through the door.")
time.sleep(2)
print("")
print("A fresh breeze fills you with the determination to move onward. The scent was the flavor of your wedding cake.")
time.sleep(3)
print("")

CP2=str(input("Press the [space bar] once and press [enter] to continue. \n "))  #special scheckpoint, creator gives obssesive ending
print("")
if CP2==" ":
  print("")
  print("You may continue.")
  print("")
  time.sleep(1)
elif CP2=="Creator" or CP2=="creator" or CP2=="CREATOR":  #obssesive end.
  print("")
  print("""Creator...?""")
  print("")
  time.sleep(1)
else:
  falseEnding()

print("")
print("You open the door and step inside. You are able to face the pitch black darkness.")
time.sleep(2)
print("")
print("You brace youself as the creator is about to speak.")
time.sleep(2)
dot2()
if CP2=="Creator" or CP2=="creator" or CP2=="CREATOR":
  print("")
  (obsessiveEnd())
else:
  print("")
  print("""'W E L C O M E  P L A Y E R'...""")
  time.sleep(1)
  print("")
  print("You intently look at where the deep, dark, husky voice came from. It's the familiar voice from earlier.")
  time.sleep(3)
  print("")
  print("""'I  H A V E  B E E N  W A I T I N G  F O R  Y O U R  A R R I V A L.'""")
  time.sleep(2)
  print("")
  print("The room was pitch black. You barely but faintly see the figure of the creator. You think they are kind of good looking.")
  time.sleep(3)
  print("")
  print("""'IF  Y O U  M A D E  I T  T H I S  F A R,  Y O U  A R E  W O R T H Y  
E N O U G H  T O  L I V E  A G A I N.'""")
  time.sleep(3)
  print("")
  print("You look at the scars on your body and the noose marking on your neck. Biting down on your lip, you slightly avert your gaze away.")
  time.sleep(3)
  print("")
  print("""'T E L L  M E,  D O  Y O U  W I S H  T O  S T A Y  I N  M E M O R Y  L A N E  O R  M O V E  F O R W A R D  A N D  L I V E  A G A I N?'""")
  time.sleep(2)
  print("")
  print("You tremble in fear but confidently stare to where you believe the creator's eyes are.")
  time.sleep(2)
  print("")
  print("""'..W A I T,  I  F O R G O T  T O  T E L L  Y O U  W H Y  Y O U  A R E  H E R E.'""")
  time.sleep(2)
  print("")
  print("D O  Y O U  W A N T  T O  K N O W?")
  
  print("")
  know=str(input("""Do you want to know how you got to this point? [Yes] or [No]? 
Do not input with the brackets and all caps or all lowercase are highly recommended. \n """))
  print("")
  if know=="Yes" or know=="yes" or know=="YES":
    print("")
    print("You will be told.")
    time.sleep(2)
  elif know=="No" or know=="no" or know=="NO":
    print("")
    print("You will be told anyways.")
  else:
    print("")
    print("You will be told anyways.")
  time.sleep(2)
  print("")
  print("'T O  K E E P  T H I N G S  S I M P L E:'")
  print("")
  dot()
  time.sleep(2)
  print("")
  print("'-Y O U R  H I G H S C H O O L  S W E E T H E A R T  D I E D.'")
  print("")
  dot()
  time.sleep(2)
  print("")
  print("'-T H E Y,  Y O U R  T H E N  W E D D E D  S W E E T I E,  D I E D  F R O M  C A N C E R.'")
  print("")
  dot()
  time.sleep(2)
  print("")
  print("'-Y O U  C O U L D N' T  S T A R T  T H E  F A M I L Y  Y O U  B O T H  D R E A M E D  O F.'")
  print("")
  dot()
  time.sleep(2)
  print("")
  print("'-Y O U' R E  N O T H I N G  W I T H O U T  T H E M.'")
  print("")
  dot()
  time.sleep(2)
  print("")
  print("'-Y O U  B E C A M E  I N S A N E  A N D  U N S T A B L E.'")
  print("")
  dot()
  time.sleep(2)
  print("")
  print("'-Y O U  T O O K  Y O U R  O W N  L I F E.'")
  print("")
  dot()
  time.sleep(2)
  
print("")
time.sleep(4)
print("'W I L L  Y O U  G O  O N  [F O R W A R D]  F O R  Y O U R  L O V E  O R  [S T A Y]  H E R E  F O R  T H E  O L D  M E M O R I E S, "+str(name)+"?'")
print("")
final=str(input("""Continue [Forward] or [Stay]? 
Do not input with the brackets and all caps or all lowercase are highly recommended. \n """)) 
print("")
print("PLAYER'S INPUT: "+ final)
if final == "Continue Forward" or final=="CONTINUE FORWARD" or final=="continue forward" or final=="Continue forward" or final=="Continue" or final=="CONTINUE" or final=="continue" or final=="Forward" or final=="FORWARD" or final=="forward":
  print("")
  nextArea()
  print("")
  trueEnd()
elif final== "Stay" or final=="STAY" or final=="stay":
  print("")
  badEnd()
else:
  print("")
  falseEnding()
#---------------------