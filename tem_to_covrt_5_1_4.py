def temperature(cel):
    print("temperature conversion")
    Fahr = (cel * 1.8) + 32
    print('Coverted temperature=',Fahr)

num1=float(input("Enter the temperature in celcius "))
temperature(num1)