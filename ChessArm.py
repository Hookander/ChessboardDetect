from chessboard_detect import *
import numpy as np

"""
But global: étudier les différences entre 2 photos d'échiquier pour savoir quelle pièce a bougé en connaissant
    la position précédente, et l'update, pour potentiellement discuter avec une API type stockfish.. etc

"""

"""
nouvelle idée à implémenter : on pondère tt les coeffs de l'image,
quitte à la mettre en noir et blanc dès le début, pour que la valeur moyenne soit fixée,
peut permettre de corriger un peu et d'améliorer

On peut aussi, comme on connait la forme de l'échiquier et la position des cases blanches/noires,
relever leurs couleurs pour avoir un idée de l'éclairage, et même déterminer s'il y a une pièce dessus
"""


old_color_array, _, _ = getColorArray(60, False , False, False)
new_color_array, better_warped_img, milieux = getColorArray(51, False , False, False)




old_rb, new_rb = np.zeros([64]), np.zeros([64])

#Black and white conversion
old_rb[:] = old_color_array[:, 0]*0.30 + old_color_array[:, 1]*0.59 + old_color_array[:, 2] * 0.11
new_rb[:] = new_color_array[:, 0]*0.30 + new_color_array[:, 1]*0.59 + new_color_array[:, 2] * 0.11

#Normalization
old_rb = old_rb / np.max(old_rb)
new_rb = new_rb / np.max(new_rb)

#print(old_rb[0])
diff_mean = np.abs(old_rb - new_rb)
#print(old_color_array[12:14])
#print(new_color_array[12:14])

print(diff_mean)
max_diff = np.argmax(diff_mean)
print(max_diff)

plt.imshow(better_warped_img)
plt.scatter((milieux[max_diff][0]), (milieux[max_diff][1]))
plt.show()
#print(diff_mean[23])
#Deux valeurs maximales potentielle -> la case qui n'a plus de pièce et peut-être la case de destination
#SAUF si une pièce a été mangée


