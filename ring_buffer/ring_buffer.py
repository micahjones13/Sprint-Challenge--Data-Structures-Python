class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # append item to storage at current place
        # if self.capacity == self.current:
        #     self.current = 0
        # self.storage.append(item)
        # del self.storage[0:2]

        # if the capicty == current, restart the counter and overwrite the older values
        if self.capacity == self.current:
            self.current = 0
        # since it's a pre-allocated list, just need to change the value at each index of the list
        # using current as a counter, we go through each place in the list and update it until we reach capacity
        self.storage[self.current] = item
        # up counter
        self.current += 1

    def get(self):
        new = []
        # don't want to return None values in the list.
        for i in range(len(self.storage)):
            if self.storage[i] != None:
                new.append(self.storage[i])

        return new


test = RingBuffer(5)

test.append('a')
test.append('b')
test.append('c')
test.append('d')
print(test.get())
