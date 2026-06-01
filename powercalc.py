val = (input("Enter the value you want to calculate the power of: "))
try:
    val = int(val)
    valisascorord = "number"
    val2 = val
except ValueError:
        try:
            val = float(val)
            valisascorord = "decimal number"
            val2 = val
        except ValueError:
                try:
                    val = str(val)
                    val2 = val
                    valisascorord = str(input("Do you mean the ASCII value or the placement in the latin lexicon? (ASCII/placement): ").lower())
                    if valisascorord == "ascii":
                        valisascorord = "ASCII value of"
                        val = int(ord(val))
                    elif valisascorord == "placement":
                        valisascorord = "placement in the latin lexicon of"
                        val = int(ord(val) - 96)
                    else:
                        print("Invalid input. Please enter 'ASCII' or 'placement'.")
                        exit()
                except ValueError:
                    print("Invalid input. Please enter a number or a string.")
                    exit()
power = (input("Enter the power you want to calculate: "))
try:
    power = int(power)
    powerisascorord = "number"
    power2 = power
except ValueError:
        try:
            power = float(power)
            powerisascorord = "decimal number"
            power2 = power
        except ValueError:
                try:
                    power = str(power)
                    power2 = power
                    powerisascorord = str(input("Do you mean the ASCII value or the placement in the latin lexicon? (ASCII/placement): ").lower())
                    if powerisascorord == "ascii":
                        powerisascorord = "ASCII value of"
                        power = int(ord(power))
                    elif powerisascorord == "placement":
                        powerisascorord = "placement in the latin lexicon of"
                        power = int(ord(power) - 96)
                    else:
                        print("Invalid input. Please enter 'ASCII' or 'placement'.")
                        exit()
                except ValueError:
                    print("Invalid input. Please enter a number or a string.")
                    exit()
woc = str(input("Would you like to calculate it using a for loop or a exponentiation operator? (for/exponentiation): "))
if woc == "for":
    print("This will put heavy load on your computer: ")
    for i in range(power):
        val = val * val
        result = int(val)
elif woc == "exponentiation":
    result = val ** power
else:
    print("Invalid input. Please enter 'for' or 'exponentiation'.")
    exit()
print("The result of the", valisascorord, val2, "to the power of the", powerisascorord, power2, "using the", woc, "method is:", result)
exit()