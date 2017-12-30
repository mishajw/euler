def compute():
    tri(n):
        tri = n(n+1)/2
        return(tri)
    ans = 3*tri(math.floor(1000/3))+5*tri(math.floor(1000/5))-15*math.floor(1000/15)
    return(ans)
    

if __name__ == "__main__":
	print(compute())