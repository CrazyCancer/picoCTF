# Đây là cách giải quyết của tôi

g = 31
p = 97
a = 88
b = 26
text_key = "trudeau"
plain_text = ""
semi_cipher = []
cipher_text = [97965, 185045, 740180, 946995, 1012305, 
21770, 827260, 751065, 718410, 457170, 0, 
903455, 228585, 54425, 740180, 0, 239470, 936110, 10885,
674870, 261240, 293895, 65310, 65310, 185045, 65310, 
283010, 555135, 348320, 533365, 283010, 76195, 130620, 185045]

#ở đây chúng ta sẽ đi tìm key
u = pow(g, a) % p
v = pow(g, b) % p
key = pow(v, a) % p
b_key = pow(u, b) %p
shared_key = key

#sau khi có key thì ta tìm lại semi_cipher từ hàm "encrypt"
for num in cipher_text:
    semi_cipher.append(int(num/shared_key/311))

#và sau khi đã có tất cả thì chỉ việc đi tìm plain_text
key_length = len(text_key)
for i, num in enumerate(semi_cipher[::1]):
    key_char = text_key[i % key_length]
    encrypted_char = chr(num ^ ord(key_char))
    plain_text = encrypted_char + plain_text
  
print(plain_text)

#picoCTF{custom_d2cr0pt6d_019c831c}


