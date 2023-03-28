def somar(num1,num2):
  total = num1 + num2
  print(total)
  
def sub(num1,num2):
  total = num1 - num2
  print(total)
  
def mult(num1,num2):
  total = num1 * num2
  print(total)
  
def menu ():
  print("----------Calculadora----------")
  print("")
  print("1 - somar\n2 - subtrair\n3 - multiplicar\n4 - Sair")
  print("__________")

while True:
  menu()
  pegar = int(input("Escolha qual operação deseja realizar: "))
  if pegar == 4:
    print("\nSaindo\n")
    break
  else:
    a = int(input("Insira o primeiro número: "))
    b = int(input("Insira o segundo número: "))
  if pegar == 1:
   print("\nIniciando a soma!!!\n") 
   somar(a,b)
    
  
  elif pegar == 2:
    print("\nIniciando a subtração!!!\n")
    sub(a,b)
    
  elif pegar == 3:
    print("\nIniciando a subtração!!!\n")
    mult(a,b)

  else:
    break
