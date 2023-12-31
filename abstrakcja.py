from abc import ABC,abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x=x

    def msg(self,m):
        return f'kod numer: {m}'

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*7

class Regular(Prototyp):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def policz(self):
        return 1001

    def policz_x(self):
        return super().policz_x()+self.y*3


r = Regular(4,8)
print(f'policz: {r.policz()}')
print(f'policz_x: {r.policz_x()}')
print(r.msg(554))
