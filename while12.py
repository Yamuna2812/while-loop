books = ["Python", "Java", "C++"]
issued = []

while True:
    print("\n1.View 2.Issue 3.Return 4.Exit")
    ch = input("Choice: ")
    
    if ch == '1':
        print("Available:", books)
    
    elif ch == '2':
        b = input("Book name: ")
        if b in books:
            books.remove(b)
            issued.append(b)
            print("Issued")
        else:
            print("Not available")
    
    elif ch == '3':
        b = input("Return book: ")
        if b in issued:
            issued.remove(b)
            books.append(b)
            print("Returned")
    
    else:
        break
