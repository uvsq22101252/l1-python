


def codage_hamming(bits):
    liste_7bits = [0]*7
    #bits de message
    i = 0
    for j in [2, 4, 5, 6]:
        liste_7bits[j] = bits[1]
        i += 1
    # on ajoute les bits de controlle
    liste_7bits[0] = bits[0] ^ bits[1] ^ bits[3]
    liste_7bits[1] = bits[0] ^ bits[2] ^ bits[3]
    liste_7bits[3] = bits[1] ^ bits[2] ^ bits[3]
    
    return(liste_7bits)
print(codage_hamming([1, 0, 0, 0]))


def decodage_hamming(bits):
    ## calcul bits de controle
    p1 = bits[2] ^ bits[4] ^ bits[6]
    p2 = bits[2] ^ bits[5] ^ bits[6]
    p3 = bits[4] ^ bits[5] ^ bits[6]
    ## position erreur
    num = int(p1 != bits[0])+ int(p2 != bits[1])*2 + int(p3 != bits[3])*4

    if num in [3,5,6,7]:
        #on remplace bits[num-1] par 0 s'il valait 1 et par 1 si il valait 0
        bits[num-1] = int(not bits[num -1])
        print("corection d'un pixel corrompu en position "+ str(num) + "\n")
        return [bits[2],bits[4], bits[5],bits[6]]

print(decodage_hamming([1,1,1,0,0,0,0]))
print(decodage_hamming([1,1,1,0,1,0,0]))