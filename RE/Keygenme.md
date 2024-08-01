# Keygenme
file: https://artifacts.picoctf.net/c/53/keygenme

Trước tiên ta sẽ kiểm tra bằng ***Detect It Easy***
![image](https://hackmd.io/_uploads/HyrUvJnv0.png)

Vì là ELF64 nên tôi sẽ mở nó bằng IDA64

Bên dưới là hàm main của chương trình

```c =
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  char s[40]; // [rsp+10h] [rbp-30h] BYREF
  unsigned __int64 v5; // [rsp+38h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  printf("Enter your license key: ");
  fgets(s, 37, stdin);
  if ( ((unsigned __int8 (__fastcall *)(char *))((char *)&sub_1208 + 1))(s) )
    puts("That key is valid.");
  else
    puts("That key is invalid.");
  return 0LL;
}
```
Chương trình yêu cầu ta nhập vào một chuỗi key

Nếu điều kiện if đúng thì sẽ in ra `"That key is valid."`

Kiểm tra hàm `sub_1208` 

![image](https://hackmd.io/_uploads/rks3hJhPR.png)

Có vẻ như quá trình phân tích bị lỗi nên ta sẽ chuyển sang đọc bằng assembly 
```
.text:0000000000001208 sub_1208        proc near               ; CODE XREF: main+52↓p
.text:0000000000001208                 push    rbx
.text:0000000000001208 sub_1208        endp ; sp-analysis failed
.text:0000000000001208
.text:000000000000120A                 nop     edx
.text:000000000000120D                 push    rbp
.text:000000000000120E                 mov     rbp, rsp
.text:0000000000001211                 sub     rsp, 0E0h
.text:0000000000001218                 mov     [rbp-0D8h], rdi
.text:000000000000121F                 mov     rax, fs:28h
.text:0000000000001228                 mov     [rbp-8], rax
.text:000000000000122C                 xor     eax, eax
.text:000000000000122E                 mov     rax, 7B4654436F636970h
.text:0000000000001238                 mov     rdx, 30795F676E317262h
.text:0000000000001242                 mov     [rbp-90h], rax
.text:0000000000001249                 mov     [rbp-88h], rdx
.text:0000000000001250                 mov     rax, 6B5F6E77305F7275h
.text:000000000000125A                 mov     [rbp-80h], rax
.text:000000000000125E                 mov     dword ptr [rbp-78h], 5F7933h
.text:0000000000001265                 mov     word ptr [rbp-0B2h], 7Dh ; '}'
.text:000000000000126E                 lea     rax, [rbp-90h]
.text:0000000000001275                 mov     rdi, rax
.text:0000000000001278                 call    _strlen
.text:000000000000127D                 mov     rcx, rax
.text:0000000000001280                 lea     rdx, [rbp-0B0h]
.text:0000000000001287                 lea     rax, [rbp-90h]
.text:000000000000128E                 mov     rsi, rcx
.text:0000000000001291                 mov     rdi, rax
.text:0000000000001294                 call    _MD5
.text:0000000000001299                 lea     rax, [rbp-0B2h]
.text:00000000000012A0                 mov     rdi, rax
.text:00000000000012A3                 call    _strlen
.text:00000000000012A8                 mov     rcx, rax
.text:00000000000012AB                 lea     rdx, [rbp-0A0h]
.text:00000000000012B2                 lea     rax, [rbp-0B2h]
.text:00000000000012B9                 mov     rsi, rcx
.text:00000000000012BC                 mov     rdi, rax
.text:00000000000012BF                 call    _MD5
.text:00000000000012C4                 mov     dword ptr [rbp-0C8h], 0
.text:00000000000012CE                 mov     dword ptr [rbp-0C4h], 0
.text:00000000000012D8                 jmp     short loc_1321
```
Sau khi kiểm tra xong phần này thì tôi tìm được một phần của flag `picoCTF{br1ng_y0ur_0wn_k3y_????}`

Tiếp tục kiểm tra, tôi tìm thấy được phần flag còn thiếu 
```
.text:00000000000013BF loc_13BF:                               ; CODE XREF: .text:000000000000139A↑j
.text:00000000000013BF                 cmp     dword ptr [rbp-0BCh], 1Ah
.text:00000000000013C6                 jle     short loc_139C
.text:00000000000013C8                 movzx   eax, byte ptr [rbp-5Eh]
.text:00000000000013CC                 mov     [rbp-15h], al
.text:00000000000013CF                 movzx   eax, byte ptr [rbp-56h]
.text:00000000000013D3                 mov     [rbp-14h], al
.text:00000000000013D6                 movzx   eax, byte ptr [rbp-57h]
.text:00000000000013DA                 mov     [rbp-13h], al
.text:00000000000013DD                 movzx   eax, byte ptr [rbp-70h]
.text:00000000000013E1                 mov     [rbp-12h], al
.text:00000000000013E4                 movzx   eax, byte ptr [rbp-56h]
.text:00000000000013E8                 mov     [rbp-11h], al
.text:00000000000013EB                 movzx   eax, byte ptr [rbp-5Eh]
.text:00000000000013EF                 mov     [rbp-10h], al
.text:00000000000013F2                 movzx   eax, byte ptr [rbp-64h]
.text:00000000000013F6                 mov     [rbp-0Fh], al
.text:00000000000013F9                 movzx   eax, byte ptr [rbp-56h]
.text:00000000000013FD                 mov     [rbp-0Eh], al
.text:0000000000001400                 movzx   eax, byte ptr [rbp-0B2h]
.text:0000000000001407                 mov     [rbp-0Dh], al
.text:000000000000140A                 mov     rax, [rbp-0D8h]
.text:0000000000001411                 mov     rdi, rax
.text:0000000000001414                 call    _strlen
.text:0000000000001419                 cmp     rax, 24h ; '$'
.text:000000000000141D                 jz      short loc_1426
.text:000000000000141F                 mov     eax, 0
.text:0000000000001424                 jmp     short loc_1475
```

Tương ứng với 8 kí tự còn thiếu 
```
.text:00000000000013C8                 movzx   eax, byte ptr [rbp-5Eh]
.text:00000000000013CC                 mov     [rbp-15h], al
.text:00000000000013CF                 movzx   eax, byte ptr [rbp-56h]
.text:00000000000013D3                 mov     [rbp-14h], al
.text:00000000000013D6                 movzx   eax, byte ptr [rbp-57h]
.text:00000000000013DA                 mov     [rbp-13h], al
.text:00000000000013DD                 movzx   eax, byte ptr [rbp-70h]
.text:00000000000013E1                 mov     [rbp-12h], al
.text:00000000000013E4                 movzx   eax, byte ptr [rbp-56h]
.text:00000000000013E8                 mov     [rbp-11h], al
.text:00000000000013EB                 movzx   eax, byte ptr [rbp-5Eh]
.text:00000000000013EF                 mov     [rbp-10h], al
.text:00000000000013F2                 movzx   eax, byte ptr [rbp-64h]
.text:00000000000013F6                 mov     [rbp-0Fh], al
.text:00000000000013F9                 movzx   eax, byte ptr [rbp-56h]
.text:00000000000013FD                 mov     [rbp-0Eh], al
```
Bây giờ chúng ta chỉ cần debug để xem flag còn thiếu là gì 

Ở đây tôi debug bằng cách sử dụng `Remote Linux debugger` trên IDA. Tuy nhiên có vẻ chương trình đã bị lỗi nên tôi không thể debug 

Vì thế tôi quyết chạy thử file trên linux 

Sau khi chạy dòng lệnh `chmod +x Keygenme` thì bị báo lỗi
`error while loading shared libraries: libcrypto.so.1.1: cannot open shared object file: No such file or directory`

Sau một lúc tìm kiếm thì tôi đã tìm được cách tải thư viện `libcrypto.so.1.1`
```
wget http://nz2.archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.22_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.22_amd64.deb
```

Sau cài được thư viện thì tôi mở file bằng IDA cho linux (có lẽ các bạn sẽ thắc mắc tại sao mình lại mở thêm IDA thì do trên linux là bản free và mình vừa cài thư viện trên linux)

```c=
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  char s[40]; // [rsp+10h] [rbp-30h] BYREF
  unsigned __int64 v5; // [rsp+38h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  printf("Enter your license key: ");
  fgets(s, 37, stdin);
  if ( (unsigned __int8)sub_1209(s) )
    puts("That key is valid.");
  else
    puts("That key is invalid.");
  return 0LL;
}
```
```c=
__int64 __fastcall sub_1209(const char *a1)
{
  size_t v1; // rax
  size_t v2; // rax
  int v4; // [rsp+18h] [rbp-C8h]
  int v5; // [rsp+18h] [rbp-C8h]
  int i; // [rsp+1Ch] [rbp-C4h]
  int j; // [rsp+20h] [rbp-C0h]
  int k; // [rsp+24h] [rbp-BCh]
  int m; // [rsp+28h] [rbp-B8h]
  char v10[18]; // [rsp+2Eh] [rbp-B2h] BYREF
  char v11[16]; // [rsp+40h] [rbp-A0h] BYREF
  char s[32]; // [rsp+50h] [rbp-90h] BYREF
  char v13[18]; // [rsp+70h] [rbp-70h] BYREF
  char v14; // [rsp+82h] [rbp-5Eh]
  char v15; // [rsp+89h] [rbp-57h]
  char v16; // [rsp+8Ah] [rbp-56h]
  char v17[72]; // [rsp+90h] [rbp-50h] BYREF
  unsigned __int64 v18; // [rsp+D8h] [rbp-8h]

  v18 = __readfsqword(0x28u);
  strcpy(s, "picoCTF{br1ng_y0ur_0wn_k3y_");
  strcpy(v10, "}");
  v1 = strlen(s);
  MD5(s, v1, &v10[2]);
  v2 = strlen(v10);
  MD5(v10, v2, v11);
  v4 = 0;
  for ( i = 0; i <= 15; ++i )
  {
    sprintf(&v13[v4], "%02x", (unsigned __int8)v10[i + 2]);
    v4 += 2;
  }
  v5 = 0;
  for ( j = 0; j <= 15; ++j )
  {
    sprintf(&v17[v5], "%02x", (unsigned __int8)v11[j]);
    v5 += 2;
  }
  for ( k = 0; k <= 26; ++k )
    v17[k + 32] = s[k];
  v17[59] = v14;
  v17[60] = v16;
  v17[61] = v15;
  v17[62] = v13[0];
  v17[63] = v16;
  v17[64] = v14;
  v17[65] = v13[12];
  v17[66] = v16;
  v17[67] = v10[0];
  if ( strlen(a1) != 36 )
    return 0LL;
  for ( m = 0; m <= 35; ++m )
  {
    if ( a1[m] != v17[m + 32] )
      return 0LL;
  }
  return 1LL;
}
```
Đến đây tôi chỉ cần debug và tìm phần flag còn thiếu
```
v17[59] = v14;
v17[60] = v16;
v17[61] = v15;
v17[62] = v13[0];
v17[63] = v16;
v17[64] = v14;
v17[65] = v13[12];
v17[66] = v16;
```
