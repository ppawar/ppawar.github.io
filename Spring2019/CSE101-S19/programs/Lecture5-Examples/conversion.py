def f(c):
    f(c)=c*(9/5)+32
    return f
Celsius_Temperature = int(input("Enter Temperature in Celsius: "))
print(str((Celsius_Temperature))+'Celsius='+ '{:,f()}', format(f(Celsius_Temperature), 'Fahrenheit')