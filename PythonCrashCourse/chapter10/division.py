"""处理ZeroDivisionError异常"""

print("Give me two numberts, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nFirst Number: ")
    if first_num == 'q':
        break
    second_number = input("\nSecond Number: ")
    try:
        answer = int(first_num) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide zero")
    else:
        print(answer)



