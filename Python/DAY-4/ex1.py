import sys
temperature = input("Input valid Fareinheit temperature value: \n")
try:
   temperature = temperature.replace("F", "")
   print(temperature)
   temperature = int(temperature)
except ValueError:
    print("Invalid input. Try again.")
    sys.exit()

if temperature < 97.7:
    print("Temperature is low.")
elif temperature >= 97.7 and temperature <= 99.5:
    print("Temperature is normal.")
else:
    print("Temperature is high.")