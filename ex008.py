# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

#valor = int(input('Digite um valor em metros '))
#c = valor * 100
#m = valor * 1000
#print('Este valor equivale á {} centímetros e {} milimetros '.format(c, m))
# km, hm, dam, m, dm, cm, mm
medida = float(input('Uma distância em Metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medidaa de {}m corresponde a {}km\n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(medida, km, hm, dam, dm, cm, mm))