# Séance Python — Analyse fréquentielle d'un texte

## 1. Présentation

Cette séance pédagogique propose de réaliser une première analyse fréquentielle d'un texte en Python.

L'objectif est de compter le nombre d'occurrences de chaque lettre de l'alphabet, puis de calculer la fréquence d'apparition de chaque lettre dans le message étudié.

Le traitement repose sur une séquence de caractères qui stocke les compteurs d'occurrences. Chaque lettre de l'alphabet dispose d'un emplacement de trois caractères.

Le programme utilise plusieurs fonctions afin de répartir les traitements et de faciliter la compréhension du code.

## 2. Objectifs pédagogiques

À l'issue de cette séance, vous serez capable de :

- Parcourir une chaîne de caractères avec une boucle `for`.
- Convertir un texte en minuscules avec la méthode `lower()`.
- Convertir un caractère en valeur numérique avec la fonction `ord()`.
- Reconnaître les lettres de l'alphabet à l'aide d'une condition `if`.
- Manipuler des chaînes de caractères et extraire des sous-chaînes.
- Utiliser le découpage d'une chaîne avec la syntaxe `[start:end]`.
- Convertir une chaîne numérique en entier avec `int()`.
- Définir et appeler des fonctions Python.
- Transmettre des paramètres à une fonction et récupérer sa valeur de retour.
- Calculer une fréquence en pourcentage.
- Formater une valeur numérique pour afficher un résultat lisible.

## 3. Principe de l'analyse fréquentielle

L'analyse fréquentielle consiste à déterminer combien de fois chaque lettre apparaît dans un texte.

Pour chaque lettre, le programme calcule :

- **Le nombre d'occurrences** : nombre de fois où la lettre apparaît dans le message.
- **La fréquence** : proportion des occurrences de cette lettre par rapport au nombre total de caractères du message, exprimée en pourcentage.

La formule utilisée est :

