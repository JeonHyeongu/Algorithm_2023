a = list(map(int, input().split()))
price = 0
if len(set(a)) == 3:
    price = max(a)*100
elif len(set(a)) == 2:
    if a[0] in a[1:]:
        price = 1000 + a[0]*100
    else:
        price = 1000 + a[1]*100
else:
    price = 10000 + a[0]*1000
print(price)