import random
 
def hit_or_miss(acc):
  return random.randint(1,100) <= acc
  
def tackle(my_acc, opp_hp):
  hit_or_miss_result = hit_or_miss(my_acc)

  if(hit_or_miss_result):
    opp_hp -= 10
    print("Bam!")
    input("<<Press Enter>>")
    
  else:
    print("But it missed!")
    input("<<Press Enter>>")
    
  return opp_hp

def sandAttack(my_acc, opp_acc):
  hit_or_miss_result = hit_or_miss(my_acc)

  if(opp_acc != 0):
    if(hit_or_miss_result):
        opp_acc -= 10
        print("Swoosh!")
        input("<<Press Enter>>")
    else:
      print("But it missed!")
      input("<<Press Enter>>")

  return opp_acc

def pokeball(opp_hp):
  hit_or_miss_result = hit_or_miss(100 - opp_hp)

  if(hit_or_miss_result):
    print("You caught a Bulbasaur!")
    input("<<Press Enter>>")
    return True
  else:
    print("But it broke free!")
    input("<<Press Enter>>")
    return False

def Bulbasaur(my_acc, opp_hp, opp_acc):  
  attack = random.randint(0, 1)
  #Tackle = 0, SandAttack = 1
  
  if attack == 0:
    print("Bulbasaur uses Tackle")
    input("<<Press Enter>>")
    opp_hp = tackle(my_acc, opp_hp)
  
  else: #if attack = 1
    print("Bulbasaur uses Sand Attack")
    input("<<Press Enter>>")
    opp_acc = sandAttack(my_acc, opp_acc)
    
  return opp_hp, opp_acc

def Pikachu(my_acc, opp_hp, opp_acc, result):  
  print("What to do>\n1. Tackle\n2. Sand Attack\n3. Throw Pokeball")
  attack = input ("<<Please enter 1, 2 or 3>> ")
  attack = int(attack)
  #Tackle = 1, SandAttack = 2, Throw Pokeball = 3
  
  if attack == 1:
    print("Pikachu uses Tackle")
    input("<<Press Enter>>")
    opp_hp = tackle(my_acc, opp_hp)
  
  elif attack == 2: 
    print("Pikachu uses Sand Attack")
    input("<<Press Enter>>")
    opp_acc = sandAttack(my_acc, opp_acc)
    
  else:
    print("You threw a Pokeball")
    input("<<Press Enter>>")
    result = pokeball(opp_hp)
    
  return opp_hp, opp_acc, result

def display_stats(bhp, bacc, php, pacc):
  print("Bulbasaur\n  hp", bhp, "acc ", bacc)
  print("Pikachu\n  hp", php, "acc ", pacc)

def main():
  while True:
    print("<------------------->")
    print("It's a Bulbasaur")
    input("<<press enter>>")
    print("What do you want to do?")
    print("1. Battle")
    print("2. Run away")
    
    b_hp = 100
    b_acc = 100
    p_hp = 100
    p_acc = 100
    result = False
    
    val = input('<<Please enter 1 or 2>> ')
    
    try:
      val = int(val)
    except ValueError:
      print("That is a string. Please enter 1 or 2")
    

    if val == 2:
      print("Goodbye")
      print("<<program ends>>")
      break
    
    elif val == 1:
      print("Pikachu I choose you")
      input("<<Press enter>>")

      while(True):
        display_stats(b_hp, b_acc, p_hp, p_acc)
        
        p_hp, p_acc = Bulbasaur(b_acc, p_hp, p_acc)
        
        display_stats(b_hp, b_acc, p_hp, p_acc)
        
        if (p_hp == 0):
          print("Pikachu fainted")
          break
               
        b_hp, b_acc, result = Pikachu(p_acc, b_hp, b_acc, result)
        
        if (b_hp == 0):
          print("Bulbasaur fainted")
          break
          
        elif (result):
          break
          
    else:
      print("Try again")    
      
if __name__ == "__main__":
  main()
