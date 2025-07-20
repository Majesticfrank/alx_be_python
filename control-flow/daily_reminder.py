task = input("Enter your task: ")
priority =input(" priority (high/medium/low): ")
time_bound =input("is it time-bound?(yes/no): ")

match priority:
    case "high":
        if(time_bound == "yes"):   
            print("Reminder: 'Finish project report' is a high priority tassk that requires immediate attention today!")
    case "medium":
        if(time_bound == "no"):
            print("complete at will ")
    case "low":
        if (time_bound == "low"):
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")