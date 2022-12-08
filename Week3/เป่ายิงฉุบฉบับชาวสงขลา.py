"""เป่ายิงฉุบฉบับชาวสงขลา"""
def main():
    """เป่ายิงฉุบฉบับชาวสงขลา"""
    pee_sui = input()
    pee_numphung = input()
    print("Draw"*(pee_sui == pee_numphung) + "Sui"*((pee_sui == "Stone" and\
    pee_numphung == "Bird")\
    or (pee_sui == "Water" and pee_numphung == "Stone") or (pee_sui == "Bird"\
    and pee_numphung == "Water"))\
    + "Numphung"*((pee_sui == "Bird" and pee_numphung == "Stone") or\
    (pee_sui == "Stone" and pee_numphung == "Water") or\
    (pee_sui == "Water" and pee_numphung == "Bird")))
main()
