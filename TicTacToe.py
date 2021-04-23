import random

empty_list = [["1", "2", "3"],
              ["4", "5", "6"],
              ["7", "8", "9"]]
print(empty_list[0][0], empty_list[0][1], empty_list[0][2])
print(empty_list[1][0], empty_list[1][1], empty_list[1][2])
print(empty_list[2][0], empty_list[2][1], empty_list[2][2])

pick_side = input("O/X? ")
pick_side = pick_side.upper()

i = 0

if pick_side == "O":
    bot_side = "X"
    while i < 5:

        k = 0
        while k < 1:
            user_position = int(input("Enter position! (1 - 9) "))
            if user_position == 1:
                if (empty_list[0][0] is not pick_side) and (empty_list[0][0] is not bot_side):
                    empty_list[0][0] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 2 and (empty_list[0][1] is not bot_side):
                if (empty_list[0][1] is not pick_side) and (empty_list[0][1] is not bot_side):
                    empty_list[0][1] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 3 and (empty_list[0][2] is not bot_side):
                if (empty_list[0][2] is not pick_side) and (empty_list[0][2] is not bot_side):
                    empty_list[0][2] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 4 and (empty_list[1][0] is not bot_side):
                if (empty_list[1][0] is not pick_side) and (empty_list[1][0] is not bot_side):
                    empty_list[1][0] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 5 and (empty_list[1][1] is not bot_side):
                if (empty_list[1][1] is not pick_side) and (empty_list[1][1] is not bot_side):
                    empty_list[1][1] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 6 and (empty_list[1][2] is not bot_side):
                if (empty_list[1][2] is not pick_side) and (empty_list[1][2] is not bot_side):
                    empty_list[1][2] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 7 and (empty_list[2][0] is not bot_side):
                if (empty_list[2][0] is not pick_side) and (empty_list[2][0] is not bot_side):
                    empty_list[2][0] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 8 and (empty_list[2][1] is not bot_side):
                if (empty_list[2][1] is not pick_side) and (empty_list[2][1] is not bot_side):
                    empty_list[2][1] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 9 and (empty_list[2][2] is not bot_side):
                if (empty_list[2][2] is not pick_side) and (empty_list[2][2] is not bot_side):
                    empty_list[2][2] = pick_side
                    k += 1
                else:
                    continue

        j = 0
        while j < 1:
            bot_position = random.randint(1, 9)
            if bot_position == 1:
                if (empty_list[0][0] is not pick_side) and (empty_list[0][0] is not bot_side):
                    empty_list[0][0] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 2:
                if (empty_list[0][1] is not pick_side) and (empty_list[0][1] is not bot_side):
                    empty_list[0][1] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 3:
                if (empty_list[0][2] is not pick_side) and (empty_list[0][2] is not bot_side):
                    empty_list[0][2] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 4:
                if (empty_list[1][0] is not pick_side) and (empty_list[1][0] is not bot_side):
                    empty_list[1][0] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 5:
                if (empty_list[1][1] is not pick_side) and (empty_list[1][1] is not bot_side):
                    empty_list[1][1] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 6:
                if (empty_list[1][2] is not pick_side) and (empty_list[1][2] is not bot_side):
                    empty_list[1][2] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 7:
                if (empty_list[2][0] is not pick_side) and (empty_list[2][0] is not bot_side):
                    empty_list[2][0] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 8:
                if (empty_list[2][1] is not pick_side) and (empty_list[2][1] is not bot_side):
                    empty_list[2][1] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 9:
                if (empty_list[2][2] is not pick_side) and (empty_list[2][2] is not bot_side):
                    empty_list[2][2] = bot_side
                j += 1
            else:
                continue

        print(empty_list[0][0], empty_list[0][1], empty_list[0][2])
        print(empty_list[1][0], empty_list[1][1], empty_list[1][2])
        print(empty_list[2][0], empty_list[2][1], empty_list[2][2])

        if empty_list[0][0] == empty_list[0][1] and empty_list[0][0] == empty_list[0][2]:
            if empty_list[0][0] is pick_side:
                print("You Win! ")
                break
            elif empty_list[0][0] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[1][0] == empty_list[1][1] and empty_list[1][0] == empty_list[1][2]:
            if empty_list[1][0] is pick_side:
                print("You Win! ")
                break
            elif empty_list[1][0] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[2][0] == empty_list[2][1] and empty_list[2][0] == empty_list[2][2]:
            if empty_list[2][0] is pick_side:
                print("You Win! ")
                break
            elif empty_list[2][0] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[0][0] == empty_list[1][0] and empty_list[0][0] == empty_list[2][0]:
            if empty_list[0][0] is pick_side:
                print("You Win! ")
                break
            elif empty_list[0][0] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[0][1] == empty_list[1][1] and empty_list[0][1] == empty_list[2][1]:
            if empty_list[0][1] is pick_side:
                print("You Win! ")
                break
            elif empty_list[0][1] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[0][2] == empty_list[1][2] and empty_list[0][2] == empty_list[2][2]:
            if empty_list[0][2] is pick_side:
                print("You Win! ")
                break
            elif empty_list[0][2] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[0][0] == empty_list[1][1] and empty_list[0][0] == empty_list[2][2]:
            if empty_list[0][0] is pick_side:
                print("You Win! ")
                break
            elif empty_list[0][0] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[0][2] == empty_list[1][1] and empty_list[0][2] == empty_list[2][0]:
            if empty_list[0][2] is pick_side:
                print("You Win! ")
                break
            elif empty_list[0][2] is bot_side:
                print("You Lose! ")
                break
        elif i > 3:
            print("It's a Draw")

        i += 1

