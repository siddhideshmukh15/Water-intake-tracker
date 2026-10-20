print("==== Water Intake Tracker ====")
goal=int(input("Enter your daily goal(ml):"))
total=0

while True:
    print("\n 1.Add Water")
    print("2.View progress")
    print("3.Exit")
    
    choice=input("Enter your choice:")
    
    if choice =="1":
        amount=int(input("Enter water consumed(ml):"))
        
        if amount >0:
            total += amount
            print("water intake added!")
            
        else:
            print("Enter a positive amount!")
            
    elif choice=="2":
        print("Daily Goal:",goal,"ml")
        print("Water consumed:",total,"ml")
        print("Remaining:",max(0,goal-total),"ml")
        progress=min(100,round(total/goal*100))
        print("progress:",progress,"%")
            
    elif choice=="3":
        print("keep tracking your hydration!")
        break
    else:
        print("Invalid choice!")