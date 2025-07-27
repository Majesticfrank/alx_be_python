import datetime

def display_current_datetime():
    current_date = datetime.datetime.today() 
    formatted_date = current_date.strftime("%A, %d %B %Y, %I:%M %p") 
    print(f"Current date and time: {current_date}")
    print(f"Formatted date and time: {formatted_date}")
    return current_date 
def calculate_future_date():

        days = int(input("Enter the number of days to add to the current date (1-31): "))
        if 0 < days <= 31:
            current_date = datetime.datetime.today()
            future_date = current_date + datetime.timedelta(days=days)
            print(f"Future date after {days} days: {future_date.strftime('%A, %d %B %Y, %I:%M %p')}")
        else:
            print("Invalid input. Please enter a number between 1 and 31.")
    
       


display_current_datetime()
calculate_future_date()

