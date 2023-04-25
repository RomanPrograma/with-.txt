


try:
    with open("with.txt", "r") as f:
        content = f.read()
    for digit in content.split():
        if digit.isdigit():
            print(digit)
except Exception as e:
    print("Error", e)
