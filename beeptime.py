import winsound

d ={'1':1000, '2':1250, '3':1500, '4':1750, '5':2000, '6':2250, '7':2500, '8':2750, '9':3000, '0':50}
def Program():
    while 1:
         x=(input())
         y=(len(x))
         a=1
         z=()
         if (x)==('tips'):
             print("""press 0 to increase the duration of song string..
                   type playlist_creation to create a playlist to save and
                   play again by typing in playlist_creation""")
         if (x)==('Playlist_creation'):
             z=(x)
         if (x)==('Play_playlist'):
             x=(z)
         else:
             if x is 'q' or x is 'Q':
                break
         if '0' in x:
             for i in range(y):
                 if (x[i]) in (d.keys()):
                     print("Now playing "+ x[i])
                     winsound.Beep(d[x[i]],1000)
                 else:
                     print("""Your response was not valid, try using:
                                          j,f,k,d,l,s""")
                     Program()

         for i in range(y):
             if (x[i]) in (d.keys()):
                 print("Now playing "+ x[i])
                 winsound.Beep(d[x[i]],500)
             else:
                 print("Invalid Response, Try Number keys")
                 Program() 
             
            
            

def Sound():
    print("press 1 to beep")
    j=(input())
    if (j)==('1'):
        winsound.Beep(1000,500)
    else:
        print("YOU BETTER LISTEN TO MY DIRECTIONS! RESTART!")
        Sound()
    print("press 2 to big beep")
    f=(input())
    if (f)==('2'):
        winsound.Beep(1250,500)
    else:
        print("YOU BETTER LISTEN TO MY DIRECTIONS! RESTART!")
        Sound()
    print("press 3 to really big beep")
    k=(input())
    if (k)==('3'):
       winsound.Beep(1500,500)
    else:
        print("YOU BETTER LISTEN TO MY DIRECTIONS! RESTART!")
        Sound()
    print("press 4 to mega big beep.")
    d=(input())
    if (d)==('4'):
        winsound.Beep(1750,500)
    else:
        print("YOU BETTER LISTEN TO MY DIRECTIONS! RESTART!")
        Sound()
    print("press 5 to super mega beep.")
    l=(input())
    if (l)==('5'):
        winsound.Beep(2000,500)
    else:
        print("YOU BETTER LISTEN TO MY DIRECTIONS! RESTART!")
        Sound()
    print("press 6 to ultimate mega beep")
    s=(input())
    if (s)==('6'):
        winsound.Beep(2250,500)
    else:
        print("YOU BETTER LISTEN TO MY DIRECTIONS! RESTART!")
        Sound()
    print("press 7 to big ultimate beep")
    a=(input())
    if (a)==('7'):
        winsound.Beep(2500,500)
    else:
        print("YOU BETTER LISTEN TO MY DIRECTIONS! RESTART!")
        Sound()
    print("press 8 to really big ultimate beep")
    q=(input())
    if (q)==('8'):
        winsound.Beep(2750,500)
    else:
        print("YOU BETTER LISTEN TO MY DIRECTIONS! RESTART!")
        Sound()
    print("press 9 to mega ultimate beep")
    w=(input())
    if (w)==('9'):
        winsound.Beep(3000,500)
    else:
        print("YOU BETTER LISTEN TO MY DIRECTIONS! RESTART!")
        Sound()
    
    print("Your done with the tutorial, have fun making noise, the programs yours.")
    print("By the way, press 'tips' to get epic tips and fun cheats!")
    Program()
def Choice():
    print("""Hey there! Is this your first time in this program?
          if so, you might want to do the tutorial, otherwise you
          can skip to the actuall fun! Press 't' to access the tutorial
          and 'f' to get to the fun!""")
    y=(input())
    if(y)==('t'):
        Sound()

    elif(y)==('f'):
        Program()
    else:
        print("Your response was unreadable, please re-enter response")
        Choice()
Choice()
    
