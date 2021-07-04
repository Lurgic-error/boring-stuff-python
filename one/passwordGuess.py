password = open('pswfile.txt').read()
userPwd = input("Enter your password...\n")
if password == userPwd:
    print("What it do bebiiiiii...?")
    userKey = input("\n Press enter to exit...")
    print(userKey)
elif userPwd == '12345':
    print("Really niggah...?")
else:
    print("Access Denied")