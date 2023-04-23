#try:
#    _file = open('new file.txt', 'r')
#    file_cont = _file.read()
#    string = 'hello'
#    if string in file_cont:
#        print('yes')
#except Exception as e:
#    print(e)
#finally:
#    file_cont.close()
try:
    with open('new file.txt', 'r') as f:
        file_cont = f.read().split()
    striing = 'hello'
    if striing in file_cont:
        print('yes')
    else:
        print('no')
except Exception as e:
    print(f'error: {e}')
