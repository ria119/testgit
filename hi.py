leaveprogram = 0

while leaveprogram != "q":

    import random

    print("This is the Dice Rolling Program !")
    print("press enter to roll")

    input()
    number = random.randint(1,6)
    if number==1:
        print("[-------------]")
        print("[             ]")
        print("[      0      ]")
        print("[             ]")
        print("[-------------]")
        print()
        print("Type 'q' to Quit")
        leaveprogram = input()
    if number==2:
        print("[-------------]")
        print("[             ]")
        print("[   0     0   ]")
        print("[             ]")
        print("[-------------]")
        print()
        print("Type 'q' to Quit")
        leaveprogram = input()
    if number==3:
        print("[-------------]")
        print("[   0     0   ]")
        print("[             ]")
        print("[      0      ]")
        print("[-------------]")
        print()
        print("Type 'q' to Quit")
        leaveprogram = input()
    if number==4:
        print("[-------------]")
        print("[   0     0   ]")
        print("[             ]")
        print("[   0     0   ]")
        print("[-------------]")
        print()
        print("Type 'q' to Quit")
        leaveprogram = input()
    if number==5:
        print("[-------------]")
        print("[   0     0   ]")
        print("[      0      ]")
        print("[   0     0   ]")
        print("[-------------]")
        print()
        print("Type 'q' to Quit")
        leaveprogram = input()
    if number==6:
        print("[-------------]")
        print("[   0     0   ]")
        print("[   0     0   ]")
        print("[   0     0   ]")
        print("[-------------]")
        print()
        print("Type 'q' to Quit")
        leaveprogram = input()
