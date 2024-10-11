# easyAdd1.2: a lightweight calculator

# TODO
# - export to expenses google sheet

LINE_CLEAR = '\x1b[2K'
LINE_UP = '\033[1A'


def calculate(total):

    while True:

        print(f"    Total: £{format(round(total, 2), '.2f')}", end='\r')
        print(LINE_UP, end=LINE_CLEAR)
        num = input("    ")

        if num == "":
            return total

        while True:
            try:
                num = float(num)
                break
            except ValueError:
                print(LINE_UP, end=LINE_CLEAR)
                num = input("    ")
                continue

        print("")
        total += num


print("")
print("\n------------------------------------\n")
print(" I'm a funny welcome screen")
print(" Enter a list of numbers to add together")
print(" Or simply paste a list of numbers!")
print("\n------------------------------------\n")
print("")


while True:

    total = 0

    total = calculate(total)
    print(LINE_UP, end=LINE_CLEAR)
    print("")
    print(f"    this week i spent £{format(round(total, 2), '.2f')}")

    print("\n    Press enter to start again")
    print("    Or '0' to quit...")
    choice = input()

    if choice == '0':
        print("Goodbye!")
        exit(0)

    print("------------------------------------\n\n")
