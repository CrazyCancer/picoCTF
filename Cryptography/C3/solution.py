#Sau khi đọc xong chương trình thì tôi có cách giải như sau

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"
out = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"

input = ""
prev = 0

for char in out:
    cur = lookup2.index(char) + prev
    input += lookup1[cur % 40]
    prev = cur

#Sau khi thực hiện xong thì chúng ta nhận được giá trị của input

# asciiorder
# fortychars
# selfinput
# pythontwo

chars = ""
from fileinput import input
for line in input():
    chars += line
b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print chars[i] #prints
        b += 1 / 1

#Đến đây chúng ta chỉ cần viết lại chương trình và input giống như trên là được
#tôi đọc file input với nội dung giống như trên
with open("input.txt", "r") as file:
    chars = file.read()

b = 1 / 1

for i in range(len(chars)):
    if i == b * b * b:
        print(chars[i], end='')
        b += 1 / 1

#Thu được kết quả: adlibs
