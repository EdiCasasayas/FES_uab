###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.
print("\nExercici 2:")
numero = 1
suma_parells = 0
while numero <= 20:
  if numero % 2 == 0:
    suma_parells += numero
  numero += 1


# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.
numero=int(input("Donam un numero:"))
multi=0
while multi<=10:
    resultat=multi*numero
    print(f"{numero}x{multi} ={resultat}")
    multi+=1


# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.
num=int(input("Donam un numero enter:"))
suma=0

while num!=0:
    suma+=num
    num=int(input("Donam un numero enter:"))

print(f"Suma total de els numero introduits={suma}")   

# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.

# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.
termes=int(input("Quant numero de la sequencia de Fibonacci vols veuere:"))
a=0
b=1
com=0
while com<=termes:
    print(a)
    seguent=a+b
    a=b
    b=seguent
    com+=1

print(f"La suma total es de {a}")    




# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.

num=int(input("Digam un numero per adivinar el numero secret:"))

secret=7

while num!=secret:
    if num>secret:
        print("El numero es mes gran que el secret")
    else:
        print("El numero es mes petit que el secret")

    num=int(input("Torna a provar un altre numero:"))



print(f"Has endivinat el numero, que era el {secret}")    

