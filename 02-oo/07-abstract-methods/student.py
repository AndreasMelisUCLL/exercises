# Write your code here
from abc import ABC, abstractmethod
class A(ABC):
    def a(self):
        self.b()
        
    @abstractmethod
    def b(self):
        ...
        
    @abstractmethod
    def c(self):
        ...

    def e(self):
        self.c()


class B(A): # gets a, e, has to implement b, c
    def b(self):
        self.a()

    def c(self):
        self.e()


class C(B): # gets a, b, c, e
    def f(self):
        pass


class D(A): # gets a, e, has to implement b, c
    def b(self):
        self.f()
        
    @abstractmethod
    def f(self):
        ...


class E(D): # gets a, b, e, has to implement c, f
    def c(self):
        self.a()

    def f(self):
        self.e()

    def g(self):
        self.f()


class F(ABC):
    def a(self):
        self.b()
        self.f()
    
    @abstractmethod
    def b(self):
        ...
        
    @abstractmethod
    def f(self):
        ...