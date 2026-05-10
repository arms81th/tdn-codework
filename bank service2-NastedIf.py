#เป็นการใช้เงื่อนไข Nested If ในการเขียน
#Bank Service
username=input("Enter username:")#ป้อนชื่อบัญชีผู้ใช้
password=input("Enter user password:")#ป้อนรหัสผ่านผู้ใช้

if username=="admin" and password=="1234":
    print("Welcome to login")#เข้าสู่ระบบได้ต่อเมื่อตรงตามเงื่อนไข
    service=input("Enter service number \n Deposit  service(1) \n Transfer service(2) \n Withdraw service(3):")#ป้อนหมายเลขบริการ
    if service=="1":
        print("Deposit service")#บริการรับฝาก
        Account_number=input("Please enter your account number:")#ระบุหมายเลขบัญชี
        Deposit_service=input("Specify the amount:")#ระบุจำนวนเงิน
        print(f"\nSuccessfully deposited {Deposit_service} to account {Account_number}")

    elif service=="2":
        print("Transfer service")#บริการโอนเงิน
        Account_number=input("Please enter your account number:")#ระบุหมายเลขบัญชี
        Transfer_service=input("Specify the amount:")#ระบุจำนวนเงิน
        print(f"\nSuccessfully deposited {Transfer_service} to account {Account_number}")

    elif service=="3":
        print("Withdraw service")#บริการถอน
        Account_number=input("Please enter your account number:")#ระบุหมายเลขบัญชี
        Withdraw_service=input("Specify the amount:")#ระบุจำนวนเงิน
        print(f"\nSuccessfully deposited {Withdraw_service} to account {Account_number}")

    else:
      print("Invalid service number..Please try again")#หมายเลขบริการไม่ถูกต้อง กรุณาลองอีกครั้ง
else:
    print("Username or password is incorrect.")#ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง