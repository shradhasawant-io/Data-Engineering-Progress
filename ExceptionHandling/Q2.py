try:
    numbers = [12,3,4]
    print(numbers[(5)])
except IndexError:
    print("Invalid Index")
except ValueError:
    print("Invalid Value")
except Exception:
    print("Some other error occurred")