medical_cause=input("Enter a medical cause yes or no:")
atten=int(input("Enter your attendance:"))

if medical_cause =="yes":
   print("You are allowed")
else:
   if atten>=75:
      print("You are allowed")
   else:
      print("You are not allowed")


#Activity 2
units=int(input("Enter the no of units you have consumed:"))

if (units<50):
   amount=units*2.60
   tax=25
elif(units<=100):
   amount=units*3.25
   tax=35
elif(units<=200):
   amount=units*5.26
   tax=75

total=amount+tax
print("\nElectricity bill =%.2f" %total)

#Activity 3

print("Select your ride")
print("1. Car")
print("2. Bike")

choice=int(input("Enter your choice:"))

if(choice==1):
    print("What type of car do you want?")
    print("1. Sedan")
    print("2. SUV")

    choice1=int(input("Enter your choice:"))
    if(choice1==1):
      print("You have selected a sedan")
    else:
      print("You have selected an SUV")

elif(choice==2):
    print("What type of bike do you want?")
    print("1. Cruiser")
    print("2. Sport")

    choice2=int(input("Enter your choice:"))
    if(choice2==1):
        print("You have selected a cruiser")
    elif(choice2==2):
        print("You have selected a sport bike")
else:
    print("Invalid choice")
