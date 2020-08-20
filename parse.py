import json
import re
# import sympy
from sympy import symbols, Eq, solve

a=[]

def prettify(argument):
    if(argument == 'equal'):
        return '='
    elif (argument == 'add'):
        return '+'
    elif (argument == 'subtract'):
        return '-'
    elif (argument == 'multiply'):
        return '*'
    elif (argument == 'divide'):
        return '/'
    else:
        return argument

def isOperator(args):
    # l = []
    # print(args)
    # l=['+','-','*','/','=']
    if (args == '+' or args == '-' or args == '*' or args == '/' or args =='='):
        return True
    else:
        return False

    # if(args in l):
    #     return True
    # else:
    #     # print(args)
    #     return False

def changeOperator(args):
    if '+' == args:
        return '-'
    elif '-' == args:
        return '+'
    elif '*' == args:
        return '/'
    elif '/' == args:
        return '*'
    else:
        return args

        
def preToInfix(expression):
    s = []
    length=len(expression)
    # print(expression)
    for i in range(length-1,-1,-1):
        # print(i)
        if(isOperator(expression[i])):
            op1=s[len(s)-1]
            s.pop()
            op2=s[len(s)-1]
            s.pop()
            temp = ''
            if(i<=1):
                temp = str(op1) + ' ' + str(expression[i]) + ' ' + str(op2)
                # print(temp)
            else:
                temp = '('+ str(op1) + ' ' + str(expression[i]) + ' ' + str(op2) + ')'
                # print(temp)

            # print(temp)
            s.append(temp)
            
        else:
            # print(expression[i])
            s.append(expression[i])
    # print(s)
    return s[len(s)-1]

def sol(rhs,exp):
    s = []
    exp = list(re.sub('x|[()]|\s', ' ', exp).split(' '))
    exp = [i for i in exp if i]
    print(exp)
    count  = 0
    length = len(exp)
    # print(length)
    # print(exp[1])
    if(length>3):
        for i in range(1,length):
            if (isOperator(exp[i]) and isOperator(exp[i+1])):
                s.append(changeOperator(exp[i])+exp[i-1]+')'+changeOperator(exp[i+1]))
                # print(s)
                # print(i)
                i = i +1

                print(exp[i],exp[i+1])  
            elif(isOperator(exp[i])):
                count = count +1
                # print(type(exp[i]))
                # i = i -1
                # print(exp[i])
                s.append(changeOperator(exp[i])+exp[i-1])
                # i = i+1
                # print(i)
                # print(s)
                # i = i+1
            else:
                # i = i-1
                s.append(exp[i])
                # print(i)
        print(count)
        # print('(' + rhs + "".join(s))
        return '(' + rhs + ''.join(s)

    # print(rhs+exp.slice(0,len(exp)-1))
    return rhs+exp[slice(0,len(exp)-1)]
    

    

def rec(obj):
    global a
    for key in obj:
        # print(key)
        if ((type(obj[key]) is not str) and (obj[key] is not None) ):
            if(type(obj[key]) is int ):
                a.append(prettify(obj[key]))
            else:
                rec(obj[key])
        else:
            a.append(prettify(obj[key]))
    return a

# def solve_linear_equation ( equ ):
#     match = re.match(r"(\d+)x\+(\d+)=(\d+)", equ)
#     m, c, y = match.groups()
#     m, c, y = float(m), float(c), float(y) # Convert from strings to numbers
#     x = (y-c)/m
#     print ("x = %f" % x)

with open('test.json') as f:
  data = json.load(f)
# print(data)
# print(json.dumps(data, indent = 4, sort_keys=True))
test = rec(data)

# print(test)
expression = preToInfix(test)
print(expression)

lhs = expression.split('=')[0]
# print(lhs)
rhs = expression.split('=')[1].strip()
# print(rhs)
value=sol(rhs,lhs)

print(value)
# a = sympy.Eq((21-1)/10,0)
# print(a)
# print(sympy.solve((21-1)/10))
# solve_linear_equation()

# equ=get(handles.edit1,value);
# x = symbols('x')
# eq1 = Eq(expression)