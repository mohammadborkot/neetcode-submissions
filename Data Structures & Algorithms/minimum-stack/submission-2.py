class MinStack:


    def __init__(self):
        self.con = [] # internal stack
        self.min_stack = [] # track min numbers

    def push(self, val: int) -> None:
        # We can add to min if val is not null
        if val is not None:
            # Is the min stack empty?
            if len(self.min_stack) == 0:
                self.min_stack.append(val)
            else:
                # Push only if its less than the current min
                if val <= self.getMin():
                    self.min_stack.append(val)
        self.con.append(val)

    def pop(self) -> None:
        # Stack is empty
        if len(self.con) == 0:
            return None

        # val to remove is the min val, so pop from min stack
        if self.getMin() == self.con[len(self.con) - 1]:
            self.min_stack.pop(len(self.min_stack) - 1)
        
        self.con.pop(len(self.con) - 1)

    def top(self) -> int:
        return self.con[len(self.con) - 1]

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[len(self.min_stack) - 1]
