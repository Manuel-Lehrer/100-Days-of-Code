print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
direction = input(
    'You are at a crossroad. Where do you want to go? Type "left" or "right" ')  # add .lower here for the future!
direction_lower = direction.lower()

if direction_lower == "left":
    wait_or_swim = input(
        'You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to  swim across. ')
    wait_or_swim_lower = wait_or_swim.lower()
    if wait_or_swim_lower == "wait":
        which_door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you cose? ")
        which_door_lower = which_door.lower()

        if which_door_lower == "yellow":
            print("Congrats G, you got the treasure!")

        elif which_door_lower == "red":
            print("Game Over! You got set on fire")
            print('''
               (  .      )
                 )           (              )
                       .  '   .   '  .  '  .
              (    , )       (.   )  (   ',    )
               .' ) ( . )    ,  ( ,     )   ( .
            ). , ( .   (  ) ( , ')  .' (  ,    )
           (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      ''')
        elif which_door_lower == "blue":
            print("Game Over. You got pierced by a knight with a sword")
            print('''


                                 ___
                                ( ((
                                 ) ))
        .::.                    / /(
       'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
      (J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
       `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
        `::'                    \ \(
                                 ) ))
                                (_((
      ''')
        else:
            print("You chose a door that does not exist buddy. Game over!")

    else:
        print("Game over!. You got eaten by a motherfucking Shark while trying to swim your way to the island")
        print('''


                    (`.
                     \ `.
                      )  `._..---._
    \`.       __...---`         o  )
     \ `._,--'           ,    ___,'
      ) ,-._          \  )   _,-'
     /,'    ``--.._____\/--''
    ''')
else:
    print("Game Over! They were deadly snakes around the corner.")
    print('''
             _.--....
               _....---;:'::' ^__/
             .' `'`___....---=-'`
            /::' (`
            \'   `:.
             `\::.  ';-"":::-._  {}
          _.--'`\:' .'`-.`'`.' `{I}
       .-' `' .;;`\::.   '. _: {-I}`\
     .'  .:.  `:: _):::  _;' `{=I}.:|
    /.  ::::`":::` ':'.-'`':. {_I}::/
    |:. ':'  :::::  .':'`:. `'|':|:'
     \:   .:. ''` .:| .:, _:./':.|
      '--.:::...---'\:'.:`':`':./
                     '-::..:::-'
  ''')