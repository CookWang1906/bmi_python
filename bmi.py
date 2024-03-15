#These programs will never be out of time.
import time

def pick():
    print("\nHello welcome to the Body Mass Index measuring, so what exactly is BMI?")
    print("Body Mass Index (BMI) is a person's weight in kilograms divided by the square of height in meters.")
    print("A high BMI can indicate high body fatness. BMI screens for weight categories that may lead to health problems, but it does not diagnose the body fatness or health of an individual.")
    print("Cautions: You should not use BMI as a measure if you're pregnant. Athletes is very healthy even though their BMI is in the obese range.")
    time.sleep(3)
    print("\n1. Measure your BMI")
    print("2. Stop measuring")
    choices = int(input("Please choose one to continue: "))
    
    if choices == 1:
        bmi()
    elif choices == 2:
        print()
    else:
        print("Try again!")
        return pick()
    
def bmi():
    a = float(input("\nYour height (cm): "))
    b = float(input("Your weight (kg): "))
    a1 = a/100
    bmi = b/(a1*a1)
    
    if bmi < 18.5:
        print(f"\nYour BMI result: {bmi}\nBe careful! You're in the underweight range.")
        print("You can watch the routines folder to know better on how to improve your weight.")
        time.sleep(5)
        return pick()
    elif 18.5 <= bmi <= 24.9:
        print(f"\nYour BMI result: {bmi}\nVery good! You're in the healthy weight range.")
        print("Congratulations! You're a healthy person.")
        print("You can maintain your health even better by watching the routines folder.")
        time.sleep(3)
        return pick()
    elif 25 <= bmi <= 29.9:
        print(f"\nYour BMI result: {bmi}\nCautions! You're in the overweight range.")
        print("To know better about losing weight, you can read the routines folder for your weight.")
        time.sleep(5)
        return pick()
    elif bmi >= 30:
        print(f"\nYour BMI result: {bmi}\nWarning! You're in the obese range.")
        print("You can know better about losing weight by watching the routines folder. I hope you the best, man.")
        time.sleep(5)
        return pick()
pick()