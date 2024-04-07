# from https://leetcode.com/problems/implement-queue-using-stacks/?envType=daily-question&envId=2024-01-29

class MyQueue:

    def __init__(self):
        self.data = []
        

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        return self.data.pop(0)

    def peek(self) -> int | None:
        if not self.data:
            return None
        return self.data[0]

    def empty(self) -> bool:
        if self.data == []:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
x = 1
obj = MyQueue()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()