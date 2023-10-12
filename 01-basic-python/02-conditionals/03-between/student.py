def is_prime(n):
    for i in range(2, n): #We gaan delen door elke getal tussen 2 en de nummer zelf
        if (n % i) == 0: #Niet een priemgetal
            return False
    #als er geen 'break' in de 'for' gevonden wordt - dan is het wel een priemgetal
    return n > 1