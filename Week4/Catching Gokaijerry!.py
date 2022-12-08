"""Catching Gokaijerry!"""
def main():
    """Catching Gokaijerry!"""
    state = 0
    police = int(input())
    while police > 0:
        txt = input()
        if txt == "Boom!!!":
            if state == 0:
                police = police - 1
                state = 1
        elif txt == "The trap is set.":
            state = 1

        elif txt == "No trap here":
            state = 0

        elif txt == "Catch the Gokaijerry":
            print("%d police is catching Gokaijerry." %police)
            break
    if police == 0:
        print("Gokaijerry is alive.")
main()
