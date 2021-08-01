def gugudan():
     number = int(input("몇단?: "))

     print(number, "단")


     for i in range(1,10):
         result = number*i

         if i % 2 != 0:

             if result<=50:
                 print(number , 'X',i, ' = ', result)
                
gugudan()