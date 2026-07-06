class MinStack:
    def __init__(self):
        #Initialize 2 type of stacks one for min and other standard
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #Check if the stack doesn't exist
        if not self.minstack:
            self.minstack.append(val)
        else:
            #Calculate the minimum
            min_val = self.minstack[-1]
            min_val = min(min_val,val)
            self.minstack.append(min_val)

    def pop(self) -> None:
        #Pop both the stacks
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]
        
