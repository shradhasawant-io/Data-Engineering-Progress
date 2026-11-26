def practice():
    try:
        return 10
    finally:
        print("Finally Executed")
practice()
print(practice())