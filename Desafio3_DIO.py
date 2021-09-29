#enter 3 input values
a = [float(x) for x in input().split()]

#if the values attend the triangle condition, print the Perimeter value
if a[0] + a[1] > a[2] and a[0] + a[2] > a[1] and a[1] + a[2] > a[0]:
    print(f"Perímetro = {sum(a):.1f}")
#if the values don't attend the triangle condition, print the trapezium area value
else:
    print(f"Área = {((a[0] + a[1])* a[2])/2:.1f}")