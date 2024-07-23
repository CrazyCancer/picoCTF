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
 v5[1] = ( >> 16) % 0x100    
 v5[2] = (i >> 8) % 0x100    
 v5[3] = i % 0x100



