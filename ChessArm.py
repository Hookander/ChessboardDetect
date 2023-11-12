from chessboard_detect import *
import numpy as np

"""
But global: étudier les différences entre 2 photos d'échiquier pour savoir quelle pièce a bougé en connaissant
    la position précédente, et l'update, pour potentiellement discuter avec une API type stockfish.. etc

"""

#pour convertir en noir et blanc = val = 0.30*R + 0.59*G + 0.11*B
old_color_array = getColorArray(34, False , False, False)
new_color_array = getColorArray(35, False , True, False) #! juste pour le test

old_rb, new_rb = np.zeros([64]), np.zeros([64])4
old_rb[:] = old_color_array[:, 0]*0.30 + old_color_array[:, 1]*0.59 + old_color_array[:, 2] * 0.11
new_rb[:] = new_color_array[:, 0]*0.30 + new_color_array[:, 1]*0.59 + new_color_array[:, 2] * 0.11

#print(old_rb[0])
diff_mean = np.abs(old_rb - new_rb)
#print(old_color_array[12:14])
#print(new_color_array[12:14])
print(diff_mean)
print(np.argmax(diff_mean))
print(diff_mean[45])
#Deux valeurs maximales potentielle -> la case qui n'a plus de pièce et peut-être la case de destination
#SAUF si une pièce a été mangée


