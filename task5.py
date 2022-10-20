# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0
def FormatSum(lst):

  str=""
  for i in range(len(lst)):
      if(lst[i].count("-")!=0):
        str=str+lst[i]
      else:
        if str=="":
          str=str+lst[i]
        else:
          str=str+"+"+lst[i]

  return str 

def NSum(lst):  
  s=[]  
  d=[]
  num=0
  for i in range(len(lst)):
    if "^" in lst[i]:
      num=lst[i][lst[i].find("^")+1:len(lst[i])]
      if s.count(num)==0:
        s.append(num)
    elif "x" in lst[i]:
      if s.count("1")==0:
        s.append("1")
    elif "^" not in lst[i]:
      if s.count("0")==0:
        s.append("0")
  
  #s.sort()

#****************************************
  for i in range(len(s)):
    sm=0
    if lst[i]!="0" and lst[i]!="1":
      for ii in range(len(lst)):                    
        if "x^" in lst[ii]:
          num=lst[ii][lst[ii].find("^")+1:len(lst[ii])]          
          if s[i]==num:        
            if lst[ii][0:lst[ii].find("x")]!="":
              sm=sm+int(lst[ii][0:lst[ii].find("x")])

    if sm!=0:
      d.append(f"{sm}х^{s[i]}")  
#****************************************
    sm=0
    for ii in range(len(lst)):                    
      if "^" not in lst[ii]:
        if "x" in lst[ii]:
          sm=sm+int(lst[ii][0:lst[ii].find("x")])
    
  if sm!=0:
     d.append(f"{sm}х")
# #****************************************
  sm=0
  for ii in range(len(lst)):                    
    if "^" not in lst[ii]:
      if "x" not in lst[ii]:        
        sm=sm+int(lst[ii])
    
  if sm!=0:
     d.append(f"{sm}")
  
  return d

def convert(frm):
  frm=frm.replace(" ","")
  frm=frm.replace("=0","")
  frm=frm.replace("-"," -")  
  frm=frm.split("+")

  res=[] 
  for i in range(len(frm)):  
    n=frm[i].split(" ")
    for ii in range(len(n)):
      res.append(n[ii])

  return res

file1='file1.txt'
file2='file2.txt'

with open(file1, 'w', encoding='utf-8') as file:
    file.write('23x^9 - 16x^8 + 3x^7 + 15x^4 - 2x^3 + x^2 + 20 = 0')

with open(file2, 'w', encoding='utf-8') as file:
    file.write('17x^9 + 15x^8 - 8x^7 + 15x^6 - 10x^4 + 7x^3 - 13x + 33 = 0')


with open(file1,'r') as file:
    frm1 = file.readline()
    file.close()
print("")
print(frm1)

with open(file2,'r') as file:
    frm2 = file.readline()    
    file.close()
print(frm2)

frm1=convert(frm1)
frm2=convert(frm2)


sumfrm=[]
for i in range(len(frm1)):
  sumfrm.append(frm1[i])

for i in range(len(frm2)):
  sumfrm.append(frm2[i])

print("")
print(f"Результат: {FormatSum(NSum(sumfrm))}")
print("")

