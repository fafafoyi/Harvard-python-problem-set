import math

def main():
    fraction = get_fraction()
    gauge = convert_to_gauge(fraction)
    print(gauge)
 

def get_fraction():
    
    while True:
        try:
            fraction_input = input("Fraction : ").strip()
            numerator, denominator = map(int, fraction_input.split('/'))
            percentage = (numerator / denominator) * 100
            rounded_percentage = math.ceil(percentage)

            return rounded_percentage
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

def convert_to_gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"



main()