import copy

#Finding parents
def find_parents(adj_matrix,node):
    parents = []
    n = len(adj_matrix)
    for i in range(n):
        if(adj_matrix[i][node] == 1):
            parents.append(i)
    return parents

#To generate binary entries
def binary(n):
    no_of_rows = 2**n
    no_of_columns = n
    table = [[0 for i in range(n)]]
    for i in range(1,no_of_rows):
        l = []
        l = copy.deepcopy(table[i-1])
        for j in range(n-1,-1,-1):
            if(l[j] == 0):
                l[j] = 1
            else:
                l[j] = 0
            if(l not in table):
                table.append(l)
                break
    '''for i in range(no_of_rows):
        print(table[i])'''
    return table
                
            
    
#To get the input probabilities
def get_input_probabilities(adj_matrix,nodes):
    n = len(nodes)
    prob = {}
    for i in range(n):
        parents = find_parents(adj_matrix,i)
        no_of_parents = len(parents)
        if(parents == []):
            print(f"Node {nodes[i]} has no dependancies")
        else:
            print(f"Node {nodes[i]} has {no_of_parents} dependancies")
        no_of_rows = 2**no_of_parents
        no_of_columns = 2
        binary_entries = binary(no_of_parents)
        states = [False,True]
        prob_dist = []
        for j in range(no_of_rows):
            l = []
            print("\nEnter probability given: ")
            for k in range(no_of_parents):
                print(f"{nodes[parents[k]]} is {states[binary_entries[j][k]]}", end = ",")
            false = float(input("\nEnter false value: "))
            l.append(false)
            truth = float(input("Enter truth value: "))
            l.append(truth)
            prob_dist.append(l)
        print("\n")
        prob[i] = prob_dist
    return prob
 
def convert_binary_to_int(list_of_values):
    n = len(list_of_values)
    binary_entries = binary(n)
    for i in range(2**n):
        if(binary_entries[i] == list_of_values):
            return i
            
#Calculating joint probability distribution
def calculate_probability(prob,conditions,graph):
    n = len(graph)
    prod = 1
    for i in range(n):
        parents = find_parents(graph,i)
        no_of_parents = len(parents)
        if(no_of_parents == 0):
            prod *= prob[i][0][conditions[i]]
        else:
            l = []
            for j in parents:
                l.append(conditions[j])
            integer_value = convert_binary_to_int(l)
            prod *= prob[i][integer_value][conditions[i]]
    return prod
            

#Getting input values

#Creating the graph
n = int(input("Enter the number of nodes/states: "))
nodes = []
binary(n)

#Using an adjacency matrix to represent the graph
adj_matrix = []
for i in range(n):
    l = []
    for j in range(n):
        if(i == j):
            l.append(0)
        else:
            l.append(999)
    adj_matrix.append(l)
print("\n")
for i in range(n):
    s = input(f"Enter label for node {i}: ")
    nodes.append(s)

for i in range(n):
    print("\n")
    for j in range(n):
        if(i == j):
            continue
        choice = input(f"Does {nodes[i]} determine {nodes[j]}? (Y/N): ")
        if(choice == 'Y'):
            adj_matrix[i][j] = 1

print("\n")
prob = get_input_probabilities(adj_matrix,nodes)

print("Calculating Join Probability:")
conditions = []
for i in range(n):
    s = input(f"Is {nodes[i]} true?(Y/N): ")
    if(s == 'Y'):
        conditions.append(1)
    else:
        conditions.append(0)
        
print("Joint probability is:",calculate_probability(prob,conditions,adj_matrix))




