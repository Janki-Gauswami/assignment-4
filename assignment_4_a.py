
    try:
        with open("sample.txt","r") as f:
            for x in f:
                print(x)  
    except FileNotFoundError:
        print("Error: The file 'sample.txt' was not found.")

