list = []
print("\n\t\t\tFaustini Password Gen")
print("/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/ ")

print("\tCaso não saiba alguma informação, deixe em branco e pressione enter\n ")
print("/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/\n ")


n= input("Qual o nome do alvo ? ")
n=n.replace(" ","")
list.append(n)

def quantidade(q,p):
  quant= input(q)

  if quant!="" and quant!="0":
    for i in range (0, int(quant)):
      x= input(p+str(i+1)+' ')
      x= x.replace(" ","")
      list.append(x)
def datas(q,p):
  quant= input(q)
  

  if quant!="" and quant!="0":
    for i in range (0, int(quant)):
      st= input(p+str(i+1)+' ')
      x= st
      x= x.replace(" ","")
      list.append(x)
      st= st[-2:] #yy
      st = st.replace(" ","")
      list.append(st)
      
      st= st[-3:] #yyy
      st = st.replace(" ","")
      list.append(st)

      st= st[-4:] #yyyy
      st = st.replace(" ","")
      list.append(st)

      st= st[1:2] #xd
      st = st.replace(" ","")
      list.append(st)

      st= st[3:4] #xm
      st = st.replace(" ","")
      list.append(st)

      st= st[2:] #dd
      st = st.replace(" ","")
      list.append(st)

      st= st[2:4] #mm
      st = st.replace(" ","")
      list.append(st)

def pessoa():
  quant= input("Quantas pessoas ligadas ao alvo, deseja inserir ? ")
  for i in range (0, int(quant)):
    s=input(" Nome da pessoa "+i+" ").lower
    list.append(s)
    quantidade("Quantas datas ligadas entre pessoa 1 e o alvo você possui ?","Qual a data (DDMMAAAA) ")




quantidade("Quantos sobrenomes você tem do alvo (Caso nenhum deixe em branco) ", "Qual o sobrenome ")
datas("Quantas outras datas ligadas ao alvo você tem DDMMAAAA ? ", "Qual a data ")


def shuffle():
  v=[1]
  for i in range(0,len(list)):
    v[0]=list[i]
    print(v)
    for j in range(0,len(list)-1):
      list.append(list[j]+v[0])

def leet():
  for i in range (0, len(list)):
    leetmsg=list[i]
    if 'a' or 'e' or 'i' or 'o' or 't' or 's' in leetmsg:
      leetmsg = leetmsg.replace('a', str(4))
      leetmsg = leetmsg.replace('e', str(3))
      leetmsg = leetmsg.replace('i', str(1))
      leetmsg = leetmsg.replace('o', str(0))
      leetmsg = leetmsg.replace('s', '$')
      leetmsg = leetmsg.replace('you', 'j00')
      list.append(leetmsg)
      if 't' in leetmsg:
        leetmsg = leetmsg.replace('t', str(7))
        list.append(leetmsg)

def gerar():
  file = open(list[0]+'.txt', 'w')
  list.sort()
  lista= set(list)
  for item in list:
    file.write("%s\n" % item)
  stringg="[+] "+str(len(lista))+' senhas geradas'
  print(stringg)
  print(lista)
shuffle()
leet()

gerar()




input('Press ENTER to exit')

