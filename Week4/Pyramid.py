"""Pyramid"""
def main():
    """Pyramid"""
    num = int(input())
    for i in range(num):
        print(' '*(num-i-1) + '*'*((2*i)+1))
    for i in range(num):
        print(' '*(i+1) + '*'*((2*((num-1)-i))-1))
main()
