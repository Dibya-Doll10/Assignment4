temp1 = input("Write something about yourself: ")
f = open(r"F:\\Video Script Translation\TUTEDUDE ASSIGNMENTS\output.txt","w")
f.write(temp1)
f.close()

f = open(r"F:\\Video Script Translation\TUTEDUDE ASSIGNMENTS\output.txt","r")
if f.read() == temp1 :
    print("Data successfully written")
else:
    print("Data not entered")

temp2 = input("Enter some additional data: ")
f = open(r"F:\\Video Script Translation\TUTEDUDE ASSIGNMENTS\output.txt","a")
f.write(temp2)
f.close()

f = open(r"F:\\Video Script Translation\TUTEDUDE ASSIGNMENTS\output.txt","r")
print(f.read())












