import sys

game, nums, checker, last_placement, last_letter, stop, p_win, s1, s2, s3, s4 = [], [], [], 0, "", 1, False, 0, 0, 0, 0
w_value = 0

for f in range(1, 17):
    nums.append(' ')
    if len(str(f)) == 1:
        nums.append(" " + str(f) + " ")
    else:
        nums.append(" " + str(f))


def check_for_possible_wins():
    global p_win, s1, s2, s3, w_value
    check_for_win = []
    for i in game[1::2]:
        if i.isspace():
            check_for_win.append(" ")
        elif not i.isspace():
            for j in i:
                if j == ' ':
                    j = ''
                check_for_win.append(j)
    check_for_win = list(''.join(check_for_win))
    for i in range(len(check_for_win) - 2):
        s1 = check_for_win[i]
        s2 = check_for_win[i + 1]
        s3 = check_for_win[i + 2]
        if (s1 == "S" and s2 == " " and s3 == "S") or (s1 == " " and s2 == "O" and s3 == "S") or (
                s1 == "S" and s2 == "O" and s3 == " "):
            p_win = True
            if s1 == " ":
                w_value = i + 1
                return i + 1
            elif s2 == " ":
                w_value = i + 1 + 1
                return i + 1 + 1
            elif s3 == " ":
                w_value = i + 2 + 1
                return i + 2 + 1


for _ in range(16):
    game.append("∣")
    game.append("   ")
game.append("∣")
print(''.join(game))
print(''.join(nums))


def out_of_range(ind):
    if not 1 <= ind <= 16:
        return True
    return False


def check_if_placement_used(index):
    try:
        if game[index].isspace():
            return False
        return True
    except:
        return True


def check_if_game_is_done():
    global p_win
    for i in game[1::2]:
        if i.isspace():
            checker.append(" ")
        elif not i.isspace():
            for j in i:
                if j == ' ':
                    j = ''
                checker.append(j)
    if "SOS" in ''.join(checker).strip():
        checker.clear()
        return True
    checker.clear()
    return False


class Filler:
    def __init__(self):
        self.placement = int(input("placement : "))
        self.letter = input("S,O : ")

    def filling(self):
        global last_placement, last_letter
        if out_of_range(self.placement):
            print("Out of Range!")
            return Filler().filling()
        if check_if_placement_used(2 * self.placement - 1):
            print("Place already used!")
            return Filler().filling()
        if self.letter.lower() != "s" and self.letter.lower() != "o":
            print("Please Choose 'S' or 'O' !")
            return Filler().filling()
        game[2 * self.placement - 1] = ' ' + self.letter.upper() + ' '
        print(''.join(game))
        print(''.join(nums))
        last_placement = self.placement
        last_letter = self.letter


Filler().filling()
#      CASE 1     #
if last_letter.lower() == "s":  # if player1 started with S
    if not (out_of_range(2 * last_placement + 5) or check_if_placement_used(2 * last_placement + 5)):  # take his S+3
        game[2 * last_placement + 5] = " S "
        print("\n" + ''.join(game))
        print(''.join(nums))


    else:  # if S+3 is not empty take S-3
        game[2 * last_placement - 7] = " S "
        print("\n" + ''.join(game))
        print(''.join(nums))

