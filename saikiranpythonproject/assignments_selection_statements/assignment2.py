def make_amount(rupees_to_make,no_of_five,no_of_one):
    total=(no_of_five*5)+no_of_one
    five_needed=(int) (rupees_to_make/5)
    one_needed=rupees_to_make%5
    if (five_needed<=no_of_five and one_needed<=no_of_one):
        print("5 rupees needed",five_needed)
        print("1 rupees needed",one_needed)
    elif(total==rupees_to_make):
        print("5 rupees- needed",no_of_five)
        print("1 rupees- needed",no_of_one)
    else:
        print("cannot give you the change")
    
make_amount(21,5,2)
print("next line")
make_amount(30,5,2)
