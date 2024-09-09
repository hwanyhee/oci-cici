f= open("cicd.txt","w+")
for i in range(20):
    f.write("This is line!!! %d\r\n" % (i+1))