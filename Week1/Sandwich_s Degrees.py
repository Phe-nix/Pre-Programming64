"""Sandwich's Degrees"""
import math
def main():
    """Sandwich's Degrees"""
    num_a = float(input())
    num_b = float(input())
    num_lfa = math.atan2(num_a, num_b)
    num_degrees = math.degrees(num_lfa)
    print("%.2f deg"%(num_degrees))
main()
