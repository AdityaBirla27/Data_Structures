from heap import *

class heap_delete(heap):

    def delete(self, i):# therefore using this code will run in (log n) time
        if(i <= self.heapsize):#to validate that i is not out of bounds
            self.A[i] = self.A[-1]#replace i by last element
            del(self.A[-1])#removes last element
            self.heapsize =self.heapsize -1#reduce heap size by 1
            self.min_heapify(i)#heapify position i
