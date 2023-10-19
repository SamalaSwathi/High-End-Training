class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def add_data_in_queue(self, value):
        if (self.rear+1)%self.size == self.front:
            print("queue is full")
        elif self.front == -1:
            self.front = 0 
            self.rear = 0 
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = value
    def remove_data_from_queue(self):
        if self.front == -1:
            print("queue is empty")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.rear = -1
            self.front = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front += (self.front+1)%self.size
            return temp
    def print_queue(self):
        print(self.queue)
        print(self.front, self.rear)
        
ob = CircularQueue(5)
ob.add_data_in_queue(100)
ob.add_data_in_queue(200)
ob.add_data_in_queue(300)
ob.add_data_in_queue(400)
ob.add_data_in_queue(500)
ob.remove_data_from_queue()
ob.add_data_in_queue(600)
ob.print_queue()
