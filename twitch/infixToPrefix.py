import sys


#operations and their precedence
#parens precedence can be removed with special casing on the operator stack
ops = set(["+","-","*","/"])
preced = dict({ "+": 0, "-": 0, "*": 1, "/": 1, "(": -1})

def infixToPrefix(tokens, flags):

    def isInt(numString):
        #possibly use isinstance(val,type) instead of a try-catch
        try:
            int(numString)
            return True
        except ValueError:
            return False

    def evalExp(operator, operandLeft, operandRight):
        #evaluates if -r, otherwise, leaves unevaluated
        #only evaluates if both operands are numbers
        operand = '( ' + operator + ' ' + operandLeft + ' ' + operandRight + ' )'
        if flags == '-r':
            if isInt(operandLeft) and isInt(operandRight):
                if operator == '+':
                    operand = str(int(operandLeft) + int(operandRight))
                elif operator == '-':
                    operand = str(int(operandLeft) - int(operandRight))
                elif operator == '*':
                    operand = str(int(operandLeft) * int(operandRight))
                elif operator == '/':
                    operand = str(int(operandLeft) / int(operandRight))
        return operand

    operandStack = []
    operatorStack = []

    for item in tokens:
        #check if operand
        if item not in ops and item != '(' and item != ')':
            operandStack.append(item)
        
        elif item == ')':
            #on finding close parens, evaluate everything enclosed
            #can break if there is no open parens to be found**bad expression
            while operatorStack[-1] != '(':
                operator = operatorStack.pop()
                operandRight = operandStack.pop()
                operandLeft = operandStack.pop()
                operand = evalExp(operator, operandLeft, operandRight)
                operandStack.append(operand)

            operator = operatorStack.pop()

        elif item == '(' or len(operatorStack) == 0 or preced[item] > preced[operatorStack[-1]]:
            #if open parens, empty stack, or higher precedence than top of stack, put on top of stack
            operatorStack.append(item)


        elif preced[item] <= preced[operatorStack[-1]]:
            #if lower priority than top of stack, evaluate off top of stack til lower precedence
            while len(operatorStack) > 0 and preced[item] <= preced[operatorStack[-1]]:
                operator = operatorStack.pop()
                operandRight = operandStack.pop()
                operandLeft = operandStack.pop()
                operand = evalExp(operator, operandLeft, operandRight)
                operandStack.append(operand)

            operatorStack.append(item)

    #if stack not empty yet
    while len(operatorStack) > 0:
        operator = operatorStack.pop()
        operandRight = operandStack.pop()
        operandLeft = operandStack.pop()
        operand = evalExp(operator, operandLeft, operandRight)
        operandStack.append(operand) 
        
    print operandStack[-1]
    #print for console checking
    return operandStack[-1]
    operandStack.pop()     



if len(sys.argv) < 2:
    print "no file specified"
elif len(sys.argv) > 3:
    print "too many arguments"
else:
    filename = sys.argv[1]
    flags = ''
    if len(sys.argv) == 3:
        flags = sys.argv[2]
    f = open(filename, 'r+')
    lines = f.readlines()
    f.close()
    #resets prefix file
    f = open('prefix', 'w')
    f.write('')
    f.close()
    f = open('prefix', 'a')
    for line in lines:
        line = line.replace('\n','')
        f.write(infixToPrefix(line.split(' '), flags) + '\n')
    f.close()