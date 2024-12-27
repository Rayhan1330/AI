import copy

def generate():
    goal = [0,0]
    tree = [[0,0]]
    action = ["Initial",]
    i = 0
    while(True):
        prev = tree[i]
        if(prev == None):
            tree.append(None)
            tree.append(None)
            action.append(None)
            action.append(None)
            i += 1
            continue
        if(prev[0] == 2):
            break
        curr = copy.deepcopy(prev)
        if(prev[0] != 4 or prev[1] != 3): #one of em isnt full
            if(prev[0] != 4):
                curr[0] = 4
                if(curr not in tree):
                    tree.append(curr)
                    action.append("Fill Jug 1")
                curr = copy.deepcopy(prev)
                if(curr[1]): #jug2 aint empty
                    if(curr[0] == 0):
                        curr[0] = curr[1]
                        curr[1] = 0
                    else:
                        curr[0] = curr[0] + curr[1]
                        k = 0
                        if(curr[0] > 4):
                            k = curr[0] - 4
                            curr[0] = 4
                        curr[1] = k
                    if(curr not in tree):
                        tree.append(curr)
                        action.append("Transfer content from Jug 2 to Jug 1")
                    curr = copy.deepcopy(prev)
            if(prev[1] != 3):
                curr[1] = 3
                if(curr not in tree):
                    tree.append(curr)
                    action.append("Fill Jug 2")
                curr = copy.deepcopy(prev)
                if(curr[0]): #jug1 aint empty
                    if(curr[1] == 0):
                        if(curr[0] == 4):
                            curr[1] = 3
                            curr[0] = 1
                        else:
                            curr[1] = curr[0]
                            curr[0] = 0
                    else:
                        curr[1] = curr[0] + curr[1]
                        k = 0
                        if(curr[1] > 3):
                            k = curr[1] - 3
                            curr[1] = 3
                        curr[0] = k
                    if(curr not in tree):
                        tree.append(curr)
                        action.append("Transfer content from Jug 1 to Jug 2")
                    curr = copy.deepcopy(prev)
        if(prev[0] != 0 or prev[1] != 0):
            if(prev[0] != 0):
                curr[0] = 0
                if(curr not in tree):
                    tree.append(curr)
                    action.append("Empty Jug 1")
                curr = copy.deepcopy(prev)
            if(prev[1] != 0):
                curr[1] = 0
                if(curr not in tree):
                    tree.append(curr)
                    action.append("Empty Jug 2")
                curr = copy.deepcopy(prev)
            
        n = len(tree)
        if(2*i + 1 >= n):
            tree.append(None)
            action.append(None)
        n = len(tree)
        if(2*(i+1) >= n):
            tree.append(None)
            action.append(None)
        i += 1
    return tree,action


def dfs(tree,state):
    print("\nDFS Search\n")
    stack = [0,]
    n = len(tree)
    cost = 0
    while(stack != []):
        cost += 1
        i = stack.pop()
        print(action[i])
        print(tree[i])
        if(tree[i][0] == 2):
            break
        try:
            if(tree[2 * (i + 1)] != None):
                stack.append(2*(i+1))
        except:
            pass
        try:
            if(tree[2*i + 1] != None):
                stack.append(2*i + 1)
        except:
            pass
        print("\n")
    return cost
        
def bfs(tree,state):
    queue = [0,]
    cost = 0
    while(queue != []):
        cost += 1
        i = queue.pop(0)
        print(action[i])
        print(tree[i])
        if(tree[i][0] == 2):
            break
        try:
            if(tree[2*i + 1] != None):
                queue.append(2*i + 1)
        except:
            pass
        try:
            if(tree[2*(i + 1)] != None):
                queue.append(2*(i + 1))
        except:
            pass
        print("\n")
    return cost
    
def dls(tree,action,depth):
    print("\nDLS Search\n")
    stack = [(0,0)]
    n = len(tree)
    cost = 0
    while(stack != []):
        cost += 1
        i,j = stack.pop()
        print(action[i])
        print(tree[i])
        if(tree[i][0] == 2):
            break
        try:
            if(tree[2 * (i + 1)] != None and j != depth):
                stack.append((2*(i+1),j+1))
        except:
            pass
        try:
            if(tree[2*i + 1] != None and j != depth):
                stack.append((2*i + 1,j+1))
        except:
            pass
        print("\n")
    else:
        return -1
    return cost
    
def ids(tree,action,depth):
    for i in range(1,depth+1):
        cost = dls(tree,action,i)
        if(cost == -1):
            print("Solution not found at depth:",i)
        else:
            print("Solution found at depth:",i)
            return cost
    else:
        return -1
    
        

if __name__ == '__main__':
    tree,action = generate()
    cost = 0
    print("Enter 1 for DFS\n2 for BFS\n3 for DLS\n4 for IDS")
    choice = int(input("Enter: "))
    if(choice == 1):
        cost = dfs(tree,action)
    elif(choice == 2):
        cost = bfs(tree,action)
    elif(choice == 3):
        depth = int(input("Enter depth limit: "))
        cost = dls(tree,action,depth)
    elif(choice == 4):
        depth = int(input("Enter max depth: "))
        cost = ids(tree,action,depth)
    if(cost == -1):
        print("Goal state not found!")
    else:
        print("Cost is:",cost)
