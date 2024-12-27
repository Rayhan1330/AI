def greedy_bfs(adj_matrix,states,state,goal_state,heuristic,path):
    path.append(state)
    if(state == goal_state):
        return path
    min = 999
    n = len(states)
    for i in range(state,n):
        if(adj_matrix[state][i] !=0 and adj_matrix[state][i] < 999):
            if(heuristic[i] < min):
                min = heuristic[i]
                min_state = i
    #path_cost += min
    return greedy_bfs(adj_matrix,states,min_state,goal_state,heuristic,path)
 


def find_cost(adj_matrix,path):
    n = len(path)
    path_cost = 0
    for i in range(n-1):
        path_cost += adj_matrix[path[i]][path[i+1]]
    return path_cost
     

'''states = ["S","A","B","C","D","E","F","G","H","I"]
adj_matrix = [[0,3,2,999,999,999,999,999,999,999],[3,0,999,4,1,999,999,999,999,999],[2,999,0,999,999,3,1,999,999,999],[999,4,999,0,999,999,999,999,999,999],[999,1,999,999,0,999,999,999,999,999],[999,999,3,999,999,0,999,999,5,999],[999,999,1,999,999,999,0,3,999,2],[999,999,999,999,999,999,3,0,999,999],[999,999,999,999,999,5,999,999,0,999],[999,999,999,999,999,999,2,999,999,0]]
heuristic = [13,12,4,7,3,8,2,0,4,9]

start_state = 0 #S
goal_state = 7 #G'''

states = ["S","A","B","C","D","G"]

adj_matrix = [[0,1,999,999,999,10],[1,0,2,1,999,999],[999,2,0,999,5,999],[999,1,999,0,3,4],[999,999,5,3,0,2],[10,999,999,4,2,0]]

start_state = 0 #S
goal_state = 5 #G

heuristic = [5,3,4,2,6,0]

path = greedy_bfs(adj_matrix,states,start_state,goal_state,heuristic,[])

print("Path:")
for i in path:
    print(states[i],end = " -> ")
print("\n")
print("Path cost:",find_cost(adj_matrix,path))



