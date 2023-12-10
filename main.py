print("Diggers; DevOPs + Scrum Master; maresyp")
print("maresyp")
print("Diggers; tester; Pavlucek")
print("Developer: Mirek0206")
print("Diggers; developer; gruszm")

from abc import ABC, abstractmethod

class ArithmeticDifference(ABC):
    @abstractmethod
    def Difference[T: float](self, a: T, b: T) -> T:
        raise NotImplementedError