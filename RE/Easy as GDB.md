# Easy as GDB

File: https://mercury.picoctf.net/static/34d95f5c7898c0d9500790225437239e/brute

Kiểm tra file bằng ***Detect It Easy***
![image](https://hackmd.io/_uploads/HJUlWzpOC.png)

Mở file bằng Ida

Tại `Sub_9AF` chúng ta được yêu cầu nhập đầu vào 

![image](https://hackmd.io/_uploads/rkxH-zTO0.png)

```c=
v0 = (char *)strnlen(&aZNh, 512, v2, v3);
//v0 sẽ được gán bằng độ dài của chuỗi aZNh
```

![image](https://hackmd.io/_uploads/ByOHGG6dA.png)

```c=
src = (char *)sub_82B(v0, (size_t)v0);
```
có vẻ như không phải tham số được truyền vào là v0, vậy nên chuyển sang assembly để xem nó là gì

![image](https://hackmd.io/_uploads/BkGG7M6_0.png)

`v0` ở đây sẽ là chuỗi đầu vào và `(size_t)v0` là độ dài của đầu vào

vào hàm `sub_82B` để xem
```c=
char *__cdecl sub_82B(char *src, size_t n)
{
  unsigned int i; // [esp+0h] [ebp-18h]
  char *dest; // [esp+Ch] [ebp-Ch]
  size_t na; // [esp+24h] [ebp+Ch]

  na = (n & 0xFFFFFFFC) + 4;
  dest = (char *)malloc(na + 1);
  strncpy(dest, src, na);
  for ( i = 180154381; i < 0xDEADBEEF; i += 2075469 )
    sub_6BD(dest, na, i);
  return dest;
}
```
với mỗi lần lặp nó sẽ gọi đến hàm `sub_6BD`
```c=
unsigned int __cdecl sub_6BD(int a1, unsigned int a2, int a3)
{
  unsigned int result; // eax
  unsigned int i; // [esp+14h] [ebp-14h]
  char v5[4]; // [esp+18h] [ebp-10h]
  unsigned int v6; // [esp+1Ch] [ebp-Ch]

  v6 = __readgsdword(0x14u);
  v5[0] = HIBYTE(a3);
  v5[1] = BYTE2(a3);
  v5[2] = BYTE1(a3);
  v5[3] = a3;
  for ( i = 0; i < a2; ++i )
    *(_BYTE *)(a1 + i) ^= v5[i & 3];
  result = __readgsdword(0x14u) ^ v6;
  if ( result )
    sub_B20();
  return result;
}
```
giá trị của v5 sẽ được lấy từ a3, nhưng tôi chưa hiểu nó sẽ lấy như thế nào. vậy nên tôi sẽ chuyển sang hợp ngữ để xem
```
mov     eax, [ebp+arg_8]
shr     eax, 18h
mov     [ebp+var_10], al
mov     eax, [ebp+arg_8]
shr     eax, 10h
mov     [ebp+var_F], al
mov     eax, [ebp+arg_8]
shr     eax, 8
mov     [ebp+var_E], al
mov     eax, [ebp+arg_8]
mov     [ebp+var_D], al
```
 v5[0] = (a3 >> 24) % 256    
 v5[1] = (a3 >> 16) % 256    
 v5[2] = (a3 >> 8) % 256    
 v5[3] = a3 % 256 
 
Vì giá trị được lấy từ thanh ghi al nên phải %256 để lấy 8 bit thấp 

ví dụ: eax = 0011 0000 0011 1001    
ah = 0011 0000 và al = 0011 1001

Tiếp đến chuỗi flag sẽ được mã hóa bằng phép xor 
```c=
for ( i = 0; i < a2; ++i )
    *(_BYTE *)(a1 + i) ^= v5[i & 3];
```
Sau khi mã hóa xong flag thì gọi đến hàm `sub_7C2`
```c=
unsigned int __cdecl sub_7C2(int a1, unsigned int a2, int a3)
{
  unsigned int result; // eax
  unsigned int j; // [esp+8h] [ebp-8h]
  int i; // [esp+Ch] [ebp-4h]

  if ( a3 <= 0 )
  {
    result = a2 - 1;
    for ( i = a2 - 1; i > 0; --i )
      result = sub_751(a1, a2, i);
  }
  else
  {
    for ( j = 1; ; ++j )
    {
      result = j;
      if ( a2 <= j )
        break;
      sub_751(a1, a2, j);
    }
  }
  return result;
}
```
Hàm `sub_751` sẽ được gọi đến để thực hiện việc xáo trộn flag     
Tuy nhiên nếu a3 > 0 thì việc xáo trộn sẽ ngược với khi a3 <= 0 và chúng ta cần phải để ý chỗ này
```c=
unsigned int __cdecl sub_751(int a1, int a2, int a3)
{
  unsigned int result; // eax
  char v4; // [esp+Bh] [ebp-5h]
  unsigned int i; // [esp+Ch] [ebp-4h]

  for ( i = 0; ; i += a3 )
  {
    result = a2 - a3 + 1;
    if ( i >= result )
      break;
    v4 = *(_BYTE *)(a1 + i);
    *(_BYTE *)(a1 + i) = *(_BYTE *)(i + a3 - 1 + a1);
    *(_BYTE *)(a1 + i + a3 - 1) = v4;
  }
  return result;
}
```
Sau đó sẽ kiểm tra giá trị trả về của `sub_8C4` có bằng 1 hay không
```c=
int __cdecl sub_8C4(char *src, size_t n)
{
  int v3; // [esp+0h] [ebp-18h]
  size_t i; // [esp+4h] [ebp-14h]
  char *dest; // [esp+8h] [ebp-10h]
  char *v6; // [esp+Ch] [ebp-Ch]

  dest = (char *)calloc(n + 1, 1u);
  strncpy(dest, src, n);
  sub_7C2(dest, n, -1);
  v6 = (char *)calloc(n + 1, 1u);
  strncpy(v6, aZNh, n);
  sub_7C2(v6, n, -1);
  puts("checking solution...");
  v3 = 1;
  for ( i = 0; i < n; ++i )
  {
    if ( dest[i] != v6[i] )
      return -1;
  }
  return v3;
}
```
Tại đây chương trình sẽ thực hiện việc xáo trộn flag thêm một lần nữa, đồng thời xáo trộn chuỗi `aZNh`. Sau đó kiểm tra xem flag và `aZNh` sau khi xáo có giống nhau không `dest[i] != v6[i]`

Sau khi flag được xáo trộn 2 lần với a3 = 1 và a3 = -1 thì việc xáo trộn là vô nghĩa và ta không cần bận tâm đến nó

Tuy nhiên để tìm lại flag ta cần phải xáo trộn lại `aZNh` cho đúng vị trị. Do ta thấy rằng `aZNh` là chuỗi flag đã bị xáo trộn một lần với a3 = 1, vì vậy ta cần xáo trộn lại với a3 = -1

Sau đó xor lại để tìm flag 

```py=
dest = [  0x7A, 0x2E, 0x6E, 0x68, 0x1D, 0x65, 0x16, 0x7C, 0x6D, 0x43, 
  0x6F, 0x36, 0x65, 0x62, 0x40, 0x16, 0x43, 0x62, 0x40, 0x3F, 
  0x58, 0x01, 0x58, 0x33, 0x62, 0x6B, 0x53, 0x30, 0x38, 0x17]


for i in range(len(dest)-1, 0, -1):
  result = len(dest) - i + 1
  for j in range(0, result, i):
    dest[j], dest[j+i-1] = dest[j+i-1], dest[j]

v5 = [0,0,0,0]
for i in range(180154381, 3735928559, 2075469):
  v5[0] = (i >> 24) % 0x100
  v5[1] = (i >> 16) % 0x100
  v5[2] = (i >> 8) % 0x100
  v5[3] = i % 0x100
  for j in range(len(dest)):
    dest[j] ^= v5[j&3]

for i in dest:
  print(chr(i), end='')


#flag: picoCTF{I_5D3_A11DA7_e5458cbf}
```
