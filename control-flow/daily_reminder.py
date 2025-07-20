task = input("Enter your task: ")
priority =input("priority (high/medium/low): ")
time_bound =input("is it time-bound?(yes/no): ")

match priority:
    case "high":
        if(time_bound == "yes"):   
            print(f"Reminder:{task} is a high priority tassk that requires immediate attention today!")
    case "medium":
        if(time_bound == "no"):
            print(f"complete{task} at will ")
    case "low":
        if (time_bound == "no"):
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")