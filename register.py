
#Introduccion de datos
name = input("your name ")
age = int(input("your age "))
weight = input("type weight ")
monthlyPaymend = input("mensualidad ")
user = input("type new user ")
password = input("type new password ")
#los datos recolectados se guardan en un diccionario para ser mostrados mas adelange
data = {
            "nick": name,
            "edad": age,
            "peso": weight,
            "mensualidad": monthlyPaymend
        }
print("--------------------------")
#Se iniciara seción 
userName = input("User ")
pas = input("password ")
#Comprobación del usuario, si es correcto, pasara a la siguiente comprobación
#si no, nos mandara un mensaje de incorrecto
if user == userName:
    #Se comprobara si la contraseña es correcta
    #si es correcta, nos mostrara un mensae de bienvenida y nuestros datos
    if pas == password:
        print("Bienvenido")
        for datos in data:
            print(data[datos])
    else:
        #si es incorrecta, nos mostrara un mensaje
        print("password incorrect")
else:
    print("User invalid")

