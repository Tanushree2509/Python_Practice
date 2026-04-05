A, B = map(int, input().split())

print(f"floor {A} / {B} = {A//B}")
print(f"ceil {A} / {B} = {(A+B-1)//B}")
print(f"round {A} / {B} = {(A*2+B)//(2*B)}")