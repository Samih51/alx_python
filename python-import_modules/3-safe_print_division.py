def safe_print_division(a,b):
    try:
        
        result = a / b
 
    except ValueError:
        print("Invalid input. Please enter valid integers.")
    except ZeroDivisionError:
        result = None
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("Inside result:{}".format(result))
safe_print_division(6,0)