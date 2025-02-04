#Programme de gestion des étudiants et des notes

etudiants = []  # Création d’une liste vide
notes = []  # Liste pour stocker les notes des étudiants

def ajouter_etudiant(nom):
    etudiants.append(nom)

def supprimer_etudiant(nom):
    if nom in etudiants:
        etudiants.remove(nom)
    else:
        print(f"L'étudiant {nom} n'est pas dans la liste.")

def afficher_etudiants():
    if len(etudiants) == 0:
        print("Aucun étudiant enregistré.")
    else:
        print("Liste des étudiants :")
        for etudiant in etudiants:
            print(etudiant)

def saisir_notes():
    global notes
    if len(etudiants) == 0:
        print("Veuillez d'abord ajouter des étudiants avant de saisir des notes.")
        return

    notes.clear()  # Réinitialiser les notes
    for etudiant in etudiants:
        while True:
            try:
                note = float(input(f"Entrez la note de {etudiant} (entre 0 et 20) : "))
                if 0 <= note <= 20:
                    notes.append(note)
                    break
                else:
                    print("La note doit être comprise entre 0 et 20.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    afficher_statistiques_notes()

def afficher_statistiques_notes():
    if len(notes) == 0:
        print("Aucune note enregistrée.")
        return

    moyenne = sum(notes) / len(notes)
    note_max = max(notes)
    note_min = min(notes)
    au_dessus_moyenne = len([note for note in notes if note > moyenne])

    print("\n--- Résultats des notes ---")
    print(f"Nombre de notes saisies : {len(notes)}")
    print(f"Moyenne des notes : {moyenne:.2f}")
    print(f"Note la plus élevée : {note_max}")
    print(f"Note la moins élevée : {note_min}")
    print(f"Nombre d'élèves avec une note au-dessus de la moyenne : {au_dessus_moyenne}")

while True:
    print("\n1. Ajouter un étudiant")
    print("2. Supprimer un étudiant")
    print("3. Afficher tous les étudiants")
    print("4. Saisir les notes")
    print("5. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == '1':
        nom = input("Entrez le nom de l'étudiant : ")
        ajouter_etudiant(nom)
    elif choix == '2':
        nom = input("Entrez le nom de l'étudiant à supprimer : ")
        supprimer_etudiant(nom)
    elif choix == '3':
        afficher_etudiants()
    elif choix == '4':
        saisir_notes()
    elif choix == '5':
        print("Au revoir !")
        break
    else:
        print("Choix invalide")
