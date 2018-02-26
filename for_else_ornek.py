for i in range(1, 50, 4):
    if i % 15 == 0:
        print("fizzbuzz")
        break
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
else:
    print("break yapılmadı")