import base64, sys
print("--------------------------------------------------")
print("----Created by Kingofpython a.k.a Python King-----")
print("--------------------------------------------------")
end = "y"
while end == "y":
    ans = raw_input("Do you want to encode or decode ").lower()
    if ans == "encode" or ans == "1":
        encode = raw_input("What do you want to encode? ")
        encode = base64.b64encode(encode)
        print ("Your encoded text is " + encode)
    if ans == "decode" or ans == "2":
        decode = raw_input("What do you want to decode? ")
        decode = base64.b64decode(decode)
        print ("Your decoded text is " + decode)
    end = raw_input("Again? [Y/N]").lower()
    if end == "n":
        end = "y"
        sys.exit()


    

 

