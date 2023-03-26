# easyAdd1.2: a lightweight calculator

# TODO
# - export to expenses google sheet

LINE_CLEAR = '\x1b[2K'
LINE_UP = '\033[1A'


def calculate(i, total):

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
        total += round(num, 2)
        i += 1


print("\n------------------------------------\n")
print(" Welcome to easyAdd1.2")
print(" Enter a list of numbers to add together")
print(" Or simply paste a list of numbers!")
print("\n------------------------------------\n")


while True:

    print("""
    ------------------------------------
    enter - enter another list
    0 - quit: 
    ------------------------------------
    """)

    prompt = input("Prompt: ")

    if prompt == "":
        i = 1
        total = 0

        total = calculate(i, total)
        print(LINE_UP, end=LINE_CLEAR)
        print("")
        print(f"    this week i spent £{format(round(total, 2), '.2f')}")

    elif prompt == "0":
        print("\nGoodbye!")
        exit(0)

    else:
        print("Please enter a valid option")
