#Question No. 1 (By using recursion)
def inversesum_recursion(n,x):
	if n==0:
		return 0
	else:
		x=(1/(x**n))+inversesum_recursion(n-1,x)
		return x


# Question No. 1 (By using for loop)
def inversesum_for(n,x):
	if n==0:
		return 0
	sum1=0
	for i in range(1,n+1):
		sum1+=(1/(x**i))
	return sum1


# Question No. 2
def series(n):
	if n%2==0:
		return (n*n)-1
	else:
		return (n*n)+1



# Question No. 3
def formula(x,y,a,b):
	p=(x+(1/y))**a
	q=(x-(1/y))**b
	p=p*q
	r=(y+(1/x))**a
	q=(y-(1/x))**b
	r=r*q
	q=p/r
	return q
