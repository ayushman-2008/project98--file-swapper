def swaptext():
    filename= input("enter the file name")
    filename2= input("enter the file name no.2")
    with open(filename,'r') as a:
        data_a = a.read()
    with open(filename2,'r') as b:
        data_b = b.read()

    with open(filename,'w') as a:
        a.write(data_b)
    with open(filename2,'w') as b:
        b.write(data_a)

swaptext()



    

