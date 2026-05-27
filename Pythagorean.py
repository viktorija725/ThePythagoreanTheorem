import math

def main():
    print("*** The Pythagorean theorem ***")
    print("a2 + b2 = c2")
    print("a and b - triangle legs")
    print("c - hypotenuse")
    print()

    a = float(input(f"Enter a: "))
    b = float(input(f"Enter b: "))
    print()

    newa = a**2
    newb = b**2
    newc = newa + newb
    area = (a*b)/2
   

    print(f"{a}\u00b2 + {b}\u00b2 = c\u00b2")
    print(f"{newa} + {newb} = c\u00b2")
    print(f"{newc} = c\u00b2")
    print(f"c = {round(math.sqrt(newc), 2)}cm")
    print(f"area = {area}cm\u00b2")
    print()
    print(f"Congratulations!")


if __name__ == "__main__":
    main()
