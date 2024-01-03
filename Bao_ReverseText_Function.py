while True:

    mytxt = (input("Enter a text and print it in reverse/backward:")[::-1])
    
    InpCheck = mytxt.isdigit()
    if InpCheck == True:
        print("Error Reported! Enter text only.")
    else:
        print(mytxt)
      
    key = str(input("Enter [1] to exit or Press [Enter] to continue:"))
    
    if key == str(1):
       exit()
  