

from PIL import Image
import numpy as np
import string


imagem = Image.open("polig1.jpg")
#Rotulacao = np.array(imagem,dtype=int)
Rotulacao = np.array(imagem, dtype=str) # tranforma a imagem numa matriz de Character





'''
Rotulacao = np.array([['255', '0', '0', '255', '255'],
                        ['255', '0', '255', '0', '255'],
                        ['255', '0', '0', '0', '255'],
                        ['255', '255', '255', '255', '255'],
                        ['255', '255', '255', '255', '255']])
'''

print("Matriz da Imagem:\n\n",Rotulacao)

#x,y = 5,5

x,y = Rotulacao.shape
print( x,y)

'''
for i in range(x):
    for j in range(y):
        if(Rotulacao[i,j] < 127):
            Rotulacao[i,j] = 0
        else:
            Rotulacao[i, j] = 255

nova_imagem = Image.fromarray(Rotulacao.astype('uint8'))
nova_imagem.save("nova.jpg")

'''
#alfabeto = ABCDEFGHIJKLMNOPQRSTUVWXYZ

#Rotulacao = np.zeros((x1,y1),dtype=int)
#print("\n\nImagem Ampliada\n",Rotulacao)]

alfabeto = 'A'


equivalencias1 = []
equivalencias2 = []

for i in range(x):
    for j in range(y):

        if (ord(alfabeto) == 90): #se chegar no Z, volta pro A
            alfabeto += 'A'
        if(Rotulacao[i,j] != '255'): #se p = 1
            if(Rotulacao[i,j-1] == '255' and Rotulacao[i-1,j] == '255'): #se r e s forem 0
                Rotulacao[i,j] = alfabeto
                alfabeto = chr(ord(alfabeto) + 1)
            elif(Rotulacao[i,j-1] != '255' and Rotulacao[i-1,j] != '255'): # se r e s forem 1
                if(Rotulacao[i,j-1] != Rotulacao[i-1,j]): # tem label diferente
                    Rotulacao[i, j] = Rotulacao[i-1,j]
                    equivalencias1.append(Rotulacao[i-1,j])
                    equivalencias2.append(Rotulacao[i,j-1])
                else:
                    Rotulacao[i, j] = Rotulacao[i,j-1]
            elif(Rotulacao[i,j-1] != '0' and  Rotulacao[i-1,j] == '255'): # se r ou s forem 1
                Rotulacao[i, j] = Rotulacao[i,j-1]
            elif(Rotulacao[i,j-1] == '255' and  Rotulacao[i-1,j] != '0'):
                Rotulacao[i, j] = Rotulacao[i-1,j]

        #Rotulacao[i, j] = alfabeto

#Equivalencias
k = 0
print ("equival", equivalencias1.__len__())

while(equivalencias1.__len__() > 0):
    for i in range(x):
        for j in range(y):
                if(Rotulacao[i, j] == equivalencias2.__getitem__(k)):
                    Rotulacao[i, j] = equivalencias1.__getitem__(k)

    equivalencias2.__delitem__(k)
    equivalencias1.__delitem__(k)
    #k+=1

for i in range(x):
    for j in range(y):
        print(Rotulacao[i, j])

#print("\n\nRotulada\n",Rotulacao)

