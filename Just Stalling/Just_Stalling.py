N = int(input(''))
A = sorted(map(int,input('').split(' ')))
B = sorted(map(int,input('').split(' ')))


t = 0
answer = 1
for i in range(N):
    while t < N and B[N-t-1] >= A[N-i-1]:
        t+=1
    answer *= t-i
print(answer)
