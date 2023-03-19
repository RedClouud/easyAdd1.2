# easyAdd1.2

prompt = ""


def calculate(i, total):

    while True:
        num = input(f"Enter item {i}: ")

        if num == "":
            return total

        while True:
            try:
                num = float(num)
                break
            except ValueError:
                print("Please enter a valid number")
                continue

        total += round(num, 2)
        i += 1


print("\n------------------------------------\n")
print(" Welcome to easyAdd1.2")
print(" Enter a list of numbers to add together")
print(" Or simply paste a list of numbers!")
print("\n------------------------------------\n")

while prompt != "0":
    i = 1
    total = 0

    total = calculate(i, total)
    print(f"\nthis week i spent £{format(total, '.2f')}\n")

    prompt = input("Press enter to enter another list, 0 to quit: ")

print("\nGoodbye!")
