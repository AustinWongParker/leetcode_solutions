class Solution:
    def isValid(self, s: str) -> bool:
        myStack = [ ]
        closeToOpen =  {   ')': '('    ,    ']': '['     ,    '}': '{'   }

        for i in s:

            # check if its a closing bracket
            if i in closeToOpen:

                # check if stack is empty
                if myStack and myStack[-1] == closeToOpen[i]:
                    myStack.pop()
                else:
                    return False

            #if we get an open bracket
            else:
                myStack.append(i)

        return True if not myStack else False