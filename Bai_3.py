import random

list_password = ["CNTT", "KHMT", "KTPM", "HTTT"]

N = int(input())

tk = {}

for i in range(N):
    username = f"202360{str(i+1).zfill(4)}"
    
    password = random.choice(list_password) + username
    
    tk[f"Account{i+1}"] = {
        "Username": username,
        "Password": password
    }

for account, info in tk.items():
    print(f"{account}:")
    print(f"  Username: {info['Username']}")
    print(f"  Password: {info['Password']}")