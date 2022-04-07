


def codage_hamming(bits):
    liste_7bits = [0]*7
    #bits de message
    i = 0
    for j in 4:
        liste_7bits[j] = bits[1]
    
    # on ajoute les bits de controlle
    liste_7bits[4] = bits[0] ^ bits[1] ^ bits[3]
    liste_7bits[5] = bits[0] ^ bits[2] ^ bits[3]
    liste_7bits[6] = bits[1] ^ bits[2] ^ bits[3]
    
    return(liste_7bits)
print(codage_hamming([1, 0, 0, 0]))


def decodage_hamming(bits):
    ## calcul bits de controle
    p1 = bits[2] ^ bits[4] ^ bits[6]
    p2 = bits[2] ^ bits[5] ^ bits[6]
    p3 = bits[4] ^ bits[5] ^ bits[6]
    ## position erreur si il y en a une (0 sinon)
    num = int(p1 != bits[4])*4 + int(p2 != bits[5])*2 + int(p3 != bits[6])

    if (num == 3):
        bits[0] = int(not bits[0])
    if (num == 5):
        bits[1] = int(not bits[1])
    if (num == 6):
        bits[2] = int(not bits[2])
    if (num == 7):
        bits[3] = int(not bits[3])
    return bits[:4]

print(decodage_hamming([1, 1, 1, 0, 0, 0, 0]))
print(decodage_hamming([1, 1, 1, 0, 1, 0, 0]))