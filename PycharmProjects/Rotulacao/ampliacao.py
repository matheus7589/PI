
from PIL import Image
import numpy as np


escala = 1

imagem = Image.open("terra.jpg")
#Rotulacao = np.array(imagem,dtype=int)
ampliacao = np.array(imagem, dtype=int)

x,y,z = ampliacao.shape
print(x,y,z)

x1 = x * escala
y1 = y * escala

nova_img = np.array((x1, y1), dtype=int)

for i in range(x1):
    for j in range(y1):
        bx = i/escala
        by = j/escala
        nova_img[i,j] = ampliacao[bx,by]

imagem_nova = Image.fromarray(nova_img.astype('uint8'))
imagem_nova.show()



