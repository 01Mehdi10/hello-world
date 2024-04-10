def nomMois(n):
    mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

    if 1 <= n <= 12:
        return mois[n - 1]
    else:
        return None

# Demander à l'utilisateur de saisir le numéro du mois jusqu'à ce qu'une valeur valide soit fournie.
while True:
    print("Entre le numéro du mois pour afficher son nom : ", end=" ")
    n = int(input())
    m = nomMois(n)

    if m is not None:
        print("Le mois est : ", m)
        break
    else:
        print("Tu n'as pas entré un numéro valide ! Réessaye.")
        