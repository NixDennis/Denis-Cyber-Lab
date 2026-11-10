parola = input("Scrieti parola dumneavoastra: ")
punctaj = 5
if len(parola) < 8:
    print("Parola trebuie sa aiba cel putin 8 caractere.")
    punctaj -= 1

cntnr = 0
cntup = 0
cntlow = 0
cntspc = 0
for i in range(len(parola)):
    if parola[i].isdigit():
        cntnr += 1
    if parola[i].isupper():
        cntup += 1
    if parola[i].islower():
        cntlow += 1
    if not parola[i].isalnum():
        cntspc += 1

if cntup == 0:
    print("Parola trebuie sa contina cel putin o litera mare.")
    punctaj -= 1
if cntlow == 0:
    print("Parola trebuie sa contina cel putin o litera mica.")
    punctaj -= 1
if cntspc == 0:
    print("Parola trebuie sa contina cel putin un caracter special.")
    punctaj -= 1
if cntnr == 0:
    print("Parola trebuie sa contina cel putin o cifra.")
    punctaj -= 1

print("Punctajul parolei este: ", punctaj)

if punctaj <= 2:
    print("Parola este slaba.")
elif punctaj <= 4:
    print("Parola este medie.")
else:
    print("Parola este puternica.")
