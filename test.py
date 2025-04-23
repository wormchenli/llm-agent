from injector import Injector, inject

class A:
    name: str = "Li Chen"

class C:
    name: str = "Zhi Chen"

class B:
    @inject
    def __init__(self, a: A, c:C):
        self.a = a
        self.c = c

    def print(self):
        print(f"Class A's name is {self.a.name}, C's name is {self.c.name}")

injector = Injector()
b = injector.get(B)
b.print()
