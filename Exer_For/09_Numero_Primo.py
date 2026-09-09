for numero in range(2, 51):

    primo = True

    for divisor in range(2, numero):

        if numero % divisor == 0:

            primo = False
            break

    if primo:

        print(numero) 