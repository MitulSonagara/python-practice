def func1(*args):
    for arg in args:
        print(arg)

print("first call :")
func1(20, 40, 60)
print("second call :")
func1(80, 100)
