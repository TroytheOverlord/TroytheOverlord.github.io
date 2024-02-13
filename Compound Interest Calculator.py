principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter your initial principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
while rate <= 0:
    rate = float(input("Enter your interest rate amount: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")

print(principle)
print(rate)
print(time)

final_amount = principle * ((1 + rate / 100) ** time)

print(f"Your final amount is after {time} year/s is: ${round(final_amount,2)}")