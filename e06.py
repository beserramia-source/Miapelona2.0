monto=0
billetes1000=0
billetes200=0
resto=0
restofinal=0

monto= int(input("¿cuanto dinero quisiera sacar?"))
          
billetes1000=(monto/1000)
resto=(monto%200)
          
print("billetes de 1000", billetes1000)
print("billetees de 200", billetes200)
print("dinero no entregado", restofinal)




