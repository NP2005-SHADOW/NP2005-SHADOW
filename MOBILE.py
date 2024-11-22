def mobile_number(n):
    if len(n) == 10:
        if n[0]=="7" or n[0]=="8" or n[0]=="9":
            print("entered number is valid")
        else:
            print("entered number is invalid")
mobile_number()