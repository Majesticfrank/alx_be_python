class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a,b):
        return a + b
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b 
    

sum_result =Calculator.add(10, 5)


product_result = Calculator.multiply(4, 5) 
