import sys
input = sys.stdin.readline

N = int(input().strip())

hash_fields = {}
for _ in range(N):
    key, status = input().split()
    if status == "enter":
        hash_fields[key] = 0
    else:
        del hash_fields[key]

keys = list(hash_fields.keys())
keys.sort(reverse=True)

for key in keys:
    print(key)
