try:
    with open('new file.txt', 'r') as f:
        file_content = f.read()
    x = file_content.split()
    words = len(x)
    print(f'words: {words}')
except Exception as e:
    print(f'error: {e}')

