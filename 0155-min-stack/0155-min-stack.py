class MinStack:

    def __init__(self):
        self.items=[]
        self.minstack=[]

    def push(self, value: int) -> None:
        self.items.append(value)
        if len(self.minstack)==0:
            self.minstack.append(value)
        else:
            self.minstack.append(min(value,self.minstack[-1]))

    def pop(self) -> None:
        self.items.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()