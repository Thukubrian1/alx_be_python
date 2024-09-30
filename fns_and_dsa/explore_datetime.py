from datetime import datetime,timedelta

def display_current_datetime():
    current_date =  datetime.now()
    print(f"Current date and time: {current_date}")

display_current_datetime()

current_date = datetime.now()

future_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

calculate_future_date = int(input("Enter the  number of days to add to the current date: "))

future_date = current_date + timedelta(days=calculate_future_date)

calculate_future_date
print(f"Future date: {future_date}")