elif pick_side == "X":
    bot_side = "O"
    while i < 5:

        k = 0
        while k < 1:
            user_position = int(input("Enter position! (1 - 9) "))
            if user_position == 1:
                if (empty_list[0][0] is not pick_side) and (empty_list[0][0] is not bot_side):
                    empty_list[0][0] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 2 and (empty_list[0][1] is not bot_side):
                if (empty_list[0][1] is not pick_side) and (empty_list[0][1] is not bot_side):
                    empty_list[0][1] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 3 and (empty_list[0][2] is not bot_side):
                if (empty_list[0][2] is not pick_side) and (empty_list[0][2] is not bot_side):
                    empty_list[0][2] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 4 and (empty_list[1][0] is not bot_side):
                if (empty_list[1][0] is not pick_side) and (empty_list[1][0] is not bot_side):
                    empty_list[1][0] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 5 and (empty_list[1][1] is not bot_side):
                if (empty_list[1][1] is not pick_side) and (empty_list[1][1] is not bot_side):
                    empty_list[1][1] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 6 and (empty_list[1][2] is not bot_side):
                if (empty_list[1][2] is not pick_side) and (empty_list[1][2] is not bot_side):
                    empty_list[1][2] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 7 and (empty_list[2][0] is not bot_side):
                if (empty_list[2][0] is not pick_side) and (empty_list[2][0] is not bot_side):
                    empty_list[2][0] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 8 and (empty_list[2][1] is not bot_side):
                if (empty_list[2][1] is not pick_side) and (empty_list[2][1] is not bot_side):
                    empty_list[2][1] = pick_side
                    k += 1
                else:
                    continue
            elif user_position == 9 and (empty_list[2][2] is not bot_side):
                if (empty_list[2][2] is not pick_side) and (empty_list[2][2] is not bot_side):
                    empty_list[2][2] = pick_side
                    k += 1
                else:
                    continue

        j = 0
        while j < 1:
            bot_position = random.randint(1, 9)
            if bot_position == 1:
                if (empty_list[0][0] is not pick_side) and (empty_list[0][0] is not bot_side):
                    empty_list[0][0] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 2:
                if (empty_list[0][1] is not pick_side) and (empty_list[0][1] is not bot_side):
                    empty_list[0][1] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 3:
                if (empty_list[0][2] is not pick_side) and (empty_list[0][2] is not bot_side):
                    empty_list[0][2] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 4:
                if (empty_list[1][0] is not pick_side) and (empty_list[1][0] is not bot_side):
                    empty_list[1][0] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 5:
                if (empty_list[1][1] is not pick_side) and (empty_list[1][1] is not bot_side):
                    empty_list[1][1] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 6:
                if (empty_list[1][2] is not pick_side) and (empty_list[1][2] is not bot_side):
                    empty_list[1][2] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 7:
                if (empty_list[2][0] is not pick_side) and (empty_list[2][0] is not bot_side):
                    empty_list[2][0] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 8:
                if (empty_list[2][1] is not pick_side) and (empty_list[2][1] is not bot_side):
                    empty_list[2][1] = bot_side
                    j += 1
                else:
                    continue
            elif bot_position == 9:
                if (empty_list[2][2] is not pick_side) and (empty_list[2][2] is not bot_side):
                    empty_list[2][2] = bot_side
                j += 1
            else:
                continue

        print(empty_list[0][0], empty_list[0][1], empty_list[0][2])
        print(empty_list[1][0], empty_list[1][1], empty_list[1][2])
        print(empty_list[2][0], empty_list[2][1], empty_list[2][2])

        if empty_list[0][0] == empty_list[0][1] and empty_list[0][0] == empty_list[0][2]:
            if empty_list[0][0] is pick_side:
                print("You Win! ")
                break
            elif empty_list[0][0] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[1][0] == empty_list[1][1] and empty_list[1][0] == empty_list[1][2]:
            if empty_list[1][0] is pick_side:
                print("You Win! ")
                break
            elif empty_list[1][0] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[2][0] == empty_list[2][1] and empty_list[2][0] == empty_list[2][2]:
            if empty_list[2][0] is pick_side:
                print("You Win! ")
                break
            elif empty_list[2][0] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[0][0] == empty_list[1][0] and empty_list[0][0] == empty_list[2][0]:
            if empty_list[0][0] is pick_side:
                print("You Win! ")
                break
            elif empty_list[0][0] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[0][1] == empty_list[1][1] and empty_list[0][1] == empty_list[2][1]:
            if empty_list[0][1] is pick_side:
                print("You Win! ")
                break
            elif empty_list[0][1] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[0][2] == empty_list[1][2] and empty_list[0][2] == empty_list[2][2]:
            if empty_list[0][2] is pick_side:
                print("You Win! ")
                break
            elif empty_list[0][2] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[0][0] == empty_list[1][1] and empty_list[0][0] == empty_list[2][2]:
            if empty_list[0][0] is pick_side:
                print("You Win! ")
                break
            elif empty_list[0][0] is bot_side:
                print("You Lose! ")
                break
        elif empty_list[0][2] == empty_list[1][1] and empty_list[0][2] == empty_list[2][0]:
            if empty_list[0][2] is pick_side:
                print("You Win! ")
                break
            elif empty_list[0][2] is bot_side:
                print("You Lose! ")
                break
        elif i > 3:
            print("It's a Draw")

        i += 1
