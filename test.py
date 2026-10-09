from injector import Injector, inject


class A:
    name: str = "llmops"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"A name is {self.a.name}")


injector = Injector()
b = injector.get(B)
b.print()
