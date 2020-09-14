import random
import os
import time
import random
os.system('clear')

from data.save import *
from data.petdata import *
from data.fileplace import *

print("╦ ╦┌─┐┬ ┬  ╔╦╗┌─┐  ╔═╗┬  ┌─┐┬ ┬")
print("╠═╣│ ││││   ║ │ │  ╠═╝│  ├─┤└┬┘")
print("╩ ╩└─┘└┴┘   ╩ └─┘  ╩  ┴─┘┴ ┴ ┴ ")

print("====================Keyboard Commands====================")
print("Enter:  This Is How You Earn Coins")
print('u:  This Is How You Upgrade The Amout Of Points You Get')
print('buy <pet>:  This Is How You Buy A Pet, The <> Are Not Needed')
print('rebirth:  This Is How You Rebirth')

ppet = "False"
dpet = "False"

while 1 < 2:

    if dog == "t":
        dpet = "True"

    if python == "f":
        ppet = "True"



    isjdadj = input('')
    inp = isjdadj.lower()

    if inp == "stats":
        os.system('clear')
        totalp = 1 * multi

        print("███████╗████████╗ █████╗ ████████╗███████╗")
        print("██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝")
        print("███████╗   ██║   ███████║   ██║   ███████╗")
        print("╚════██║   ██║   ██╔══██║   ██║   ╚════██║")
        print("███████║   ██║   ██║  ██║   ██║   ███████║")
        print("╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝")
        
        print(f"Points:  {points}")
        print(f"Point Multiplayer:  {multi}")
        print(f"Upgrade Cost:  {upcost}")
        print(f"Rebirth Level:  {rebirth}")
        print(f"Rebirth Cost:  {rebirthcost}")
        print('')
        print("True Means You Own It, False Means You Do Not Own It")
        print(f"Python={ppet}, Python Stats 1-5 Points Each Enter But .045% To Lose 1-1100 Points")
        print(f"Dog={dpet}, Dog Stats You Get 3.5 * Your Multi Per Enter")

    petsa = ["petdata", "petstats"]
    if inp in petsa:
        os.system('clear')
        print('''
            
                dMMMMb  dMMMMMP dMMMMMMP        .dMMMb dMMMMMMP .aMMMb dMMMMMMP .dMMMb 
                dMP.dMP dMP        dMP          dMP" VP   dMP   dMP"dMP   dMP   dMP" VP 
                dMMMMP" dMMMP      dMP           VMMMb    dMP   dMMMMMP   dMP    VMMMb   
                dMP     dMP        dMP          dP .dMP   dMP   dMP dMP   dMP   dP .dMP   
                dMP     dMMMMMP    dMP           VMMMP"   dMP   dMP dMP   dMP    VMMMP"    
            ''')
        print(f'''
                True Means You Own It, 
                False Means You Do Not Own It,
                
                Python={ppet}
                Dog={dpet}
            ''')

    if inp == "":
        totalup = (1 * multi) + ((rebirth - 1) * 2)
        points = points + (totalup) + ((rebirth - 1) * 2)
        print(f"+ {totalup} Point(s), New Total:  {points}")
    


    if inp == "":
        
        if python == "t":
            p_num = random.uniform(1, 5)
            points = points + p_num
            print(f"+ {p_num} From Your Python, New Total: {points}")
            pa_num = random.uniform(1, 250)
            if pa_num < 2:
                pat_num = random.uniform(1, 1100)
                points = points - pat_num
                print(f'Your Python Just Bit Someone You Just Lost {pat_num} Points')

        if dog == "t":
            points = points + ((multi) * 3.5 )
            tup = ((multi) * 3.5 )
            print(f"+ {tup} From Your Dog, New Total:  {points}")


    if inp == "buy python":
        if python == "t":
            print('You Have A Python Already')
        else:
            if pythoncost > points:
                neededd = pythoncost - points
                print(f'You Do Not Have The Points To Buy This, Points Needed {neededd}')
            else:
                python = "t"
                print('You Now Have A Python')
    
    if inp == "buy dog":
        if dog == "t":
            print('You Have A Dog Already')
        else:
            if dogcost > points:
                ned = dogcost - points
                print(f"You Do Not Have The Money To Buy A Dog, Needed {ned}")
            else:
                dog = "t"
                print('You Now Have A Dog :)')

    if inp == "u":
        if upcost > points:
            needed = upcost - points
            print(f"You Do Not Have Enough Points To Upgrade\nMore Points Needed:  {needed}")
        else:
            points = points - upcost
            xxx = .2 * rebirth
            xxxx = multi * 1.1 + ((rebirth - 1 ) * 1.6)
            sss = .1 * rebirth
            ssss = upcost * 1.3
            sssss = sss + ssss
            multi = xxx + xxxx
            upcost = sssss * 1.6 
            print(f"You Have Upgraded Your Multi To:  {multi},\nYou Now Have {points} Points")


    if inp == "rebirth":
        if rebirthcost > points:
            nemoer = rebirthcost - points
            rtobit = rebirth + 1
            print(f"You need {nemoer} Points To Rebirth To {rtobit}")
        else:
            points = 1
            multi = 1
            upcost = 20
            rebirth = rebirth + 1
            rebirthcost = rebirthcost * 1.6
            print(f'You Have Just Rebirthed To {rebirth}')
    



    if inp == "clear":
        os.system('clear')


    if inp == "save":
        f = open(dataplace, "w")
        #f = open('save.py', "w")
        f.write(f"points = {points}\n")
        f.write(f"multi = {multi}\n")
        f.write(f"upcost = {upcost}\n")
        f.write(f"rebirth = {rebirth}\n")
        f.write(f"rebirthcost = {rebirthcost}\n")
        
        f.close()


        ff = open(petdataplace, "w")
        #ff = open('petdata.py', "w")
        ff.write(f"python = '{python}'\n")
        ff.write(f"pythoncost = {pythoncost}\n")
        ff.write(f"dog = '{dog}'\n")
        ff.write(f"dogcost = {dogcost}")

        ff.close()
        
        os.system('clear')

        print(" ██████████              █████                  █████████                                     █████")
        print("░░███░░░░███            ░░███                  ███░░░░░███                                   ░░███ ")
        print(" ░███   ░░███  ██████   ███████    ██████     ░███    ░░░   ██████   █████ █████  ██████   ███████ ")
        print(" ░███    ░███ ░░░░░███ ░░░███░    ░░░░░███    ░░█████████  ░░░░░███ ░░███ ░░███  ███░░███ ███░░███ ")
        print(" ░███    ░███  ███████   ░███      ███████     ░░░░░░░░███  ███████  ░███  ░███ ░███████ ░███ ░███ ")
        print(" ░███    ███  ███░░███   ░███ ███ ███░░███     ███    ░███ ███░░███  ░░███ ███  ░███░░░  ░███ ░███ ")
        print(" ██████████  ░░████████  ░░█████ ░░████████   ░░█████████ ░░████████  ░░█████   ░░██████ ░░████████")
        print("░░░░░░░░░░    ░░░░░░░░    ░░░░░   ░░░░░░░░     ░░░░░░░░░   ░░░░░░░░    ░░░░░     ░░░░░░   ░░░░░░░░ ")
else:
    print('False')
 

