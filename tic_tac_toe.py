
answer1 = '1'
answer2 = '2'
answer3 = '3'
answer4 = '4'
answer5 = '5'
answer6 = '6'
answer7 = '7'
answer8 = '8'
answer9 = '9'


def game(a):

    global in_session
    global answer1
    global answer2
    global answer3
    global answer4
    global answer5
    global answer6
    global answer7
    global answer8
    global answer9

    if a == '1':
        answer1 = player
    if a == '2':
        answer2 = player
    if a == '3':
        answer3 = player
    if a == '4':
        answer4 = player
    if a == '5':
        answer5 = player
    if a == '6':
        answer6 = player
    if a == '7':
        answer7 = player
    if a == '8':
        answer8 = player
    if a == '9':
        answer9 = player

    if (answer7 == answer8 == answer9) or (answer4 == answer5 == answer6) or (answer1 == answer2 == answer3):
        print(tally())
        print(f"{player} Player Wins!")
        in_session = False

    if (answer1 == answer4 == answer7) or (answer2 == answer5 == answer8) or (answer3 == answer6 == answer9):
        print(tally())
        print(f"{player} Player Wins!")
        in_session = False

    if (answer1 == answer5 == answer9) or (answer3 == answer5 == answer7):
        print(tally())
        print(f"{player} Player Wins!")
        in_session = False

    tally_list = [answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9]

    tie_test = 0

    for i in tally_list:
        if i == 'X' or i == 'O':
            tie_test += 1
        if tie_test == 9:
            print("TIE!!!!!!!!!!!!")
            in_session = False


def tally():

    global in_session
    global answer1
    global answer2
    global answer3
    global answer4
    global answer5
    global answer6
    global answer7
    global answer8
    global answer9

    graphic = {1: f"   {answer7}   '   {answer8}   '   {answer9}   ",
               2: f"   {answer4}   '   {answer5}   '   {answer6}   ",
               3: f"   {answer1}   '   {answer2}   '   {answer3}   ",
               4: f"       '       '      ",
               0: '- - - - - - - - - - - -'}

    board = [4, 1, 4, 0, 4, 2, 4, 0, 4, 3, 4]

    for i in board:
        print(graphic[i])


def session():

    global in_session
    global player
    global player1
    global player2
    global a
    in_session = True

    player1 = ''
    player2 = ''
    choice = input("Player One, Please choose 'X' or 'O'")
    choice = choice.upper()
    if choice == 'X':
        player1 = 'X'
        player2 = 'O'
        print("Player One is 'X', Player Two is 'O!!!")
    elif choice == 'O':
        player1 = '0'
        player2 = 'X'
        print("Player One is 'O', Player Two is 'X'")
    else:
        print('Invalid Entry')
        in_session = False

    while in_session:
        print(tally())
        player = player1
        a = input('Player One, Choose!!!')
        game(a)

        while in_session:
            print(tally())
            player = player2
            a = input('Player Two, Choose!!!')
            game(a)

            break


session()

while not in_session:
    answer1 = '1'
    answer2 = '2'
    answer3 = '3'
    answer4 = '4'
    answer5 = '5'
    answer6 = '6'
    answer7 = '7'
    answer8 = '8'
    answer9 = '9'

    question = input("Would You Like to Play Again?(Y/N)")
    question = question.lower()
    if question == 'y':
        session()
        continue
    else:
        print("Game Over")
        break


