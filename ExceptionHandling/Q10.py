try:
    print("Outer try 1")
    # a = 10/0
    # print("Outer try 2")
    try:
        print("Inner try 1")
        # l = [1,2,3]
        # print(l[5])
        # print("Inner try 2")
        try:
            print ("Inner try 3")
            n = int("abc")
        except ValueError as e:
            print(e)
    except ZeroDivisionError as error:
        print(error)
except Exception as error:
    print(error) 