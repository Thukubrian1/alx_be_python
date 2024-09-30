import datetime  

def display_current_datetime():
    current_date =  datetime.datetime.now()
    print(f"Current date and time: {current_date}")

display_current_datetime()

calculate_future_date = int(input("Enter the  number of days to add to the current date: "))

current_date = datetime.datetime.now()

future_date = current_date + datetime.timedelta(days=calculate_future_date)

print(f"Future date: {future_date}")