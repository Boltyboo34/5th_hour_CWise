#Name: Chaysen Wise and Samuel Raymond
#Class: 5th hour
#Assignment: Scenario 5

#Scenario 5
#You're all part of a new development team and the big wigs want to see what you are all capable of.
#They want you to develop whatever you want to develop, but there's only one problem:
#the same big wigs only bought enough computers for half of you. Because of this, you will
#all be split into teams of two. One serving as the brain (not using the computer),
#one serving as the hands (using the computer).

#You have until the Scenario is due to brainstorm an idea together, create a flowchart, and then
#turn that flowchart into functioning code. The code itself must have at least: 1 dictionary or list,
#1 loop, 2 if statements (elif and else statements tied to it does not count towards the total),
#1 variable with a user input, and 1 form of an assignment operator. You are free to add whatever else
#you feel is necessary to complete your concept. You will be graded based on how those ideas are
#implemented together.
tictactoeList = [0,0]
#Tic Tac Toe
while1 = 1
while2 = 1
a1 = ("_")
a2 = ("_")
a3 = ("_")
b1 = ("_")
b2 = ("_")
b3 = ("_")
c1 = ("_")
c2 = ("_")
c3 = ("_")
p1win = 0
p2win = 0
print(f"{a1}|{a2}|{a3}")
print(f"{b1}|{b2}|{b3}")
print(f"{c1}|{c2}|{c3}")
while p1win == 0 and p2win == 0:
    while1 = 1
    while2 = 1
    while while1 == 1:
        while1 = 0
        p1input = int(input())
        if p1input == 1:
            if a1 == "o":
                print("that space is taken")
                continue
            else:
                a1 = "x"
        if p1input == 2:
            if a2 == "o":
                print("that space is taken")
                continue
            else:
                a2 = "x"
        if p1input == 3:
            if a3 == "o":
                print("that space is taken")
                continue
            else:
                a3 = "x"
        if p1input == 4:
            if b1 == "o":
                print("that space is taken")
                continue
            else:
                b1 = "x"
        if p1input == 5:
            if b2 == "o":
                print("that space is taken")
                continue
            else:
                b2 = "x"
        if p1input == 6:
            if b3 == "o":
                print("that space is taken")
                continue
            else:
                b3 = "x"
        if p1input == 7:
            if c1 == "o":
                print("that space is taken")
                continue
            else:
                c1 = "x"
        if p1input == 8:
            if c2 == "o":
                print("that space is taken")
                continue
            else:
                c2 = "x"
        if p1input == 9:
            if c3 == "o":
                print("that space is taken")
                continue
            else:
                c3 = "x"
        print(f"{a1}|{a2}|{a3}")
        print(f"{b1}|{b2}|{b3}")
        print(f"{c1}|{c2}|{c3}")
        if a1 == "x" and a2 == "x" and a3 == "x":
            print("x wins")
            tictactoeList[0] += 1
            print("x has",tictactoeList[0],"wins")
            exit()
        if b1 == "x" and b2 == "x" and b3 == "x":
            print("x wins")
            tictactoeList[0] += 1
            print("x has", tictactoeList[0], "wins")
            exit()
        if c1 == "x" and c2 == "x" and c3 == "x":
            print("x wins")
            tictactoeList[0] += 1
            print("x has", tictactoeList[0], "wins")
            exit()
        if a1 == "x" and b1 == "x" and c1 == "x":
            print("x wins")
            tictactoeList[0] += 1
            print("x has", tictactoeList[0], "wins")
            exit()
        if a2 == "x" and b2 == "x" and c2 == "x":
            print("x wins")
            tictactoeList[0] += 1
            print("x has", tictactoeList[0], "wins")
            exit()
        if a3 == "x" and b3 == "x" and c3 == "x":
            print("x wins")
            tictactoeList[0] += 1
            print("x has", tictactoeList[0], "wins")
            exit()
        if a1 == "x" and b2 == "x" and c3 == "x":
            print("x wins")
            tictactoeList[0] += 1
            print("x has", tictactoeList[0], "wins")
            exit()
        if a3 == "x" and b2 == "x" and c1 == "x":
            print("x wins")
            tictactoeList[0] += 1
            print("x has", tictactoeList[0], "wins")
            exit()
        while while2 == 1:
            while2 = 0
            p2input = int(input())
            if p2input == 1:
                if a1 == "x":
                    while2 = 1
                    print("that space is taken")
                    continue
                else:
                    a1 = "o"
            if p2input == 2:
                if a2 == "x":
                    print("that space is taken")
                    continue
                else:
                    a2 = "o"
            if p2input == 3:
                if a3 == "x":
                    print("that space is taken")
                    continue
                else:
                    a3 = "o"
            if p2input == 4:
                if b1 == "x":
                    print("that space is taken")
                    continue
                else:
                    b1 = "o"
            if p2input == 5:
                if b2 == "x":
                    print("that space is taken")
                    continue
                else:
                    b2 = "o"
            if p2input == 6:
                if b3 == "x":
                    print("that space is taken")
                    continue
                else:
                    b3 = "o"
            if p2input == 7:
                if c1 == "x":
                    print("that space is taken")
                    continue
                else:
                    c1 = "o"
            if p2input == 8:
                if c2 == "x":
                    print("that space is taken")
                    continue
                else:
                    c2 = "o"
            if p2input == 9:
                if c3 == "x":
                    print("that space is taken")
                    continue
                else:
                    c3 = "o"
            print(f"{a1}|{a2}|{a3}")
            print(f"{b1}|{b2}|{b3}")
            print(f"{c1}|{c2}|{c3}")
            if a1 == "o" and a2 == "o" and a3 == "o":
                print("o wins")
                tictactoeList[1] += 1
                print("o has", tictactoeList[1], "wins")
                exit()
            if b1 == "o" and b2 == "o" and b3 == "o":
                print("o wins")
                tictactoeList[1] += 1
                print("o has", tictactoeList[1], "wins")
                exit()
            if c1 == "o" and c2 == "o" and c3 == "o":
                print("o wins")
                tictactoeList[1] += 1
                print("o has", tictactoeList[1], "wins")
                exit()
            if a1 == "o" and b1 == "o" and c1 == "o":
                print("o wins")
                tictactoeList[1] += 1
                print("o has", tictactoeList[1], "wins")
                exit()
            if a2 == "o" and b2 == "o" and c2 == "o":
                print("o wins")
                tictactoeList[1] += 1
                print("o has", tictactoeList[1], "wins")
                exit()
            if a3 == "o" and b3 == "o" and c3 == "o":
                print("o wins")
                tictactoeList[1] += 1
                print("o has", tictactoeList[1], "wins")
                exit()
            if a1 == "o" and b2 == "o" and c3 == "o":
                print("o wins")
                tictactoeList[1] += 1
                print("o has", tictactoeList[1], "wins")
                exit()
            if a3 == "o" and b2 == "o" and c1 == "o":
                print("o wins")
                tictactoeList[1] += 1
                print("o has", tictactoeList[1], "wins")
                exit()
