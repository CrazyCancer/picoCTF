# Need For Speed

File: https://jupiter.challenges.picoctf.org/static/cd51b2c95be9f3626db6fe6665afb5a3/need-for-speed

>Description
The name of the game is speed. Are you quick enough to solve this problem and keep it above 50 mph? need-for-speed.

Vẫn như cách làm mọi khi, trước tiên mình sẽ kiểm tra bằng **detect it easy**

![image](https://hackmd.io/_uploads/rJvM50kuA.png)

Chúng ta sẽ mở file bằng IDA64 

Bên dưới là hàm main của chương trình
```c=
int __cdecl main(int argc, const char **argv, const char **envp)
{
  header();
  set_timer();
  get_key();
  print_flag();
  return 0;
}
```
Sau khi xem một lượt sơ qua thì mình nhận thấy rằng hàm `get_key()` sẽ tạo `key` và hàm `print_flag()` sẽ lấy `key` này để giải mã và in ra flag

![image](https://hackmd.io/_uploads/HJCqjRkd0.png)
Có vẻ như trước khi tạo `key` thì nó sẽ qua quá trình kiểm tra nên mình sẽ debug để kiểm tra

![image](https://hackmd.io/_uploads/BkGHlyg_R.png)
Mình chỉ cần `run` và flag đã xuất hiện

