"""Composite Function"""
def main():
    '''Composite Function'''
    num = float(input())
    def fog():
        '''fog'''
        num_g = (num**3)+(4*num)-1
        forgans = (15+num_g-(num_g**3))
        forgans_2 = ((num_g**2)/3)+11
        result = forgans / forgans_2
        print("%.4f" %(result))
    fog()

    def gof():
        '''gof'''
        num_f = (15+num-(num**3))
        num_f_1 = ((num**2)/3)+11
        num_f_result = num_f / num_f_1
        gofans = (num_f_result**3)+(4*num_f_result)-1
        print("%.4f" %(gofans))
    gof()
main()
