import copy

def astar(adj_matrix,states,state,goal_state,path_cost,active_nodes,heuristic,path):
    if(state in active_nodes):
        del active_nodes[state]
    if(state == goal_state):
        return path[state]
    n = len(states)
    for i in range(state+1,n):
        if(adj_matrix[state][i] != 999): #neighbour
            new_path = copy.deepcopy(path[state])
            new_path.append(i)
            if i not in active_nodes:
                active_nodes[i] = adj_matrix[state][i] + path_cost
                path[i] = new_path
            else:
                if(adj_matrix[state][i] + path_cost < active_nodes[i]):
                    active_nodes[i] = adj_matrix[state][i] + path_cost
                    path[i] = new_path
    #For debugging purposes and for better understanding thee print statements are included
    print("After state:",state)
    print("Active nodes:",active_nodes)
    min_value = 999
    for i in active_nodes:
        if(active_nodes[i] + heuristic[i] < min_value):
            min_value = active_nodes[i] + heuristic[i]
            min_node = i
    return astar(adj_matrix,states,min_node,goal_state,min_value - heuristic[min_node],active_nodes,heuristic,path)
            
def find_cost(adj_matrix,path):
    n = len(path)
    cost = 0
    for i in range(n-1):
        cost += adj_matrix[path[i]][path[i+1]]
    return cost
        



states = ["S","A","B","C","D","G"]

adj_matrix = [[0,1,999,999,999,10],[1,0,2,1,999,999],[999,2,0,999,5,999],[999,1,999,0,3,4],[999,999,5,3,0,2],[10,999,999,4,2,0]]

start_state = 0 #S
goal_state = 5 #G

heuristic = [5,3,4,2,6,0]

path = astar(adj_matrix,states,start_state,goal_state,0,{},heuristic,{0:[0]})
#Displaying path
print("Optimal path:")
for i in path:
    print(states[i],end = " -> ")
print("\nPath cost =",find_cost(adj_matrix,path))
