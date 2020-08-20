import json
import re

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

    l=['+','-','*','/','=']

    if(args in l):
        return True
    else:
        return False

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
    for i in range(length-1,-1,-1):
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

            s.append(temp)
            
        else:
            s.append(expression[i])
    # print(s)
    return s[len(s)-1]

def sol(rhs,exp):
    s = []
    exp = list(re.sub('x|[()]|\s', ' ', exp).split(' '))
    exp = [i for i in exp if i]

    count  = 0
    length = len(exp)

    if(length>3):
        i=1
        while(i<length):
            if (isOperator(exp[i]) and isOperator(exp[i+1])):
                s.append(changeOperator(exp[i])+exp[i-1]+')'+changeOperator(exp[i+1]))
                i= i+1
            elif(isOperator(exp[i])):
                s.append(changeOperator(exp[i])+exp[i-1])
            else:
                s.append(exp[i])
            i=i+1

        return '(' + rhs + ''.join(s)

    return rhs+exp[slice(0,len(exp)-1)]
    

    

def rec(obj):
    global a
    for key in obj:
        if ((type(obj[key]) is not str) and (obj[key] is not None) ):
            if(type(obj[key]) is int ):
                a.append(prettify(obj[key]))
            else:
                rec(obj[key])
        else:
            a.append(prettify(obj[key]))
    return a


with open('test.json') as f:
  data = json.load(f)

# print(json.dumps(data, indent = 4, sort_keys=True))
test = rec(data)

# print(test)
expression = preToInfix(test)
# print(expression)

lhs = expression.split('=')[0]
# print(lhs)
rhs = expression.split('=')[1].strip()
# print(rhs)
value=sol(rhs,lhs)

print('x = ',value)
print('x = ',eval(value))
