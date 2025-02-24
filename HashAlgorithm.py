from hashlib import sha256
import time
import random

leadingZeros = 0
nonce = random.random()
hashCount = 0
hash = sha256(str(nonce).encode("utf-8")).hexdigest()
start = time.time()
print("Searching for hash...")
while (True):
	leadingZeros = 0
	for x in hash:
		if(x == "0"):
			leadingZeros += 1
		else:
			break
	if(leadingZeros > 5):
		print(hash)
		end = time.time()
		length = end - start
		print("It took", round(length, 2), "seconds to find the correct hash.")
		print("Hash rate:", round((hashCount / 1000) / length, 2), "Kh/s")
		break
	else:
		hashCount += 1
		nonce = random.random()
		hash = sha256(str(nonce).encode("utf-8")).hexdigest()
