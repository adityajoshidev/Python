
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
bids={}
continue_=True
while continue_:
    print(logo)
    print("Welcome to the Blind Auction!")
    name=input("What is your name: ")
    bid=int(input("What is your Bid amount: $"))
    bids[name]=bid
    should_continue=input("Are there any other bidders? Type 'yes' or 'no':").lower()
    if should_continue=='yes':
        print("\n"*20)
    else:
        continue_=False
        max_bid=0
        max_bidder=""
        for key in bids:
            if bids[key]>max_bid:
                max_bid=bids[key]
                max_bidder=key
        print(f"{max_bidder} won the Auction , There Bid was {max_bid}")
