# Labration 1
# Skriven av Farhad Asadi, 13 september 2021

# Krav på ett godkänd lösenord
# 1. Lösenordet måste ha en längd på minst 6 och högst 16 tecken.
# 2. Lösenordet måste ha minst ett numeriskt värde.
# 3. Lösenordet måste ha minst ett av specialtecknen $, @, ! och *.
# 4. Lösenordet måste ha minst en liten och en stor bokstav.

 

def validate_pwd(string):
    
    """
        Returnera True om lösenordet är giltigt och returnera False om lösenordet inte är giltigt 
    """

    # Kontrollera längden!
    def kontrollera_längd(passw):
        length = len(passw)
        if length < 6:
            return False
        elif length > 16:
            return False
        else:
            return True
    
    # Kontrollera om lösenordet innehåller ett numerikst värde! 
    def kontrollera_numeriskt_värde(passw):
        Yes_or_No = any(char.isdigit() for char in passw)
        if Yes_or_No == True:
            return True
        else:
            return False
    
    # Kontrollera om lösenordet innehåller en stor bokstav!
    def kontrollera_stor_bokstav(passw):
        Yes_or_No = any(char.isupper() for char in passw)
        if Yes_or_No == True:
            return True
        else:
            return False
    
    # Kontrollera om lösenordet innehåller en liten bokstav! 
    def kontrollera_liten_bokstav(passw):
        Yes_or_No = any(char.islower() for char in passw)
        if Yes_or_No == True:
            return True
        else:
            return False
    
    # Kontrollera om Lösenordet innehåller ett av specialtecknen $, @, ! och * 
    specialtecken = ['$', '@', '!', '*']
    def kontrollera_specialtecken(passw):
        Yes_or_No = any(char in specialtecken for char in passw)
        if Yes_or_No == True:
            return True
        else:
            return False

    func1 = kontrollera_längd(string) # True eller False
    func2 = kontrollera_numeriskt_värde(string) # True eller False
    func3 = kontrollera_stor_bokstav(string) # True eller False
    func4 = kontrollera_liten_bokstav(string) # True eller False
    func5 = kontrollera_specialtecken(string) # True eller False

    list1 = [func1, func2, func3, func4, func5]
    
    # EX.1: python123*
    # [Ture, True, False, True, True] = False

    # EX.2: Python123*
    # [True, True, True, True, True] = True

    if False in list1:
        print("Lösenordet duger inte, vänligen försök igen!")
        return False
    else:
        print("Bra Val!")
        return True




def main():
    var_1 = True
    while var_1:
        input_value = input("Enter your password: ")
        if validate_pwd(input_value) == True:
            var_1 = False
        else:
            var_1 = True



if __name__ == "__main__":
    main()
