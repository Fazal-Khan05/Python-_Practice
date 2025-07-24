def ctf(x):
    farenheit =(x * 9/5) + 32
    return farenheit
input = float(input("Enter Temprature in Celsius :"))

output = ctf(input)
print("The temprature in farenheit is :" , output)