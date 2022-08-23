account_number=1011
account_balance=40000
salary=250000
loan_type="car"
laon_amount_expected=300000
customer_emi_expected=30
while (account_number>=10):
    account_number=account_number//10
    
if (account_number==1):
    if(account_balance>1):
        if(salary>25000 and loan_type=="car"):
            eligible_loan_amount=500000
            no_of_emi_required=36
            if (laon_amount_expected<=eligible_loan_amount and no_of_emi_required>=customer_emi_expected):
                print("you are eligible for the loan",laon_amount_expected,"with emi",customer_emi_expected)
            else:
                print ("you are eligible for the loan",laon_amount_expected,"with emi",customer_emi_expected)
        elif(salary>50000 and loan_type=="house"):
            eligible_loan_amount=6000000
            no_of_emi_required=60
            if (laon_amount_expected<=eligible_loan_amount and no_of_emi_required>=customer_emi_expected):
                print("you are eligible for the loan",laon_amount_expected,"with emi",customer_emi_expected)
            else:
                print ("you are eligible for the loan",laon_amount_expected,"with emi",customer_emi_expected)
        elif(salary>75000 and loan_type=="business"):
            eligible_loan_amount=7500000
            no_of_emi_required=84
            if (laon_amount_expected<=eligible_loan_amount and no_of_emi_required>=customer_emi_expected):
                print("you are eligible for the loan",laon_amount_expected,"with emi",customer_emi_expected)
            else:
                print ("you are eligible for the loan",laon_amount_expected,"with emi",customer_emi_expected)
        else:
            print("enter valid loan type")
    else:
        print("your account balance is low!")
else:
    print("valid account number!")