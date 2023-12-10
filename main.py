from abc import ABC, abstractmethod

print("Diggers; DevOPs + Scrum Master; maresyp")
print("maresyp")
print("Diggers; tester; Pavlucek")
print("Developer: Mirek0206")
print("Diggers; developer; gruszm")
#BBC
class ArithmeticDifference(ABC):
    @abstractmethod
    def Difference[T: float](self, a: T, b: T) -> T:
        raise NotImplementedError

class ArithmeticsMultiply(ABC):
    @abstractmethod
    def Multiplication[T: float](self, a: T, b: T) -> T:
        raise NotImplementedError
# this... is very hard to implement
class ArithmeticDivision(ABC):
    @abstractmethod
    def division[T: float](self, a: T, b: T) -> T:
        raise NotImplementedError

class ArithmeticsAdd(ABC):
    @abstractmethod
    def Addition[T: float](self, a: T, b: T) -> T:
        raise NotImplementedError