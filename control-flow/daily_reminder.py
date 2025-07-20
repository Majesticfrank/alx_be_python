task = input("Enter the task: ")
priority =input("high/medium/low ");
time =input("is it time-bound?(yes/no) ")

match priority:
    case "high":
        if(time =="yes"):   
            print("Reminder: 'Finish project report' is a high priority tassk that requires immediate attention today!")
    case "medium":
        if(time =="no"):
            print("complete at will ")
    case "low":
        if (time=="low"):
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")