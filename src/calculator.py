from .custom_ex import IncorrectInputError


class Calculator:
    def add(self, *args: float) -> float:  # type: ignore
        return sum(args)

    def multiply(self, *args: float):  # (1,2,3)
        try:
            result: float = 1
            for i in args:
                result *= i
            return result
        except TypeError:
            raise IncorrectInputError("Wrong Input")
        
    def division(self, *args) :
        try:
            result: float = args[0]
            for i in args[1:]:
                result /= i
            return result
        except TypeError:
            raise IncorrectInputError("Wrong Input")
        
