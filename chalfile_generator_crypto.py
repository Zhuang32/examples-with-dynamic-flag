import os,sys
plugins_path = os.path.join(sys.argv[3], "plugins")
sys.path.append(plugins_path)
from chalfile_generator_lib import generator_init, generate_file, generator_finalize
##dont remove the codes above
from gmpy2 import is_prime
from os import urandom

def bytes_to_num(b):
	return int(b.encode('hex'), 16)
	
def num_to_bytes(n):
	b = hex(n)[2:-1]
	b = '0' + b if len(b)%2 == 1 else b
	return b.decode('hex')

def get_a_prime(l):
	random_seed = urandom(l)
	num = bytes_to_num(random_seed)	
	while True:
		if is_prime(num):
			break
		num+=1
	return num

def encrypt(flag):
	p1 = get_a_prime(128)
        p2 = get_a_prime(128)
        n = p1*p2
        e = 0x1001
        p = bytes_to_num(flag)
	p = pow(p, e, n)
	return num_to_bytes(p).encode('hex'),p1,p2

pc = generator_init()
flag = pc.encrypt("PKUCTF{Dynamic_Flag_Is_Powerful}")
text = '''ciphertext = %s
p1 = %d
p2 = %d
''' % encrypt(flag)
generate_file(text, "info.txt")

generator_finalize()
