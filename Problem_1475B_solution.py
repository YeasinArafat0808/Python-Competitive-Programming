t = int ( input ( ) )
for _ in range(t):
    n = int(input())
    y = n // 2020
    x = n % 2020
    if x <= y:
        print("YES")
    else:
        print("NO")
