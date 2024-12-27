import copy


def binary(n):
    table = [[0 for i in range(n)]]
    no_of_rows = 2**n
    for i in range(1,no_of_rows):
        l = copy.deepcopy(table[i-1])
        for j in range(n-1,-1,-1):
            if(l[j] == 1):
                l[j] = 0
            else:
                l[j] = 1
            if(l not in table):
                table.append(l)
                break
    return table
        
def and_operation(l1,l2):
    n = len(l1)
    l3 = []
    for i in range(n):
        l3.append(l1[i]*l2[i])
    return l3

def or_operation(l1,l2):
    n = len(l1)
    l3 = []
    for i in range(n):
        l3.append(l1[i] + l2[i])
        if(l3[-1] >1):
            l3[-1] = 1
    return l3
    
def cond_operation(l1,l2):
    n = len(l1)
    l3 = []
    for i in range(n):
        if(l1[i] == 1 and l2[i] == 0):
            l3.append(0)
        else:
            l3.append(1)
    return l3
    
def bicond_operation(l1,l2):
    n = len(l1)
    l3 = []
    for i in range(n):
        if(l1[i] == l2[i]):
            l3.append(1)
        else:
            l3.append(0)
    return l3

def not_operation(l1):
    n = len(l1)
    l3 = []
    for i in range(n):
        if(l1[i] == 0):
            l3.append(1)
        else:
            l3.append(0)
    return l3
    
        

def analyse_expression(expr):
    stack = []
    n = len(expr)
    operators = ["~","^","v","->","=>"]
    postfix_expr = []
    #Infix to postfix
    for i in range(n):
        if(expr[i] == "-" or expr[i] == "="):
            cmp = expr[i:i+2]
        elif(expr[i] == ">" ):
            continue
        else:
            cmp = expr[i]
        if(cmp == "("):
            stack.append(cmp)
        elif(cmp in operators):
            if(stack == []):
                stack.append(cmp)
            elif(stack!=[]):
                if(stack[-1] == "("):
                    stack.append(cmp)
                else:
                    val = stack.pop()
                    postfix_expr.append(val)
                    stack.append(cmp)
        elif(cmp == ")"):
            while(True):
                val = stack.pop()
                if(val == '('):
                    break
                else:
                    postfix_expr.append(val)
        else:
            postfix_expr.append(cmp)
    while(stack!=[]):
        postfix_expr.append(stack.pop())
    #print(postfix_expr)
    
    #To find number of operators
    operands = []
    operators_dict = {}
    for i in postfix_expr:
        if(i not in operands and i not in operators):
            operands.append(i)
    no_of_operands = len(operands)
    binary_entries = binary(no_of_operands)
    #print(binary_entries)
    
    #Assigning each operator its truth values
    for i in range(no_of_operands):
        l = []
        for j in range(2**no_of_operands):
            l.append(binary_entries[j][i])
        operators_dict[operands[i]] = l
    
    #Evaluating postfix operation
    stack = []
    no_of_terms = len(postfix_expr)
    for i in range(no_of_terms):
        if(postfix_expr[i] in operators):
            if(postfix_expr[i]!= "~"):
                op1 = stack.pop()
                op2 = stack.pop()
                res = op2 + postfix_expr[i] + op1
                
                if(postfix_expr[i] == "v"):
                    #Or operation
                    result = or_operation(operators_dict[op2],operators_dict[op1])
                elif(postfix_expr[i] == "^"):
                    #And operation
                    result = and_operation(operators_dict[op2],operators_dict[op1])
                elif(postfix_expr[i] == "->"):
                    #Conditional operation
                    result = cond_operation(operators_dict[op2],operators_dict[op1])
                elif(postfix_expr[i] == "=>"):
                    #Biconditional operation
                    result = bicond_operation(operators_dict[op2],operators_dict[op1])
            else:
                res = postfix_expr[i] + postfix_expr[i-1]
                op1 = stack.pop()
                result = not_operation(operators_dict[op1])
            stack.append(res)
            operators_dict[res] = result
                
        else:
            stack.append(postfix_expr[i])
    print(operators_dict[stack[-1]])
    return operators_dict[stack[-1]]

def check_tautology(l1):
    n = len(l1)
    for i in range(n):
        if(l1[i] == 0):
            print("Not a tautology!")
            return
    else:
        print("It is a tautology!")
        
    
choice = int(input("1. Tautology? 2. Equivalent expressions?: "))
if(choice == 1):
    expr = input("Enter expression: ")
    result = analyse_expression(expr)
    check_tautology(result)
else:
    expr1 = input("Enter expression 1: ")
    expr2 = input("Enter expression 2: ")
    res1 = analyse_expression(expr1)
    res2 = analyse_expression(expr2)
    if(res1 == res2):
        print("Euivalent expressions!")
    else:
        print("They are not equivalent")

