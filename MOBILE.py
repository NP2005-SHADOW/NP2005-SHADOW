def mn(n):
    n_str=str(n)
    if n_str[0] not in '7,8,9':
        return False
    digit_count=0
    for i in n_str:
        if i.isdigit():
            digit_count += 1
    if digit_count==10:
        return True
    else:
        return False
def main():
    number=int(input("enter mobile number:"))
    if mn(number):
        print("valid number")
    else:
        print("invalid number")
main()
