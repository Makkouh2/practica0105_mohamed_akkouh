x=float(input("Cantidad dinero depositada"))
interes= 0.04 
p= x * interes
p2= round(p,2)
s= (x+p2) * interes
s2= round(s,2)
t= (x+s2+p2) * interes
t2= round(t,2)
print('el primer año has ganado:',p2)
print('el segundo año has ganado:',s2)
print('el tercer año has ganado:',t2)