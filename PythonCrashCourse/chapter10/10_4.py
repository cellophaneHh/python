prompt = "随便输入点什么(输入q退出):"

while True:
    msg = input(prompt)
    if msg == 'q':
        break
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(msg + "\n")
