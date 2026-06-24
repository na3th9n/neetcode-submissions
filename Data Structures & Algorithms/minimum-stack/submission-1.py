class MinStack:

    def __init__(self):
        self.stack = []
        self.minHeap = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # tmp = self.stack
        # print(tmp)
        # heapq.heapify(tmp)
        # print(tmp)

        # return tmp[0]
        return min(self.stack)
        
