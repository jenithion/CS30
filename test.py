class P:
    def __init__(self, x):
       self.x = x + 7

    def __repr__(self):
       return f'P({self.x})'


p1 = P(4)
print(p1) #Q1
p2 = P(3)
print(p2)#Q2
p3 = P(4)

print(p3)#Q3
print(p1 == p2)#Q4
print(p1 == p3)#Q5