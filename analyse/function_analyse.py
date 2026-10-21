def nomalize_str(str_value):
    """Formatte une chaîne représentant un nombre sur 3 caractères en ajoutant des zéros à gauche.

    Args:
        str_value (str): La chaîne de caractères à normaliser.

    Returns:
        str: La chaîne complétée avec des zéros à gauche pour atteindre 3 caractères (ex: '1' -> '001').
    """
    str_val = str_value
    if len(str_val) == 1:
        str_val = "00" + str_val
    elif len(str_val) == 2:
        str_val = "0" + str_val

    return str_val


def get_count_value(_seq, _start, _end):
    """Extrait une sous-chaîne d'une séquence et la convertit en entier.

    Args:
        _seq (str): La séquence source de caractères.
        _start (int): L'index de début de la sous-chaîne.
        _end (int): L'index de fin de la sous-chaîne.

    Returns:
        int: La valeur numérique entière extraite de la portion de séquence.
    """
    _value = _seq[_start:_end]
    return int(_value)


def refactoring_seq(seq, _value, start, end):
    """Remplace une portion de la séquence par la valeur formatée sur 3 caractères.

    Args:
        seq (str): La séquence d'origine à modifier.
        _value (int | str): La valeur à insérer, qui sera normalisée sur 3 caractères.
        start (int): L'index de début de la zone à remplacer.
        end (int): L'index de fin de la zone à remplacer.

    Returns:
        str: La nouvelle séquence reconstruite avec la valeur insérée.
    """
    # Normalisation
    str_value = str(_value)
    str_value = nomalize_str(str_value)

    left_seq = seq[0:start]
    right_seq = seq[end:]
    return left_seq + str_value + right_seq


def display_analyze_aux(_message, _value, step, offset, _index):
    """Affiche les détails de fréquence et d'occurrence pour un caractère spécifique.

    Args:
        _message (str | Sized): Le message complet analysé, utilisé pour calculer la longueur totale.
        _value (int): Le nombre d'occurrences comptabilisées.
        step (int): Le pas d'incrémentation utilisé dans le parcours.
        offset (int): Le décalage utilisé pour déterminer le code du caractère ASCII/Unicode.
        _index (int): L'index actuel dans la séquence parcourue.

    Returns:
        None
    """
    frequence = _value / len(_message) * 100  # exprimé en %
    print(f" Le caractère : {chr(int(_index / step) + offset)}"
          f" occurence :{_value}"
          f" fréquence : {frequence:.4} en %")


def display_analyse(_message, _step, offset, _seq):
    """Parcourt la séquence analysée et affiche les fréquences des caractères présents.

    Args:
        _message (str | Sized): Le message source dont on calcule les fréquences.
        _step (int): La taille des blocs représentant un compteur dans la séquence.
        offset (int): Le décalage de code pour la reconversion des caractères.
        _seq (str): La séquence codée contenant les comptes d'occurrences.

    Returns:
        None
    """
    for index in range(0, len(_seq), _step):
        value = get_count_value(_seq, index, index + _step)
        if value > 0:
            display_analyze_aux(_message, value, _step, offset, index)

