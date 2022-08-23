def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if (food_type=="N"):
        bill_amount=150*quantity_ordered
        if(distance_in_kms<=6 and distance_in_kms>3):
            bill_amount=bill_amount+3*distance_in_kms
            return bill_amount
        elif(distance_in_kms>6):
            bill_amount=bill_amount+distance_in_kms*6
            return bill_amount
        else:
            return bill_amount
    elif(food_type=="V"):
        bill_amount=120*quantity_ordered
        if(distance_in_kms<=6 and distance_in_kms>3):
            bill_amount=bill_amount+3*distance_in_kms
            return bill_amount
        elif(distance_in_kms>6):
            bill_amount=bill_amount+distance_in_kms*6
            return bill_amount
        else:
            return bill_amount
        

bill_amount=calculate_bill_amount("N",2,7)
bill_amount1=calculate_bill_amount("V",2,7)
print(bill_amount)
print(bill_amount1)