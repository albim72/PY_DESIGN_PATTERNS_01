class MultiBases(type):
    def __new__(cls,name,bases,args):
        if len(bases) > 1:
            raise TypeError("Nie możliwe jest wielodziedziczenie!")
        return super().__new__(cls,name,bases,args)


class Base(metaclass=MultiBases):
    pass

class A(Base):
    pass

class B(Base):
    pass

class C(A,B):
    pass

class Info:
    pass

class Next(Info,C):
    pass

