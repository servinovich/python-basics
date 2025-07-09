# script_4_safe_div.py

# Function declaration
def safe_divide(a, b):
   
    try:
        c = a / b
        print("Success! Result =", c)
        return c
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    
    except Exception as e:
        print("Something went wrong:", e)
        return None
    
    finally:
        print("\nProcessing Complete")

# Function implementation
try:
    a = int(input("Enter a numerator: "))
    b = int(input("Enter a denominator: "))
    result = safe_divide(a, b)
    
except ValueError:
    print("Please enter valid integers.")