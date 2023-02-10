print('''
               :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
''')




print("Welcome to the Castle of Mystery.")
print("Your mission is to enter.") 
choice1 = input("You approach the front doors of the Castle of Mystery. Do you enter or leave? \n").lower()
if choice1 == "enter":
  choice2 = input("You enter into the castle. On your left is an eerie harp echoing off the dripping stone walls. On your right, you hear voices of those who may wish to harm you. Do you go left or right? \n" ).lower()
  
  if choice2 == "left":
    choice3 = input("The eerie harp's melancholy melodies flood your ears. You feel disoriented. Before you are three doors. There is a white door with gold engravings from an unfamiliar langue. There is a black door where the music seems to be coming from. Then, there is a gray door--it is nothing special. Which door do you enter? White, gray, or black? \n").lower()
    if choice3 == "white":
      print("You discover the mystery. Then, you die. Game Over.")
    elif choice3 == "black":
      print("You are blinded by the magic toxins The cloaked men find you and feed you to the giant octopus. Game Over.") 
    elif choice3 == "gray":
      print("You walk into an empty room. You look around and step back into the hallway. The voices grow closer. You look in the mirror and see a version of yourself--only old and frail. Then, you die. Game Over.")   
    else:
      print("You cannot make a decision. The cloaked men find you staring at the doors. You look over at them. You realize this is the end. Game Over.")
  else: 
    print("The cloaked men attack you and feed you to the giant octopus. Game Over.")
else:
  print("You mission is abandoned. Maybe it was for the best. Game Over.")
