def equal_or_not(nbr1, nbr2):
  if nbr1 == nbr2:
    print("Ces deux nombres sont égaux")
  else:
    print("Ces deux nombres ne sont pas égaux")

def add_(nbr):
  total = 0
  for i in range (10):
    total += nbr
    print(total)
    
    
vowel_list = ["a", "e", "i", "o", "u", "y"]
word_ = "antidisestablishmentarianism"
x = 1
while x <= len(word_):
  for i in word_:
    if i in vowel_list:
      print(i,  end = "")
  break
  x += 1
  
 from random import choice, randint
from operator import add, sub, mul, truediv

def random_op(nbr1, nbr2, nbr3):
  operators = (add, sub, mul, truediv)
  op = choice(operators)
  try:
    result = op(nbr1, nbr2) 
    result2 = op(result,nbr3)
    return result2
  except ZeroDivisionError:
    print("Error, you're trying to divide by zero")

random_op(0,32,2)


def clean_salary(nbr):
  nbr = nbr*0.80
  return nbr
  
 
def switch_values(value1, value2):
  value0=value1
  value1 = value2
  value2 = value0
  return value1, value2
  
  
def next_day(day):
  semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
  for i in semaine:
    if i == day and not "Dimanche":
      i = semaine.index(i)+1
      return (semaine[i])
    else:
      return ("Lundi")
      
      
def create_list(string):
  clean_carac = ["'", ",", "?"]
  list_ = ""
  for i in string:
    if i not in clean_carac:  
      list_ = list_ + i
  return list_.split()
  
def upper_half_time(string):
  vowel_list = ["a", "e", "i", "o", "u", "y"]
  new_string = ""
  for i in range (0,len(string), 2):
    for x in string:
      if x in vowel_list:
        x = x.upper()
      new_string = new_string + x
    return new_string
    
def create_list(string):
  carac = " "
  new_list2 = []
  for i in string:
    if i not in carac:
      new_list2.append(i)
      for i in new_list2:
        new_list = string.split()
  return new_list2
  
  
def print_age_and_name(age, first_name):
  age = input("Quel est ta date de naissance format : xx-xx-xxxx " )
  first_name = input("Quel est ton prénom ")
  this_year = 2021
  y_age = int(age.split("-")[2])
  your_age = this_year - y_age
  print("Bonjour", first_name, "aujourd'hui tu as ", your_age, "ans" )
  
def carre_nbr(nbr):
  nbr = nbr**2
  return nbr
  
def cube_nbr(nbr):
  nbr = nbr**3
  return nbr
  
def absolut_value(nbr):
  return abs(nbr)
  
def factorielle(nbr):
    if nbr == 0:
        return 1
    else:
        i = 1
        for x in range(2,nbr+1):
            i = i * x
        return i
        
def mode_nbr(liste):
  dico = {}
  for i in liste:
    count = i
    if count in dico:
      dico[count] += 1
    else:
      dico[count] = 1
  return max(dico, key = dico.get)
  
def mean_nbr(liste):
  moyenne = np.mean(liste2)
  return moyenne
  
def min_nbr(liste):
  mini = min(liste)
  return mini
  
def maxi_nbr(liste):
  maxi = max(liste)
  return maxi
  
  
