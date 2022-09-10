# Tic Tac Toe game in python

board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

print('Welcome to Tic Tac Toe!')



def player1Move():

    run = True

    while run:

        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
def player2Move():

    run = True
    while run:
        move = input('Please select a position to place an \'O\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('O', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]




def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            player1Move()
            printBoard(board)
        else:
            print(pl,'won this time,Congratulations!')
            break

        if not (isWinner(board, 'X')):
            move = player2Move()
            if move == 0:
                print('Tie Game!')
            else:
            #     insertLetter('O', move)
            #     print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print(p,'won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

def main2():
    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            player1Move()
            printBoard(board)
        else:
            print('Sorry,computer won this time!')
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('You have won this time! Good Job!')
            break

while True:
    answer = input('How do you wish to play this game, '
                   'With computer or friend?(C/F)')
    if answer.lower() == 'c' or answer.lower == 'computer':
        board = [' ' for x in range(10)]
        main2()
        break

    else:
        p=input("PLAYER 1 name:")
        pl=input("PLAYER 2 name:")
        main()
        break
    # if isBoardFull(board):
    #     print('Tie Game!')


while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break