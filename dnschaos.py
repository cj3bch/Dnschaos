import requests
import time

print (".....Bem vindo a DnsChaos.....\n")

L = ['cardt.php']
url = ("http://testphp.vulnweb.com/")

with open("wordlist.txt",'r') as wordlist:
 lercont = wordlist.readline()

try:
 requisicion = requests.get(url + L[0])
 result = requisicion.status_code
 
except Exception as erros:
    print ("encontrado o seguinte erro:",erros)

if result == 200:
  print ("diretorio encontrado:",requisicion)
else:
  print ("diretorio nao encontrado")


