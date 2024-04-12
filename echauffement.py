import sys 

def afficher_rectangle(largeur, hauteur):
    coin = "0"
    horizontal = "--"
    vertical = "|"
    
    for i in range(hauteur):
        if i == 0 or i == hauteur - 1:
            print(coin + horizontal * (largeur - 2) + coin)
        else:
            print(vertical + "  " * (largeur - 2) + vertical)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilisation : échauffement")
        sys.exit(1)
    
    try:
        largeur = int(sys.argv[1])
        hauteur = int(sys.argv[2])
        afficher_rectangle(largeur, hauteur)
    except ValueError:
        print("Erreur : les arguments doivent etre des nombres entiers entiers pour la largeur et la hauteur.")
        sys.exit(1)