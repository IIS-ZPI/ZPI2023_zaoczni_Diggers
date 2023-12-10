from abc import ABC, abstractmethod

print("Diggers; DevOPs + Scrum Master; maresyp")
print("maresyp")
print("Diggers; tester; Pavlucek")
print("Developer: Mirek0206")
print("Diggers; developer; gruszm")

class ArithmeticDifference(ABC):
    @abstractmethod
    def difference[T: float](self, a: T, b: T) -> T:
        raise NotImplementedError

class ArithmeticsMultiply(ABC):
    @abstractmethod
    def multiplication[T: float](self, a: T, b: T) -> T:
        raise NotImplementedError
# this... is very hard to implement
class ArithmeticDivision(ABC):
    @abstractmethod
    def division[T: float](self, a: T, b: T) -> T:
        raise NotImplementedError

class ArithmeticsAdd(ABC):
    @abstractmethod
    def addition[T: float](self, a: T, b: T) -> T:
        raise NotImplementedError
