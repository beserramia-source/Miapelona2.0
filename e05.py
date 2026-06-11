caramelos=0
estudiantes=0
cadaestudiante=0
sobran=0

caramelos=int(input("ingrese la cantidad de caramelos"))
estudiantes=int(input("ingrese la cantidad de estudiantes"))

cadaestudiante=(caramelos/estudiantes)
sobran=(caramelos%estudiantes)

print("a cada estudiante le tocan", cadaestudiante)
print("sobran", sobran)

