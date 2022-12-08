"""[quiz] Nintendo Battery"""
def main():
    """[quiz] Nintendo Battery"""
    battery = int(input())
    laght = int(input())
    result = int(laght*(battery / 100))
    dis = laght - result
    print("(%s%s) %d"%(result*"O", dis*"_", battery)+ "%")
main()
