try:
    _file = open('New file.txt', 'r')
    print(_file.read())
except Exception as e:
    print(e)
finally:
    _file.close()
