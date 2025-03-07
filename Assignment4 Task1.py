try:
    f =  open(r"F:\\video script translation\TUTEDUDE ASSIGNMENTS\sample.txt", "r")
    for x in f:
        print(x)

except:
    print("Error! The file was not found")
