
try:
    with open('with_.txt', 'r') as f:
        cont = f.read()
        n = input('Enter string that you want to change')
        m = input('Enter string that you want to change with')
        content = cont.replace(n, m)
    with open('with_.txt', 'w') as f:
       f.write(content)
except Exception as e:
    print(f'error: {e}')
finally:
    f.close()
    print('Done, file closed')

