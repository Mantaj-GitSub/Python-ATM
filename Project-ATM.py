Balance = 10000
print("""
Kindly Enter Your Choice: 
      
1.Check Balance
2.Deposit Money
3.Withdraw Money
4.Exit   
      """)
choice = int(input("Enter Your Choice: "))

if 1<=choice<=4 :
    while 1<=choice<=4:
       
        if choice == 1:
            print("Your balance is: {:,.2f}".format(Balance))
            
        elif choice == 2:
            dpamt = int(input("Enter Deposit Amount: "))
            Balance += dpamt
            print("Deposit Successful. Your New Balance is {:,.2f} ".format(Balance))

        elif choice == 3:
            wdamt = int(input("Enter Withdrawal Amount: "))
            if wdamt>Balance:
                print("Insufficient Funds!")
            else:
                Balance -= wdamt
                print("Withdrawal Successful. Your New Balance is {:,.2f}".format(Balance))

        elif choice == 4:
            print("Thank You For Using Our ATM!")
            break
        
        print("""
Kindly Enter Your Choice: 
              
1.Check Balance
2.Deposit Money
3.Withdraw Money
4.Exit   
              """)
        
        choice = int(input("Enter Your Choice: "))
    
    if choice<1 or choice>4:
        print("Please Enter a Valid Choice")

else:
    print("Please Enter a Valid Choice")   



        




                

