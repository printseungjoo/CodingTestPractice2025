while(True):
    essay = input()
    stack = []
    forTF = True
    if(essay == '.'):
        break
    for w in essay:
        if(w == '(' or w == '['):
            stack.append(w)
        if(w == ')'):
            if(len(stack)!=0):
                if(stack[-1] == '('):
                    stack.pop()
                else:
                    print("no")
                    forTF = False
                    break
            else:
                print("no")
                forTF = False 
                break
        if(w == ']'):
            if(len(stack)!=0):
                if(stack[-1] == '['):
                    stack.pop()
                else:
                    print("no")
                    forTF = False
                    break
            else:
                print("no")
                forTF = False 
                break
    if(forTF == False):
        continue
    if(len(stack)!=0):
        print("no")
        continue 
    print("yes")