import z3

bdt = [z3.Real(f"{i:02}") for i in range(24)]
solveur = z3.Solver()

solveur.add(bdt[0] + bdt[0] + 11.0 == bdt[0] + 130.0) 
solveur.add(bdt[1] * 7.0 == bdt[1] + 396.0) 
solveur.add((bdt[2] + 2.0) * 3.0 - 2.0 == (bdt[2] - 17.0) * 4.0) 
solveur.add(bdt[3] == 67.0) 
solveur.add((bdt[4] * 5.0 - 2.0) * 5.0 - (bdt[4] + bdt[4] + 7.0) * 6.0 ==bdt[4] * 33.0 - 1132.0) 
solveur.add((bdt[5] + bdt[5]) / 3.0 == (bdt[5] + 44.0) / 3.0) 
solveur.add((bdt[6] * 8.0 + 15.0) * 0.1666666666666667 ==(bdt[6] + bdt[6] + 81.0) * 0.5) 
solveur.add((bdt[7] * 7.0) / 2.0 == bdt[7] * 3.0 + 23.5) 
solveur.add(bdt[8] == 110.0) 
solveur.add(bdt[9] == 104.0) 
solveur.add(bdt[10] == 48.0) 
solveur.add((bdt[12] == bdt[11]) , (bdt[11] == 108.0)) 
solveur.add(bdt[13] == bdt[14] / 2.0 - 1.0) 
solveur.add(bdt[14] == bdt[14] / 2.0 + 48.0) 
solveur.add(bdt[15] == 91.0)
solveur.add(0.0 - bdt[16] / 5.0 == 36.0 - bdt[16]) 
solveur.add(bdt[17] == 49.0) 
solveur.add(bdt[18] == 91.0) 
solveur.add(bdt[19] == (bdt[3] + bdt[20]) - 16.0) 
solveur.add((bdt[20] * 3.0 - 2.0) * 3.0 - (bdt[20] * 5.0 + 2.0) * 4.0 ==bdt[20] * -8.0 - 146.0) 
solveur.add(bdt[21] == (bdt[21] + bdt[21]) - 44.0) 
solveur.add(bdt[22] == 104.0) 
solveur.add(bdt[23] + bdt[23] + 6.0 == bdt[23] + 127.0) 

assert solveur.check() == z3.sat
m = solveur.model()
print(bdt)
mot = ''
for el in bdt:
    evaluation = m.evaluate(el)
    val = round(float(evaluation.as_fraction()))
    mot += chr(val)
flag = ''
for l in mot:
    flag += chr(ord(l)+4)
print(flag)