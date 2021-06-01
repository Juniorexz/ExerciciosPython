from random import choice
import string


'''string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 0123456789
string.punctuation # <=>?@[\]^_`{|}~.
'''

tamanho = 2
valores = string.ascii_lowercase
senha = ''
for i in range(tamanho):#range = tamanho
  senha += choice(valores)

print(senha)