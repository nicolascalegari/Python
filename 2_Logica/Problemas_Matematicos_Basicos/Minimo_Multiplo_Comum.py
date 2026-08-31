a = 12
b = 18

original_a = a
original_b = b

while b != 0:

    resto = a % b
    a = b
    b = resto

mdc = a
mmc = (original_a * original_b) // mdc

print("MMC: ", mmc)