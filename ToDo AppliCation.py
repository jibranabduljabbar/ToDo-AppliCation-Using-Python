List = []

while True:
    print("Element In Our List: \n")
    for Element in List :
        print("==> " + Element + "\n")

    print("1): Add Element.")
    print("2): Delete Element.")
    print("3): Delete All Element.")
    print("4): Exit ToDo.")
    print("\n*) Note: Please Give Input In Number e.g 1, 2, 3, 4 \n")
    
    User_Inp = input("Enter Your Choice: ")
    
    if User_Inp == "1":
        List.append(input("Enter Your ToDo Item: "))
    elif User_Inp == "2":
        List.remove(input("Enter Item To Delete: "))
    elif User_Inp == "3":
        List.clear()
    elif User_Inp == "4":
        break
    else:
        print("Invalid Syntex.")
    
print("\n ----------------------------------------------------------------------------------------------- \n")