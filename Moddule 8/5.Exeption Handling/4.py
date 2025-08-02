try :
    f = open("myfile.txt","r")
    print(f.read)
except Exception as e:
    print("Exception ",e)