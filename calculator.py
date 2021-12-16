def calc(moneygiven, item_cost):
    print ("Change Calculator")

    fifty = 50 
    twenty  = 20 
    ten = 10 
    five = 5 
    two_euro_coin = 2  
    one_euro_coin = 1  
    fifty_cent_coin = 0.5
    twenty_cent_coin = 0.2 
    ten_cent_coin = 0.10 
    five_cent_coin = .05
    two_cent_coin = 0.02
    one_cent_coin = 0.01 

    moneyback = moneygiven - item_cost 

    fiftyback = int(moneyback / fifty) 
    fiftynewbalance=moneyback-fiftyback*fifty

    twentyback=int(fiftynewbalance / twenty) 
    twentynewbalance=fiftynewbalance-twentyback*twenty  

    tenback=int(twentynewbalance / ten) 
    tennewbalance=twentynewbalance-tenback*ten 

    fiveback=int(tennewbalance / five)  
    fivenewbalance=tennewbalance-fiveback*five

    twoback= int(fivenewbalance / two_euro_coin) 
    twonewbalance=fivenewbalance-twoback*two_euro_coin  

    oneback=int(twonewbalance / one_euro_coin)  
    onenewbalance=twonewbalance-oneback*one_euro_coin 

    print (fiftyback,"€ 50 Note")  
    print (twentyback,"€ 20 Note") 
    print (tenback,"€ 10 Note")  
    print (fiveback,"€ 5 Note")
    print (twoback,"€ 2 coin") 
    print (oneback,"€ 1 coin") 

    moneybacknew = moneyback-int(moneyback)
    fifty_cent_back = int(moneybacknew / fifty_cent_coin)

    fifty_cent_total = moneybacknew - fifty_cent_back * fifty_cent_coin 

    twenty_cent_back = int(fifty_cent_total / twenty_cent_coin) 
    twenty_cent_total = fifty_cent_total - twenty_cent_back * twenty_cent_coin

    ten_cent_back = int(twenty_cent_total / ten_cent_coin) 
    ten_cent_total = twenty_cent_total - ten_cent_back * ten_cent_coin 

    five_cent_back = int(ten_cent_total / five_cent_coin)   
    five_cent_total = ten_cent_total - five_cent_back * five_cent_coin

    two_cent_back = int(five_cent_total/ two_cent_coin)
    two_cent_total = five_cent_total - two_cent_back * two_cent_coin

    one_cent_back = int(two_cent_total / one_cent_coin)
    one_cent_total = two_cent_total - one_cent_back * one_cent_coin

    
    print(fifty_cent_back, '50 cents' )  
    print(twenty_cent_back,'20 cents')  
    print(ten_cent_back,'10 cents')  
    print(five_cent_back, '5 cents') 
    print(two_cent_back, '2 cents')
    print(one_cent_back, '1 cents')
