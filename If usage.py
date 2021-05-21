  
Z = str(input("Escreva seu nome: "))
A = str(input("Escreva o nome do seu pai: "))
E = int(input("Digite sua idade: "))
print("Seu nome é: ",Z)
print("O nome de seu pai é: ",A)
print("Voce tem: ",E,"anos de idade")
if E <= 10 :
    print("Voce é criança!")

if E > 10 and  E <= 20 :
    print("Voce é quase adulto..")

if E > 20 and E <= 30 :
    print("Voce é adulto!")
    
input()