class Queue:
    def __init__(self):
        # Initialize two stacks enqueue and dequeue
        self.stk_in = []  
        self.stk_out = []  

    def enqueue(self, x: int) -> None:
        self.stk_in.append(x)

    def dequeue(self) -> int:
        if not self.stk_out:
            # Transfer elements from stk_in to stk_out if stk_out is empty
            while self.stk_in:
                self.stk_out.append(self.stk_in.pop())
        
        # If stk_out is still empty, the queue is empty
        if not self.stk_out:
            raise IndexError("dequeue from an empty queue")

        return self.stk_out.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  
q.enqueue(3)
print(q.dequeue())  
