# Python Driver Code

def solve(opening_time: str, duration: str) -> str:
  n=list(map(int,input().split()))
m=list(map(int,input().split()))
a=n[0]+m[0]
b=n[1]+m[1]
if(a>24);
c=a-24
if(b>60)
c+=1;
d=b-60
print(c,end="")
print(d)

  return 

# The following snippet reads the input in the required format. 
# Just complete the solve function above. 

T = int(input())
for i in range(T):
  a = input()
  b = input()
  answer = solve(a, b)
  print(answer)
