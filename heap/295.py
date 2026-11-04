import heapq

class MedianFinder:

    def __init__(self):
        self.lista = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lista, num)


    def findMedian(self) -> float:
        tam = len(self.lista)
        temp = self.lista
        if tam % 2 == 1:
            for temp in range(int(tam/2)):
                heapq.heappop(temp)
            
            return heapq.heappop(temp)
        
        for temp in range(int(tam/2) - 1):
            heapq.heappop(temp)

        num1 = heapq.heappop(temp)
        num2 = heapq.heappop(temp)
        return (num1 + num2)/2

m = MedianFinder()
m.addNum(1);    
m.findMedian(); 
m.addNum(2);    
m.findMedian(); 
m.addNum(3);    
print(m.findMedian()); 
        