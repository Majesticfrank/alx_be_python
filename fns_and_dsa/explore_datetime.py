from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now() 
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S") 
    print(f"Current date and time: {current_date}")
    print(f"Formatted date and time: {formatted_date}")
    return current_date 
def calculate_future_date():
        from datetime import datetime, timedelta

        days = int(input("Enter the number of days to add to the current date:" ))
        if 0 < days <= 31:
            current_date = datetime.now()
            future_date = current_date + timedelta(days=days)
            print(f"Future date after {days} days: {future_date.strftime("%Y-%m-%d %H:%M:%S")}")
        else:
            print("Invalid input. Please enter a number between 1 and 31.")
    
       


display_current_datetime()
calculate_future_date()

