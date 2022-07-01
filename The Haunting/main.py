#Jeba Chowdhury
#the_haunting_refined.py
#2019.8.3
#revision of the original demo found at https://repl.it/@float_ent/the-haunting-demo
#new storyline: cody's ghost saves player from being murdered by getting player out of the way and this will have 3 paths - killing the gf maybe + either u jailed , being caught by gf - you be murdered?, you get the gf caught and you move far away
#---------------------------------
#score determines ending, most stays=gf kills u, most forewards= u kill gf and get jailed or maybe run away to hide, more debates-gf is caught and you escape far away from where she was caught, probably you move away [to a foreign country or a far away state??]

#and the ghost gives the player hints with texts
#In that communicative device
#through headphones and electrical wires/fields?
#OOOH WAIT MAYBE HE COULD MYSTERIOUSLY COMMUNICATE W GHOSTS AND SUPERNATURAL W AND WITHOUT A DEVICE, HENCE WHY HE SURVIVED THE MURDER
#-----------------------------------
#importing pre-made functions

import time

#-----------------------
#scoring system

conf_score=0
care_score=0
fals_score=0

#if c<y<z, etc at end to determine what ending out of 3 is given,, based on score
#--------------------
# '...'/pause in the text, long

def pause():
  print("")
  time.sleep(1)
  print("...")
  time.sleep(3)
  print("")

#-------------------------------
  #repeatable actions, PLEASE CHECK
  def onward_conf():
    conf_score=score_conf+1
    print("Your head is up, aiming staight at your goal.")
    time.sleep(2)

  def onward_care():
    care_score=care_score+1
    print("You avert your gaze to the side and take a breath.")
    time.sleep(2)

  def onward_fals():
    fals_score=fals_score+1
    print("You took a few steps forward and stop in your tracks.")
    time.sleep(2)

#-----------------------------
#exploration

#-------------------------------
def invalidChoice():
  print("")
  print("Invalid choice. Select again.")
  time.sleep(1)
  choice()

def choice():
  choice=(str(input("You decide to [remain], [debate], or to [proceed]?... \n")))
  if choice=="remain" or choice=="REMAIN" or choice=="Remain":
    print("")
    print("You decide to remain and observe.")
    print("")
    time.sleep(1)
    onward_fals()
    print("")
    time.sleep(1)
  elif choice=="debate" or choice=="DEBATE" or choice=="Debate":
    print("")
    print("You pace back and forth, rationally thinking about the situation.")
    print("")
    time.sleep(1)
    onward_care()
    print("")
    time.sleep(1)
  elif choice=="proceed" or choice=="PROCEED" or choice=="Proceed":
    print("")
    print("You clear your throat and look onward, moving ahead.")
    print("")
    time.sleep(1)
    onward_conf()
    print("")
    time.sleep(1)
  else:
    invalidChoice()

#-----------------------------------
#ask player's name

def askName():
  name=str(input("Please input your name. Thanks! \n"))
  pause()

#----------------------------------
#intro
askName()  
print("Year 20XX, Time 15:00, Day Sept. 23, Temerature Warm")
print("")
time.sleep(1)
print("To your left is a brick wall. There are high quality prints scattered all over.")
print("")
time.sleep(2)
print("Your curiosity takes you, examine the papers of the wall.")
print("")
time.sleep(2)
print("They all appear to be beautiful and youthful appearnce, although their ages average to about 30 years old.")
print("")
time.sleep(2)
print("Upon further evaluation, their disapperances seem to be an exact month from each other. ")
print("")
time.sleep(2)
print("Known information is provided but it is lacking in quantity and quality. The police left a note to report any details of each missing case report if they have further information to assist with the investigation.")
print("")
time.sleep(4)
print("Your eyes roam around until they meet a familiar face. You tear the paper off of the wall for reference.")
print("")
time.sleep(4)
print("This is a famous male actor who stars in many detective movies. How ironic that detectives are seeking traces for him.")
print("")
time.sleep(3)
print("His name? 'Twas Cody Carson.")
print("")
time.sleep(2)
print("His disappearance seens to be 3 weeks ago. Next week will mark one month since his vanishing act.")
print("")
time.sleep(3)
print("You chuckle and give your interest in the case.")
print("")
time.sleep(2)
print("After all...")
print("")
time.sleep(1)
print("You founded a small detective agency during your highschool phase of life and still identify with it to this day.")
print("")
time.sleep(2)
print("Completely lost in your imagination, you feel an eager tug on your arm and glance at the source it's coming from.")
print("")
time.sleep(3)
print("It was a person of a smaller frame and stature with a beautiful apperance.")
print("")
time.sleep(2)
print("You've been dating for almost a month. However their attitude is very sassy, demanding, and possesive.")
print("")
time.sleep(2)
print("'Hey, it's our date... yet- you're letting business interfere..!' Their tone is scolding and harsh.")
print("")
time.sleep(2)
print("You nearly snap back at them but taking a breath, you look at them with disapproval.")
print("")
time.sleep(2)
print(""""Hey..." """)
print("")
time.sleep(1)

#------------------------
choice()

#---------------------

print("Slowly in some moments, you leave the scence, glaring at your lover but smoothly with a smile.")
print("")
time.sleep(3)
print("They seem to not notice and tug your arm, your arms intertwined.")
print("")
time.sleep(2)
print("Being dragged along a shopping center, you grunt as your wallet empties.")
print("")
time.sleep(2)
print("The cinema.. fancy ass resturaunts... boardwalk.., the usual.")
print("")
time.sleep(2)
print("Although, it was fun in the begining")
print("")
time.sleep(2)
print("The strain it put onto your wellbeing wasn't worth it. All they wanted was a person to flex on social media rather than ")
print("")
time.sleep(2)
print("They used you and became toxic to your life.")
print("")
time.sleep(2)
print("But they are all you had")
