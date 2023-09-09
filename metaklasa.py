class MojaMeta(type):
    def __new__(cls, clsname,superclasses,attrs):
        print("*********************************************")
        print(f'nazwa klasy: {clsname}')
        print(f'dziedziczone klasy: {superclasses}')
        print(f'zbiór atrybutów: {attrs}')
        return type.__new__(cls, clsname,superclasses,attrs)

class S:
    pass

class F:
    pass

class Specjalna(S,metaclass=MojaMeta):
    def info(self):
        return 123

class B(Specjalna):
    pass

class C(F,B):
    pass
