def safe_divide(numerator , denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of {numerator} / {denominator} is {result:.2f}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    
    except  ValueError:
        return "Error: Enter a numeric value"
