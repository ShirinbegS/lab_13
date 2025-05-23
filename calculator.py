# appliances/calculator.py

def calculate_energy_consumption(power, hours, days): #cколько потребляет 

    return (power * hours * days) / 1000

def calculate_cost(energy_consumption, rate): #общая стоимость

    return energy_consumption * rate