resultado=""
desp=0
frase= input("ingresar frase: ")
for caracter in frase:
    if caracter.isalpha() == True:
        valor_ascii=ord(caracter)
        if valor_ascii >=97 and valor_ascii <=122:
           limite=ord("m")
        elif valor_ascii >= 65 and valor_ascii <=91:
           limite=ord("M")
        valor_ascii+=3
        if valor_ascii >=limite:
           valor_ascii-=26
        valor_ascii=chr(valor_ascii)
    else:
         valor_ascii=chr(valor_ascii)
    resultado+=valor_ascii
print(resultado)
        