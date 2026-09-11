def eh_Primo(numero):
    if numero < 2:
        return False

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True

print(eh_Primo(7))
print(eh_Primo(10))