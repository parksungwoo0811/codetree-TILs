a,b=input().split()
a,b=int(a),int(b)
t=(b//((a/100)**2))
t=int(t)
if t>25:
    print(t)
    print("Obesity")
else:
    print(t)