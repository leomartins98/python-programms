print ("Digite a escala de entrada: \n")
print ("1 - Fahrenheit \n2 - Celsius \n3 - Kelvin \n4 - Rankine")
opcao_entrada = int(input())

print("Digite a temperatura: ")
temp = float(input())

def celsius_fahrenheit(temp):
    return (temp * 9 / 5) + 32


def celsius_kelvin(temp):
    return temp + 273.15

def celsius_rankine(temp):
    return temp * 9/5 + 491.67


def fahrenheit_celsius(temp):
    return (temp - 32) * (5 / 9)


def fahrenheit_kelvin(temp):
    return (temp - 32) * 5 / 9 + 273.15


def fahrenheit_rankine(temp):
    return temp + 459.67


def kelvin_celsius(temp):
    return temp - 273.15


def kelvin_fahrenheit(temp):
    return (temp - 273.15) * 9 / 5 + 32


def kelvin_rankine (temp):
    return temp * 1.8


def rankine_celsius(temp):
    return (temp - 491.67) * 5/9


def rankine_fahrenheit(temp):
    return temp - 459.67


def rankine_kelvin(temp):
    return temp * 5 / 9


if opcao_entrada==1: 
    print (f"Temp Celsius: {fahrenheit_celsius(temp):.2f} \nTemp Kelvin: {fahrenheit_kelvin(temp):.2f} \nTemp Rankine: {fahrenheit_rankine(temp):.2f}")

elif opcao_entrada==2: 
    print (f"Temp Fahrenheit: {celsius_fahrenheit(temp):.2f} \nTemp Kelvin: {celsius_kelvin(temp):.2f} \nTemp Rankine: {celsius_rankine(temp):.2f}")

elif opcao_entrada==3: 
    print (f"Temp Fahrenheit: {kelvin_fahrenheit(temp):.2f} \nTemp Celsius: {kelvin_celsius(temp):.2f} \nTemp Rankine: {kelvin_rankine(temp):.2f}")

elif opcao_entrada==4: 
    print (f"Temp Celsius: {rankine_celsius(temp):.2f} \nTemp Fahrenheit: {rankine_fahrenheit(temp):.2f} \nTemp Kelvin: {rankine_kelvin(temp):.2f}")

else: 
    print("Digite um número válido!!") 
