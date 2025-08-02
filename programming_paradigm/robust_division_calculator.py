def safe_divide(numerator, denominator):
    try:
       result = float(numerator)/ float(denominator)
       return f"Result {result}"
    except ValueError:
        return ("Error: please enter numeric values only. ")
    except ZeroDivisionError:
        return ("Error: Cannot divide by zero. ")