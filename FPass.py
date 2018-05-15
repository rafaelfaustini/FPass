lista = []
print("\n\t\t\tFaustini Password Gen")
print("/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/ ")

print("\tCaso não saiba alguma informação, deixe em branco e pressione enter\n ")
print("/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/\n ")


n= input("Qual o nome do alvo ? ")
n=n.replace(" ","")
lista.append(n)


def quantidade(q,p):
  global lista
  quant= input(q)

  if quant!="" and quant!="0":
    for i in range (0, int(quant)):
      x= input(p+str(i+1)+' ')
      x= x.replace(" ","")
      if len(x)>= 8 and len(x)<= 30:
        lista.append(x)
def datas(q,p):
  quant= input(q)
  

  if quant!="" and quant!="0":
    for i in range (0, int(quant)):
      st= input(p+str(i+1)+' ')
      x= st
      x= x.replace(" ","")
      lista.append(x)
      st= st[-2:] #yy
      st = st.replace(" ","")
      lista.append(st)
      
      st= st[-3:] #yyy
      st = st.replace(" ","")
      lista.append(st)

      st= st[-4:] #yyyy
      st = st.replace(" ","")
      lista.append(st)

      st= st[1:2] #xd
      st = st.replace(" ","")
      lista.append(st)

      st= st[3:4] #xm
      st = st.replace(" ","")
      lista.append(st)

      st= st[2:] #dd
      st = st.replace(" ","")
      lista.append(st)

      st= st[2:4] #mm
      st = st.replace(" ","")
      lista.append(st)

def pessoa():
  global lista
  quant= input("Quantas pessoas ligadas ao alvo, deseja inserir ? ")
  for i in range (0, int(quant)):
    s=input(" Nome da pessoa "+i+" ").lower
    lista.append(s)
    quantidade("Quantas datas ligadas entre pessoa 1 e o alvo você possui ?","Qual a data (DDMMAAAA) ")




quantidade("Quantos sobrenomes você tem do alvo (Caso nenhum deixe em branco) ", "Qual o sobrenome ")
datas("Quantas outras datas ligadas ao alvo você tem DDMMAAAA ? ", "Qual a data ")


def shuffle():
  global lista
  v=[1]
  for i in range(0,len(lista)):
    v[0]=lista[i]
    for j in range(0,len(lista)-1):
      lista.append(lista[j]+v[0])

def leet():
  global lista
  for i in range (0, len(lista)):
    leetmsg=lista[i]
    if 'a' or 'e' or 'i' or 'o' or 't' or 's' in leetmsg:
      leetmsg = leetmsg.replace('a', str(4))
      leetmsg = leetmsg.replace('e', str(3))
      leetmsg = leetmsg.replace('i', str(1))
      leetmsg = leetmsg.replace('o', str(0))
      leetmsg = leetmsg.replace('s', '$')
      leetmsg = leetmsg.replace('you', 'j00')
      lista.append(leetmsg)
      if 't' in leetmsg:
        leetmsg = leetmsg.replace('t', str(7))
        lista.append(leetmsg)

def gerar():
  global n
  global lista
  lista = list(filter(None, lista))
  a = set(lista)
  seen = set()
  result = []
  for item in a:
    if item not in seen:
        seen.add(item)
        result.append(item)
  

  file = open(n+'.txt', 'w')
  lista_set= set(result)
  for item in lista_set:
    file.write("%s\n" % item)

shuffle()
leet()

gerar()

stringg="[+] "+str(len(lista))+' senhas geradas'
print(stringg)



input('Press ENTER to exit')

