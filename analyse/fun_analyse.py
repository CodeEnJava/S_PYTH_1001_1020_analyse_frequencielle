# déclaration des variables
OFFSET = 97
start = 0
end = 0
step = 3 # 3 octets pour définir la quantité
# la variable qui va contenir le couple (lettre ,nbfois)
seq = "000"*26
print(seq)

message = "Bonjour Toto, comment allez vous aujourd'hui les jeunes?"
# mise en minuscule
message = message.lower()

for c in message:
    # bloc pour le traitement de boucle for
    # on considère que a est en 0
    indice = ord(c) - OFFSET

    # on traite uniquement les lettre minuscules
    if 0 <= indice <= 25:
        # le bloc du alors
        start = indice * step
        end = (indice +1) * step
        # extraction de la quantité associé au caractère c
        str_value = seq[start:end]

        value = int(str_value)
        value += 1
        str_value = str(value)

        #Normalisation

        if len(str_value) == 1:
            str_value = "00" + str_value
        elif len(str_value) == 2:
            str_value = "0" + str_value

        # préparer pour injecter la str_value
        left_seq = seq[0:start]
        right_seq = seq[end:]

        seq = left_seq + str_value + right_seq

print(seq)

# Traitement fréquencielle et affichage
for index in range(0,len(seq),step):
    str_value = seq[index:index+ step]
    value = int(str_value)
    if value > 0:
        frequence = value/len(message) *100 # exprimé en %
        print(f" Le caractère : {chr(int(index/step)+OFFSET)}"
              f" occurence :{value}"
              f" fréquence : {frequence:.4} en %")
