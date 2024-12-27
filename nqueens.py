import copy
import random

def init(n):
    board = [random.randint(0,n-1) for _ in range(n)]
    return board
    
def calculate_attacks(board,n):
    no_of_atks = 0
    for i in range(n):
        for j in range(i+1,n):
            if(board[i] == board[j] or abs(board[i] - board[j]) == (j-i)):
                no_of_atks += 1
    return no_of_atks
    
    
def display(board,n):
    for i in range(n):
        for j in range(n):
            if(board[i] == j):
                print("Q |",end = " ")
            else:
                print(" |",end = " ")
        print("\n")
                
def generate_state(board,n):
    current_state = copy.deepcopy(board)
    print("Board",board)
    for i in range(1000):
        best_state = current_state
        if(calculate_attacks(current_state,n) == 0):
            print("Optimal state found!")
            break
        for j in range(n):
            for k in range(n):
                temp = copy.deepcopy(current_state)
                if(temp[j] == k):
                    continue
                temp[j] = k
                if(calculate_attacks(temp,n) < calculate_attacks(best_state,n)):
                    best_state = temp
        if(best_state == current_state):
            print("\nStuck in a local minimum, restart")
            display(best_state,n)
            current_state = init(n)
        else:
            current_state = best_state
    else:
        print("Optimal state not found!")
    return current_state
            

#display(generate_state([1,3,0,2],4),4)
display(generate_state(init(5),5),5)
