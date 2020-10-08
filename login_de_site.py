print('Bem vindo ao nosso site, para registra-se digite um nome e uma senha')
login = input('Login: ')
password = input('Password: ')
print('Agora, para continuar, confirme seus dados fornecidos')
confirm_login = input('Login: ')
confirm_password = input('Password: ')
if confirm_login == login and confirm_password == password:
  print('Agora você pode explorar o nosso site XD')
else:
  print('Parece que você errou, tente novamente o processo.')