if last_letter.lower() == "o":  # if player 1 started with O
    if last_placement >= 9:  # perfect S
        game[2 * (last_placement - 5) - 1] = " S "
        ps = 2 * (last_placement - 5) - 1
        print("\n" + ''.join(game))
        print(''.join(nums))
        Filler().filling()
        check_for_possible_wins()
        # check if he blundered #
        if p_win:
            if s2 == " ":
                game[2 * w_value - 1] = " O "
                print(f"\nPC chose placement {w_value} and letter O\n")
                print("\n" + ''.join(game))
                print(''.join(nums))
                if check_if_game_is_done():
                    print('You Lost!')
                    sys.exit()
            else:
                game[2 * w_value - 1] = " S "
                print(f"\nPC chose placement {w_value} and letter S\n")
                print("\n" + ''.join(game))
                print(''.join(nums))
                if check_if_game_is_done():
                    print('You Lost!')
                    sys.exit()
            # end of checking for blunders
            # if he didn't blunder check for your last perfectS + 3 #
        if not check_if_placement_used(ps + 6):  # second S
            game[ps + 6] = " S "
            check_for_possible_wins()
            if p_win:  # if it's a blunder, play perfectS -3 instead
                game[ps + 6] = "   "
                game[ps - 6] = " S "
                print("\n" + ''.join(game))
                print(''.join(nums))
            else:  # if it's not a blunder play it
                print("\n" + ''.join(game))
                print(''.join(nums))

        else:  # if S+3 is not available go for S-3 #
            game[ps - 6] = " S "
            check_for_possible_wins()
            if p_win:  # if it's a blunder go for S+3 instead
                game[ps - 6] = "   "
                game[ps + 6] = " S "
                print("\n" + ''.join(game))
                print(''.join(nums))
            else:  # if it's not a blunder play it
                print("\n" + ''.join(game))
                print(''.join(nums))

        #      CASE 2        #
    elif last_placement <= 8:  # (case 2)
        game[2 * last_placement + 9] = " S "  # perfect S
        print("\n" + ''.join(game))
        print(''.join(nums))
        ps = 2 * last_placement + 9

        Filler().filling()
        check_for_possible_wins()
        if p_win:
            if s2 == " ":
                game[2 * w_value - 1] = " O "
                print(f"\nPC chose placement {w_value} and letter O\n")
                print("\n" + ''.join(game))
                print(''.join(nums))
                if check_if_game_is_done():
                    print('You Lost!')
                    sys.exit()
            else:
                game[2 * w_value - 1] = " S "
                print(f"\nPC chose placement {w_value} and letter S\n")
                print("\n" + ''.join(game))
                print(''.join(nums))
                if check_if_game_is_done():
                    print('You Lost!')
                    sys.exit()

        if not check_if_placement_used(ps + 6):  # SECOND S FOR CASE 2 (perfectS + 3)
            game[ps + 6] = " S "
            check_for_possible_wins()
            if p_win:
                game[ps + 6] = "   "
                game[ps - 6] = " S "
                print("\n" + ''.join(game))
                print(''.join(nums))
            else:
                print("\n" + ''.join(game))
                print(''.join(nums))
        else:
            game[ps - 6] = " S "
            check_for_possible_wins()
            if p_win:
                game[ps - 6] = "   "
                game[ps + 6] = " S "
                print("\n" + ''.join(game))
                print(''.join(nums))

        #########################################

while not check_if_game_is_done():
    Filler().filling()
    check_for_possible_wins()
    if p_win:
        if s2 == " ":
            game[2 * w_value - 1] = " O "
            print(f"\nPC chose placement {w_value} and letter O\n")
            print("\n" + ''.join(game))
            print(''.join(nums))
            if check_if_game_is_done():
                print('You Lost!')
                sys.exit()
        else:
            game[2 * w_value - 1] = " S "
            print(f"\nPC chose placement {w_value} and letter S\n")
            print("\n" + ''.join(game))
            print(''.join(nums))
            if check_if_game_is_done():
                print('You Lost!')
                sys.exit()

    for spot in range(33):  # main BOT
        if game[spot].isspace():  # only if it's empty
            game[spot] = " S "
            check_for_possible_wins()
            if p_win:
                game[spot] = " O "
                p_win = False
                check_for_possible_wins()
                if p_win:
                    game[spot] = "   "
                    p_win = False
                else:
                    print("\n" + ''.join(game))
                    print(''.join(nums))
                    break
            else:
                print("\n" + ''.join(game))
                print(''.join(nums))
                break

print("You Lost!")
