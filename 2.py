#Segue um exemplo que remete à criação de uma variável e sequentemente dar um print

nome = 'Matheus Franco'         # Aqui armazenamos as variáveis
about = 'Student and Dev'
age = 20
_from = 'Brazil'
email = 'matheusmfranco.mf@gmail.com'

print(nome, about, age, _from, email)       #Aqui chamamos para que possam ser apresentadas ao usuário

#Podemos tambem fazer com que o usuário altere a variável atraves do prompt:

nome = input(' Digite seu nome: ')
about = input(' Digite sobre voce: ')
age = int(input(' Digite sua idade: '))
_from = input(' Digite o seu país de origem: ')
email = (' Digite o seu e-mail: ')

print(nome, about, age, _from, email) 