#python: Game Tec Tac Tao Number

import random

#The Game Board


board = [0,0,0,0,0,0,0,0,0]
arr= [0,1,2,3,4,5,6,7,8]
def show ():
    print( board[0],'|',board[1],'|',board [2])
    print ('-----------')
    print (board[3],'|',board[4],'|',board [5])
    print ('-----------')
    print (board[6],'|',board[7],'|',board [8])
    
show()

def checkLine(char, spot1,spot2,spot3):
    if board[spot1]==char and board [spot2]==char and board [spot3]==shar:
        return True

p1 = [1,3,5,7,9]
p2 = [0,2,4,6,8]
 

while True :

    indx = int(input("select an index: "))
    print(p1)

    while ( True ):
        if ( board[indx] != 0):
            print("error")
            indx = int(input("select an index: "))
        else:
            break
        
    xx = int(input("select a number: "))
    while(xx not in p1):
        xx = int(input("re-enter a number: "))
        
    
    
    board[indx] = xx
    p1.remove(xx)
    show()
    
    
    indx = int(input("select an index"))
    print(p2)
    while ( True ):
        if (board[indx] != 0):
            print("error")
            indx = int(input("select an index: "))
        else:
            break
        
    xx = int(input("select a number"))
    while(xx not in p2):
        xx = int(input("select a number"))

    
        
    board[indx] = xx
    p2.remove(xx)
    show()


    if ( board[0] + board[1] + board[2] == 15 ):
        print("winner")
        break

    if ( board[3] + board[4] + board[5] == 15 ):
        print("winner")
        break
    if ( board[6] + board[7] + board[8] == 15 ):
        print("winner")
        break
    if ( board[0] + board[4] + board[8] == 15 ):
        print("winner")
        break
    if ( board[2] + board[4] + board[6] == 15 ):
        print("winner")
        break
    if ( board[0] + board[3] + board[6] == 15 ):
        print("winner")
        break
    if ( board[1] + board[4] + board[7] == 15 ):
        print("winner")
        break
    if ( board[2] + board[5] + board[8] == 15 ):
        print("winner")
        break

