
def armstrong_number(num):
    n=num
    nod=len(str(n))
    total=0
    while n>0:
        digits=n%10
        total = total+(digits**nod)
        n=n//10
    return total == num

user_number = int(input("Enter a number: "))

print(armstrong_number(user_number))