\[
\text{Fréquence} =
\frac{\text{Nombre d'occurrences}}{\text{Longueur du message}}
\times 100
\]

Dans cette version du programme, les lettres sont comptabilisées sans distinction entre majuscules et minuscules. Les espaces, les chiffres et les signes de ponctuation ne sont pas comptabilisés comme des lettres.

Attention : le dénominateur utilisé est la longueur totale du message, espaces et ponctuation compris.

## 4. Organisation des fichiers

Le projet est organisé autour d'un module de traitement et d'un module de test.

```text
projet/
│
├── analyse/
│   ├── __init__.py
│   └── function_analyse.py
│
└── test_analyse.py
```

- `function_analyse.py` contient les fonctions utilisées pour effectuer l'analyse fréquentielle.
- `test_analyse.py` contient le scénario de test qui initialise les données, parcourt le message, compte les lettres et affiche les résultats.
- `__init__.py` permet de matérialiser le dossier `analyse` comme un package Python. Selon la version de Python et le mode d'organisation du projet, ce fichier peut être facultatif.

Adaptez les noms des fichiers à ceux réellement présents dans votre dépôt.

## 5. Description des fonctions

### 5.1. `nomalize_str(str_value)`

**Rôle :** normaliser une chaîne numérique afin de représenter une valeur sur trois caractères.

La fonction ajoute des zéros à gauche lorsque la chaîne contient un ou deux caractères.

Exemples :

| Valeur initiale | Valeur normalisée |
|---|---|
| `"1"` | `"001"` |
| `"12"` | `"012"` |
| `"125"` | `"125"` |

Cette représentation permet de conserver une longueur fixe pour chaque compteur dans la séquence.

Remarque : le nom actuel de la fonction est `nomalize_str`. Une correction orthographique vers `normalize_str` ou `normalise_str` est possible, à condition de mettre à jour tous les appels concernés.

### 5.2. `get_count_value(_seq, _start, _end)`

**Rôle :** extraire le compteur associé à une lettre et convertir sa représentation en chaîne en une valeur entière.

Les paramètres sont :

- `_seq` : séquence contenant l'ensemble des compteurs.
- `_start` : indice de début de la zone à extraire.
- `_end` : indice de fin, non inclus dans l'extraction.

Exemple :

```python
seq = "003012007"

value = get_count_value(seq, 3, 6)

print(value)  # 12
```

La fonction extrait `"012"` et retourne l'entier `12`.

### 5.3. `refactoring_seq(seq, _value, start, end)`

**Rôle :** reconstruire la séquence en remplaçant le compteur d'une lettre par sa nouvelle valeur.

La fonction :

1. Convertit la valeur en chaîne.
2. Normalise cette chaîne sur trois caractères.
3. Récupère la partie située avant le compteur.
4. Récupère la partie située après le compteur.
5. Assemble les trois parties pour produire une nouvelle séquence.

Exemple :

```python
seq = "003000007"

seq = refactoring_seq(seq, 12, 3, 6)

print(seq)  # 003012007
```

La chaîne étant immuable en Python, la fonction construit une nouvelle chaîne plutôt que de modifier directement la chaîne d'origine.

### 5.4. `display_analyze_aux(_message, _value, step, offset, _index)`

**Rôle :** calculer et afficher les informations relatives à une lettre.

La fonction reçoit le nombre d'occurrences, calcule la fréquence en pourcentage et identifie la lettre correspondante.

La lettre est retrouvée grâce à la formule :

```python
chr(int(_index / step) + offset)
```

La fréquence est calculée avec :

```python
frequence = _value / len(_message) * 100
```

Le formatage `:.4f` permet d'afficher quatre chiffres après la virgule.

### 5.5. `display_analyse(_message, _step, offset, _seq)`

**Rôle :** parcourir la séquence des compteurs et afficher les résultats de l'analyse.

La fonction parcourt la séquence par blocs de trois caractères. Pour chaque bloc :

1. Elle extrait le compteur.
2. Elle vérifie si le compteur est supérieur à zéro.
3. Si la lettre apparaît dans le message, elle appelle `display_analyze_aux()`.

Cette organisation évite d'afficher les lettres dont le nombre d'occurrences est nul.

## 6. Fonctionnement du module de test

Le module de test réalise les opérations suivantes.

### Étape 1 — Initialiser les paramètres

```python
OFFSET = 97
step = 3
seq = "000" * 26
```

- `OFFSET = 97` correspond au code de la lettre `a`.
- `step = 3` définit la taille d'un emplacement de compteur.
- `seq = "000" * 26` initialise les 26 compteurs de l'alphabet à zéro.

La séquence possède donc une longueur initiale de 78 caractères.

### Étape 2 — Préparer le message

```python
message = "Bonjour Toto, comment allez vous aujourd'hui les jeunes?"
message = message.lower()
```

Le texte est converti en minuscules pour éviter de distinguer les majuscules des minuscules pendant le comptage.

### Étape 3 — Parcourir les caractères

```python
for c in message:
    indice = ord(c) - OFFSET
```

La boucle examine successivement chaque caractère du message.

La conversion numérique permet d'associer les lettres aux indices de l'alphabet :

| Lettre | Code avec `ord()` | Indice calculé |
|---|---:|---:|
| `a` | 97 | 0 |
| `b` | 98 | 1 |
| `c` | 99 | 2 |
| `z` | 122 | 25 |

### Étape 4 — Vérifier et compter les lettres

```python
if 0 <= indice <= 25:
    start = indice * step
    end = (indice + 1) * step

    value = get_count_value(seq, start, end)
    value += 1

    seq = refactoring_seq(seq, value, start, end)
```

La condition vérifie que le caractère correspond à une lettre comprise entre `a` et `z`.

Le programme calcule ensuite la zone de stockage de cette lettre, récupère son compteur, l'incrémente et reconstruit la séquence.

### Étape 5 — Afficher les résultats

```python
display_analyse(message, step, OFFSET, seq)
```

Une fois le parcours terminé, le programme transmet le message et les compteurs à la fonction d'affichage.

Le résultat indique les lettres présentes, leurs nombres d'occurrences et leurs fréquences calculées.

## 7. Exécution du programme

Depuis l'environnement de développement, exécutez le fichier de test qui contient le parcours du message.

Vérifiez notamment :

- Que le programme ne comptabilise pas les espaces et la ponctuation comme des lettres.
- Que chaque occurrence d'une lettre augmente son compteur de un.
- Que les compteurs restent représentés sur trois caractères.
- Que seules les lettres présentes dans le texte sont affichées.
- Que les fréquences sont calculées et présentées en pourcentage.

## 8. Points de vigilance

### Limite de stockage

Chaque compteur est stocké sur trois caractères. Cette représentation permet de compter jusqu'à 999 occurrences pour une lettre.

Si un compteur dépasse cette limite, la fonction de normalisation actuelle ne garantit plus le maintien d'un emplacement de trois caractères. La séquence pourrait alors être corrompue.

### Calcul de la fréquence

Le programme divise le nombre d'occurrences par la longueur totale du message. Les espaces et les signes de ponctuation sont donc inclus dans le dénominateur.

Si l'objectif est de calculer la fréquence d'une lettre parmi les seules lettres de l'alphabet, il faudra utiliser comme dénominateur le nombre total de lettres comptabilisées.

### Caractères accentués

Le traitement actuel reconnaît uniquement les lettres de `a` à `z`. Les caractères accentués, tels que `é`, `è` ou `à`, ne sont pas comptabilisés.

Une évolution possible consisterait à normaliser le texte avant le comptage afin de traiter les accents selon une règle définie.

## 9. Pistes d'amélioration

Pour aller plus loin, vous pouvez :

1. Ajouter un compteur du nombre total de lettres analysées.
2. Comparer les fréquences obtenues avec celles d'un texte de référence.
3. Afficher les résultats dans l'ordre décroissant des fréquences.
4. Étudier le traitement des caractères accentués.
5. Améliorer la gestion des compteurs dépassant 999 occurrences.
6. Comparer cette représentation par chaîne avec une solution utilisant un dictionnaire Python.

## 10. Conclusion

Cette séance permet de mettre en pratique les chaînes de caractères, les boucles, les conditions, les conversions de types et les fonctions Python.

Elle introduit également la séparation des traitements : récupération d'une valeur, mise à jour des données, calcul des fréquences et affichage des résultats.

La réalisation constitue une première approche de l'analyse de données textuelles et prépare à l'utilisation de structures de données plus adaptées, comme les dictionnaires.
