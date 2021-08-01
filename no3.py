n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))

def find_even_number():
    numbers = [ i for i in range(n, m+1) if i%2 == 0]
    for s in numbers :
        print(s, '짝수')
        if s == (n + m) / 2 :
            print (s, '중앙값')

find_even_number()