import random

response = "y"
while response =="y":
    no = random.randint(1,6)

    if no ==1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if no ==2:
        print("[------]")
        print("[      ]")
        print("[  00  ]")
        print("[      ]")
        print("[------]")
    if no ==3:
        print("[-------]")
        print("[       ]")
        print("[  000  ]")
        print("[       ]")
        print("[-------]")
    if no ==4:
        print("[--------]")
        print("[        ]")
        print("[  0000  ]")
        print("[        ]")
        print("[--------]")
    if no ==5:
        print("[---------]")
        print("[         ]")
        print("[  00000  ]")
        print("[         ]")
        print("[---------]")
    if no ==6:
        print("[----------]")
        print("[          ]")
        print("[  000000  ]")
        print("[          ]")
        print("[----------]")

    response = input("Enter y to roll the diceand X to Exit")
    print("\n")