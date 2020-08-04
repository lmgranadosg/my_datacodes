# Funciones
# def funcion1():
#     print("Hola, esta es la primera función")
#     print("Bienvenido")

# def numeros(numero):
#     if numero == "1":
#         print("Es el número uno")
#         a = "1Hola"
#     elif numero == "2":
#         print("Es el número dos")
#         a = "2Hola"
#     elif numero == "3":
#         print("Es el número tres")    
#         a = "3Hola"
#     else:
#         print("Lo siento, no tengo más números")
#         a = "Null_Hola"
#     return a
# print(numeros("6"))

# def computepay(h,r):
#     if h <= 40.0:
#         pay = h*r
#     elif h > 40.0:
#         pay = 40.0*r + (h-40.0)*r*1.5
#     return pay

# hrs = input("Enter Hours:")
# rate = input("Enter Rate:")

# h = float(hrs)
# r = float(rate)

# p = computepay(h,r)
# print("Pay",p)

# largest = None
# smallest = None
# while True:
#     try:
#         num = input("Enter a number: ")
#         if num == "done" :
#             break
#         n = int(num)
#         if n > largest or largest is None:
#             largest = n
#         elif n < smallest or smallest is None:
#             smallest = n
#     except:
#         print("Invalid input")
#         continue
        
# print("Maximum is", largest)
# print("Minimum is", smallest)

# a = 'casa'
# print(a.capitalize())
# b='una casa'
# print(b.capitalize())

# text = "X-DSPAM-Confidence:    0.8475";
# pos = text.find(":")
# print(float(text[pos+1:]))

# handle = open(filename,mode)
# hand = open('mbox.txt','r')
# r for read, w for write
# Use the file name mbox-short.txt as the file name

# # Actividad 7.2
# fname = input("Enter file name: ")
# try:
# 	fh = open(fname)
# except:
#     print("Invalid file name")
#     quit()
# count = 0
# acumulate = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     count = count + 1
#     pos = line.find(":")
#     acumulate = acumulate + float(line[pos+1:])
# print("Average spam confidence:",acumulate/count)

# Esto es una lista
# nombres = ["Laura",'Julian',"Maria",'Manuel']

# fh = ['But soft what light through yonder window breaks',
#       'It is the east and Juliet is the sun',
#       'Arise fair sun and kill the envious moon',
#       'Who is already sick and pale with grief']

# lst = list()
# for line in fh:
#     aux = line.split()
#     for word in aux:
#         if word not in lst:
#             lst.append(word)
# lst.sort()
# print(lst)

# # Tarea 8.5
# fname = input("Enter file name: ")
# if len(fname) < 1 :
#     fname = "mbox-short.txt"
# fh = open(fname)
# count = 0
# mails = list()
# for line in fh:
#     if line.startswith("From") and not line.startswith("From:"):
#         row = line.split()
#         count = count +1
#         mails.append(row[1])
#         print(row[1])
# print("There were", count, "lines in the file with From as the first word")

counts = {'Laura':1,'Maria':2,'Julian':3,'Manuel':4}
# nombres = ["Laura",'Julian',"Maria",'Manuel']

# for name,num in counts.items():
#     print(name,num)
# stuff = dict()
# print(stuff.get('candy',-1))

# Valor mayor diccionario
# keys = counts.keys()
# values = counts.values()
# max_key = max(counts, key=lambda k: counts[k])
# print(max_key," ",counts[max_key])


# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)

# mails = dict()
# pro_value = -1
# pro_mail = ""
# for line in handle:
#     if line.startswith("From") and not line.startswith("From:"):
#         row = line.split()
#         name = row[1]
#         mails[name] = mails.get(name,0) + 1
#         # El .get funciona así
#         # Busca 'name' a ver si está en el diccionario mails
#         # Si está entonces pone su valor correspondiente
#         # Si no está, entonces lo toma como el valor que
#         # está ahí, osea cero '0'
# for key,value in mails.items():
#     if value >= pro_value:
#         pro_value = value
#         pro_mail = key
# print(pro_mail,pro_value)

# Organiza un diccionario con horas repetidas y las organiza
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# hours = dict()
# for line in handle:
#     if line.startswith("From") and not line.startswith("From:"):
#         aux = line.split()
#         time = aux[5]
#         hour = time[:2]
#         hours[hour] = hours.get(hour,0)+1
# for k,v in sorted(hours.items()):
#     print(k,v)

n = '2020 Jul  1 00:05:26 IBMBogC100_N5K_BCOL_2 %ETHPORT-5-IF_DOWN_LINK_FAILURE: Interface Ethernet102/1/39 is down (Link failure)'
if 'Ethernet' in n:
    print("Lo encontré! :D")
else:
    print("No lo encontré :(")




















