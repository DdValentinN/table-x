print("")
print("TABLES DE MULTIPLICATION : ")

n=int(input("Choisis la table que tu souhaites étudier(entre 0 et 10) :"))
def table_de_multiplication_de(n,min=1,max=10):
    if n > max:
        print("ERREUR: Vous devez rentrer un CHIFFRE compris entre 0 et 10 ")
        return

    for i in range(min,max+1):
        print("Voici la table de multiplication de", n)
        print(i,"x",n,"=", i*n)

table_de_multiplication_de(n,0,10)