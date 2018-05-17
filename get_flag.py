import sys  
from Crypto.Cipher import AES 
from binascii import b2a_hex, a2b_hex  
   
class prpcrypt():  
    def __init__(self, key):  
        self.key = key  
        self.mode = AES.MODE_CBC  
       
    def encrypt(self, text):  
        cryptor = AES.new(self.key, self.mode, self.key[-16:])
        length = 16  
        count = len(text)  
        if(count % length != 0) :  
            add = length - (count % length)  
        else:  
            add = 0  
        text = text + ('\0' * add)  
        self.ciphertext = cryptor.encrypt(text)
        return b2a_hex(self.ciphertext)  

    def decrypt(self, text):  
        cryptor = AES.new(self.key, self.mode, self.key[-16:])
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')

if len(sys.argv) <= 1:
    print("You must input your team token!")
    print("e.g. ./get_flag 12345678")
    sys.exit(1)
token = sys.argv[1]
master_flag = "hxp{Th1s_w2sn't_so_h4rd_now_do_web_of_ages!!!Sorry_f0r_f1rst_sh1tty_upload}"
try:
    pc = prpcrypt(token[-32:])
    flag = pc.encrypt(master_flag)
except Exception:
    print("Wrong team token!")
    sys.exit(1)
print(flag)
