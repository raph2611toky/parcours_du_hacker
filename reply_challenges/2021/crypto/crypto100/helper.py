
def pgcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a


def puissance_mod(x,k,n):
    puiss=1
    while(k>1):
        if x%2==1:
            puiss = (puiss*x)%n
        x = x*x % n
        k = k//2
    return puiss

def pgcd_etendu(a,b):
    x,xx=1,0
    y,yy=0,1
    while b!=0:
        q=a//b
        a,b=b,a%b
        xx, x = x-q*xx, xx
        yy, y = y-q*yy, yy
    return(a,x,y)

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_prime(a,b):
    p = []
    for i in range(a,b+1):
        if isPrime(i):
            p.append(i)
            print(i)
    return p

