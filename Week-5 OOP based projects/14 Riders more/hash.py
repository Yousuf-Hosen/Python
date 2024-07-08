import hashlib
#Rtrams -> smart
#Spikiyoabr->Lion
email='yousufhasan3538@gmail.com'
pdw="ChairOnTableWith4Legs"
pdw_encode=pdw.encode()
pdw_hash=hashlib.md5(pdw_encode).hexdigest()
your_email='yousufhasan3538@gmail.com'
your_password="5e67c1fc7c5cbd20fd4a350c1b4602ab"
hashed_your_pass=hashlib.md5(your_password.encode()).hexdigest()
if email==your_email and pdw_hash==hashed_your_pass:
    print("right User")
else:
    print("wrong password")


hacker_email='yousufhasan3538@gmail.com'
hacker_password="5e67c1fc7c5cbd20fd4a350c1b4602ab"

print(pdw)
print(pdw_hash)



