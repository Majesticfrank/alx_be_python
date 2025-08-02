def safe_divide(numerator, denominator):
    try:
       return float(numerator/denominator)
    except ValueError:
        return ("Error: please enter numeric values only")
    except ZeroDivisionError:
        return ("cannot divide by zero ")