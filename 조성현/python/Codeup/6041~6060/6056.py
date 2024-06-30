a,b=map(int,input().split())
print(bool((a and not b) or (not a and b)))