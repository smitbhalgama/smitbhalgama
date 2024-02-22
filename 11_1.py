#crate and open file named practical 11.txt
f=open("practical 11.txt",'r')
s=f.readlines()
print(s)
#read the entire content of the file and display
#f.writelines(["hii\n","hello..\n","welcome\n"])
f.readlines()
print("No of lines in files:",len(s))
c=0
for i in s:
    l=i.split()
    c=c+len(l)
print("No of worlds in files:",c)
f.close()