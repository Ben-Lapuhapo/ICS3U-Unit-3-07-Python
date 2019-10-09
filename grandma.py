# usr/bin/env python3

# Created by Ben Lapuhapo
# Created on Oct 2019
# Pibad


def main():
    # this function uses a compound boolean statement

    # input
    age = int(input("Enter Age: "))
    print("")

    # process & output
    if age >= 25 and age <= 40:
        print("You can marry The Daughter")
    elif age > 40:
        print("Too old to date Her, Just Date the Grandmother!!")
    else:
        print("Too young to date Her")


if __name__ == "__main__":
    main()
