Task = input("Input your task: ")

Priority = input("Priority (high/medium/low): ")

Time_bound = input("Is it time-bound? (yes/no): ")

match Priority:
    case "high":
        if Time_bound == "yes":
            print(f"{Task} is a high priority task that requires immediate attention today! ")
        
        elif Time_bound == "no":
            print(f"{Task} is a high priority task. Consider completing it when you have free time ")
    
    case "medium":
        if Time_bound == "yes":
            print(f"{Task} is a medium priority task that requires immediate attention today! ")
        
        elif Time_bound == "no":
            print(f"{Task} is a medium priority task. Consider completing it when you have free time ")

    case "low":
        if Time_bound:
            print(f"{task} is a low priority task that requires immediate attention today! ")
        
        elif Time_bound == "no":
            print(f"{Task} is a low priority task. Consider completing it when you have free time ")
    case _:
        print("Invalid input")