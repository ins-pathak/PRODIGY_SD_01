def convert_temperature(temperature, unit):

  converted_temps = {}
  if unit.upper() == 'C':
    converted_temps['Fahrenheit'] = (temperature * 9/5) + 32
    converted_temps['Kelvin'] = temperature + 273.15
  elif unit.upper() == 'F':
    converted_temps['Celsius'] = (temperature - 32) * 5/9
    converted_temps['Kelvin'] = (temperature + 459.67) * 5/9
  elif unit.upper() == 'K':
    converted_temps['Celsius'] = temperature - 273.15
    converted_temps['Fahrenheit'] = (temperature - 273.15) * 9/5 + 32
  else:
    converted_temps = {'Error': 'Invalid unit. Please use C, F, or K.'}

  return converted_temps


while True:
  try:
    temperature = float(input("Enter temperature value: "))
    unit = input("Enter unit (C, F, or K): ").upper()
    break
  except ValueError:
    print("Invalid input. Please enter a numerical temperature value.")


converted_temperatures = convert_temperature(temperature, unit)

if 'Error' not in converted_temperatures:
  for unit, value in converted_temperatures.items():
    print(f"{temperature:.2f}°{unit} is equivalent to {value:.2f}°")
else:
  print(converted_temperatures['Error'])
