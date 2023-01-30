# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

medida = float(input('Uma distância em Metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}metros corresponde a:')
print(f''' {km:.2f}\033[0;35mkm\033[m 
 {hm:.2f}\033[0;35mhm\033[m
 {dam:.2f}\033[0;35mdam\033[m
 {dm:.2f}\033[0;35mdm\033[m 
 {cm:.2f}\033[0;35mcm\033[m 
 {mm:.2f}\033[0;35mmm\033[m''')