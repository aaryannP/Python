print("--- Simple Calculator ---")
print("Operations: +, -, *, /")

while True:
    try:
        num1_str = input("Enter first number (or 'q' to quit): ")
        if num1_str.lower() == 'q':
                break
        num1 = float(num1_str)

        operator = input("Enter operator (+, -, *, /): ")

        num2_str = input("Enter second number: ")
        num2 = float(num2_str)

        result = None 

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        else:
            print("Invalid operator. Please use +, -, *, or /.")
            continue # Go back to the start of the loop

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        # Catches errors if float() conversion fails (e.g., user enters text)
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError as e:
        # Catches division by zero errors
        print(f"Error: {e}")
    except Exception as e:
        # Catches any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    finally:
        # This block will always execute, regardless of whether an exception occurred
        print("Calculation attempt finished.")
    print("-" * 30)