

def main(name, age, place):
    print(f"This is {name}")
    print(f"This is {age}")
    print(f"This is {place}")

if __name__ == "__main__":
    name = input("Whats your name? ")
    age = int(input("How old are you? "))
    place = input("Where are you from? ")
    main(name, age, place)
