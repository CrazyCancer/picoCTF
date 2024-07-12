# Forky

file: https://jupiter.challenges.picoctf.org/static/78c5ee78a6593e52ba5e5b08bc9f13c1/vuln

> Phần mô tả cho chúng ta biết cần tìm số nguyên cuối cùng được truyền vào hàm `doNothing(*v4)`

Trước tiên tôi mở file bằng IDA(phiên bản free cho linux)

Phía dưới là hàm main của chương trình
```c=
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int *v4; // [esp+8h] [ebp-Ch]trình

  v4 = (int *)((int (__cdecl *)(_DWORD, int, int, int, int, _DWORD))mmap)(0, 4, 3, 33, -1, 0);
  *v4 = 1000000000;
  fork();
  fork();
  fork();
  fork();
  *v4 += 1234567890;
  doNothing(*v4);
  return 0;
}
```
Sau một lúc tìm hiểu thì tôi được biết `mmap` cơ bản là cấp phát bộ nhớ, còn  `fork()` sẽ tạo ra một tiến trình con và mỗi tiến trình con sẽ nhận được một bản sao của không gian bộ nhớ của tiến trình cha

Phía trên `fork()` được gọi 4 lần nên số tiến trình con là 2^4 = 16

Vậy giá trị cuối cùng được truyền vào hàm `doNothing(*v4)` là 
1000000000 + 16*1234567890 = 20753086240

Tuy nhiên đây không phải là flag 

Sau một lúc mài mò thì tôi đã để ý đến một chỗ 
`v4 = (int *)((int (__cdecl *)(_DWORD, int, int, int, int, _DWORD))mmap)(0, 4, 3, 33, -1, 0);`

v4 ở đây là DWORD nên tôi đã thử chuyển từ QWORD sang DWORD 
![518884ed-05a8-4e10-8e4a-c5e1382dac70](https://hackmd.io/_uploads/Bygyl1h0P0.jpg)
![image](https://hackmd.io/_uploads/SJbMy2APR.png)

Và số nguyên cuối cùng này chính xác là flag chúng ta cần tìm

