N= int(input())
A= []
for i in range(1,N):
    A.append(i)
X=int(input())
def nearest_value(A,X):
    found=A[0]
    for a in A:
        if abs(a-X)< abs(found-X):
            found=a 
    return found
print(nearest_value(A,X))