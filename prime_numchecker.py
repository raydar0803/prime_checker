def prime_checker(number):
  if(number==0 or number==1):
    print("It's not a prime number")
  elif(number==2):
    print("It's a prime number")
  else:
    flag=0
    for n in range(2, number):
      if(number%n==0):
        flag=1;
        break;
    if(flag==0):
      print("It's a prime number")
    else:
      print("It's not a prime number")






n = int(input("Check this number: "))
prime_checker(number=n)

