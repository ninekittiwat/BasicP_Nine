#n = input("Enter your name:")
#if n == "kittiwat":
#    p = input("Enter your password: ")
#    if p == "123":
#        print("log in success")
#    else :
#        print("wrong password")
#else :
#    print("Not have this account")

#--------------------------------------

n = input("choose your meme(ตะแน๊ว or brainrot): ")

p = " เดอะมอลล์บางกะปิ"
k = " เดอะมอลล์บางแค"
v = " เดอะมอลล์งามวงศ์วาน"

t = " tung tung shura"
tr = " Tralalero Tralala"
b = " Bombardiro Crocodilo"

nn = "ตะแน๊ว"
bb = "brainrot"
if n == "ตะแน๊ว" :
    l = input("เลือกสาขา (p for เดอะมอลล์บางกะปิ , k for เดอะมอลล์บางแค ,v for เดอะมอลล์งามวงศ์วาน): ")
    if l == "p":
        print(nn+p)
    elif l == "k":
        print(nn+k)
    else :
        print(nn+v)
else :
    l = input("เลือกสาขา (t for tung tung shura , tr for Tralalero Tralala , b for Bombardiro Crocodilo: ")
    if l == "t":
        print(bb+t)
    elif l == "tr":
        print(bb+tr)
    else :
        print(bb+b) 