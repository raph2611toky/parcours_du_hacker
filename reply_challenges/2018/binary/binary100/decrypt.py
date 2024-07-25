def gen_table():
    table = []  # Initialise une liste vide pour stocker les valeurs générées
    for v6 in range(256):  # Boucle de 0 à 255 inclus
        if (v6 & 1):
            v7 = 0xFFFFA001
        else:
            v7 = 0
        v8 = v7 ^ (v6 >> 1)
        if (v6 & 1):
            v9 = 30720
        else:
            v9 = 20480
        if (v6 & 1):
            v10 = 10240
        else:
            v10 = 0
        v11 = v8 & 1
        if (v8 & 1):
            v10 = v9
        if (v6 & 1):
            v12 = 20480
        else:
            v12 = 0
        if (v6 & 1):
            v13 = 0xFFFFF001
        else:
            v13 = 0xFFFFA001
        if (not v11):
            v13 = v12
        v14 = v10 ^ 0xA001
        if (not ((v13 ^ (v6 >> 2)) & 1)):
            v14 = v10
        v15 = v14 ^ (v6 >> 3)
        v16 = v14 >> 1
        if (v15 & 1):
            v16 ^= 0xA001
        v17 = v16 ^ (v6 >> 4)
        v18 = v16 >> 1
        if (v17 & 1):
            v18 ^= 0xA001
        v19 = v18 ^ (v6 >> 5)
        v20 = v18 >> 1
        if (v19 & 1):
            v20 ^= 0xA001
        v21 = v20 ^ (v6 >> 6)
        v22 = v20 >> 1
        if (v21 & 1):
            v22 ^= 0xA001
        v23 = v22 ^ (v6 >> 7)
        v24 = v22 >> 1
        if (v23 & 1):
            v24 = v24 ^ 0xA001
        table.append(v24 & 0xffff)  # Ajoute la valeur finale à la liste 'table'
    return table  # Retourne la liste des valeurs générées
for t in gen_table():
    print(t)