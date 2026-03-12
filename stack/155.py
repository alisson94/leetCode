class MinStack:

    def __init__(self):
        self.lista = []
        self.menores = []

    def push(self, val: int) -> None:
        if self.lista:
            if val <= self.menores[-1]:
                self.menores.append(val)
        else:
            self.menores.append(val)
        self.lista.append(val)

    def pop(self) -> None:
        tal = self.lista[-1]
        if tal == self.menores[-1]:
            self.menores.pop()
        self.lista.pop()

    def top(self) -> int:
        return self.lista[-1]

    def getMin(self) -> int:
        return self.menores[-1]


m = MinStack()

m.push(0)
m.push(-1)
m.push(0)
m.pop()
# print(m.getMin())
# m.pop()
# print(m.getMin())

print(m.lista)
print(m.menores)