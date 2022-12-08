"""more about TEMP V.1"""
def main():
    """more about TEMP V.1"""
    num_tep = float(input())
    print("Celsius    = %.4f"%(num_tep))
    print("Fahrenheit = %.4f"%((num_tep*(9/5))+32))
    print("Kelvin     = %.4f"%(num_tep + 273.15))
    print("Rankine    = %.4f"%((num_tep + 273.15)*(9/5)))
    print("Reaumer    = %.4f"%(num_tep * (4/5)))
main()
