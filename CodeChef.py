if __name__=="__main__":
	n=int(input())
	l=[]
	for i in range (n):
		l=list(map(int,input().split(" ")))
		llen=len(l)
		l.remove(llen-1)
		print(max(l))