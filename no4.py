def count_prime_number():
    n = int(input("첫 번째 수 입력 : "))
    m = int(input("두 번째 수 입력 : "))
    d = 0
    for i in range (n, m+1):
        s = 0
        for j in range(2, i):
            if i % j == 0:
                s = 1
            
        if s == 0:
            d += 1
    print('소수 갯수 :',d)
count_prime_number()
