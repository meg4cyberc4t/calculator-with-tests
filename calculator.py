from typing import Union


class Calculator:
    @staticmethod
    def addition(x: float, y: float) -> float:
        return x + y

    @staticmethod
    def subtraction(x: float, y: float) -> float:
        return x - y

    @staticmethod
    def division(x: float, y: float) -> Union[str, float]:
        if y == 0:
            return "error"
        return x / y

    @staticmethod
    def multiplication(x: float, y: float) -> float:
        return x * y

    @staticmethod
    def pow(x: float, y: float) -> float:
        return x ** y