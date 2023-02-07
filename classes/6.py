ls = [1, 5, 2, 13, 0 , 4] #-> [5, 2, 13]

class primeClass:
    def filter_prime(x):
        cnt = 0
        for i in range(1, x + 1):
            if x % i == 0:
                cnt = cnt + 1
        if cnt == 2: return True
        return False

class_obj = primeClass.filter_prime

prime_numbers = list(filter(lambda x: class_obj(x), ls))
print(prime_numbers)


#print(prime_numbers)