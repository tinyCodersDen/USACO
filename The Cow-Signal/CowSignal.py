import sys

sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")

M,N,K = list(map(int,input().split(' ')))
for t in range(M):
    H = input()
    s = ''
    for q in H:
        s+=q*K
    for e in range(K):
        print(s)
