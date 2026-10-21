"""
 Module de test et de démonstration pour l'analyse fréquentielle de lettres.

Ce script illustre le comptage et l'analyse de la fréquence des lettres minuscules
(de 'a' à 'z') présentes dans un message texte.

Fonctionnement :
    1. Initialise une séquence représentant un tableau de comptage codé sous forme
       de chaîne de caractères (26 alvéoles de 3 caractères, initialisées à "000").
    2. Parcourt le message converti en minuscules.
    3. Calcule l'indice ASCII de chaque caractère relatif à l'OFFSET ('a' = 0).
    4. Extrait, incrémente et réinjecte la quantité comptabilisée dans la séquence.
    5. Affiche le bilan des occurrences et des fréquences pour les lettres présentes.

Variables globales :
    OFFSET (int): Code ASCII de référence pour 'a' (97).
    step (int): Taille en caractères du bloc réservé au comptage de chaque lettre (3).
    seq (str): Chaîne stockant l'état des compteurs pour les 26 lettres.
    message (str): Texte source analysé.
"""

# Importation des fonctions nécessaires à l'analyse fréquentielle.
# get_count_value() : récupère la quantité associée à une lettre.
# refactoring_seq() : met à jour la séquence contenant les fréquences.
# display_analyse() : réalise le traitement final et affiche les résultats.
from analyse.function_analyse import (
    get_count_value,
    refactoring_seq,
    display_analyse
)


# --------------------------------------------------
# Déclaration des constantes et des variables
# --------------------------------------------------

# Code ASCII de la lettre 'a'.
# Cette valeur sert de référence pour calculer l'indice
# correspondant à chaque lettre minuscule.
OFFSET = 97

# Bornes utilisées pour extraire la quantité associée
# à une lettre dans la séquence.
start = 0
end = 0

# Chaque lettre est représentée par une chaîne de 3 caractères.
# Cette longueur permet de stocker une quantité sur 3 octets.
step = 3

# Initialisation de la séquence contenant les fréquences.
# Chaque lettre de l'alphabet dispose d'un emplacement de 3 caractères.
# La séquence contient donc 26 emplacements de 3 caractères.
seq = "000" * 26


# --------------------------------------------------
# Déclaration du message à analyser
# --------------------------------------------------

# Message utilisé pour réaliser le test de l'analyse fréquentielle.
message = "Bonjour Toto, comment allez vous aujourd'hui les jeunes?"

# Conversion du message en minuscules afin de traiter
# les lettres majuscules et minuscules de manière identique.
message = message.lower()


# --------------------------------------------------
# Parcours du message et comptage des lettres
# --------------------------------------------------

# Parcours de chaque caractère du message.
for c in message:

    # Conversion du caractère en indice numérique.
    # ord(c) retourne le code numérique du caractère.
    # La soustraction de OFFSET permet d'obtenir :
    # a -> 0, b -> 1, c -> 2, ..., z -> 25.
    indice = ord(c) - OFFSET

    # Vérification que le caractère est une lettre minuscule
    # comprise entre 'a' et 'z'.
    # Les espaces, les chiffres et les signes de ponctuation
    # ne sont donc pas pris en compte.
    if 0 <= indice <= 25:

        # Calcul de la position de début de l'emplacement
        # réservé à la lettre dans la séquence.
        start = indice * step

        # Calcul de la position de fin de cet emplacement.
        # La borne end n'est pas incluse lors de l'extraction.
        end = (indice + 1) * step

        # Extraction de la quantité actuellement enregistrée
        # pour la lettre correspondant au caractère c.
        value = get_count_value(seq, start, end)

        # Incrémentation du compteur : une occurrence
        # supplémentaire de cette lettre vient d'être détectée.
        value += 1

        # Mise à jour de la séquence avec la nouvelle quantité.
        # La fonction remplace l'ancienne valeur par la valeur
        # actualisée à l'emplacement correspondant à la lettre.
        seq = refactoring_seq(seq, value, start, end)


# --------------------------------------------------
# Analyse fréquentielle et affichage des résultats
# --------------------------------------------------

# Transmission du message, de la taille d'un emplacement,
# du code de référence et de la séquence des fréquences.
# La fonction réalise le traitement final et affiche
# les résultats de l'analyse fréquentielle.
display_analyse(message, step, OFFSET, seq)

