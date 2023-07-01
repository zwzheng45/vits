output=open("output.txt","a")

for i in range(0,338):
    file = open("1.1-1.4_%d.wav.txt"%i, "r")
    a=True
    while a:
        x = file.readline()
        x=x.strip("\n")
        output.write(x)
        if not x:
            output.write("\n")
            print("End Of File")
            a = False
        output.write("，")
file.close()
output.close()