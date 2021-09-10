import operator

def Solve(N,M,ID,PRICE):
    # not enough coins to buy the cheapest item
    if min(PRICE) > M:
        return [-1]

    table = []
    # create a 2d list to hold corresponding price & id
    for i in range(0, len(PRICE)):
        table.append([PRICE[i], ID[i]])
    
    a = sorted(table, key=operator.itemgetter(1), reverse=True) # sort by ID first
    b = sorted(a, key=operator.itemgetter(0)) # then sort by PRICE as per requirement

    shoppingCart = [] # items to be bought

    for item in b:
        if item[0] > M: # over budget
            break
        else:
            shoppingCart.append(item[1]) # buy item
            M = M - item[0] # update budget

    return sorted(shoppingCart) # return in increasing ID order

if __name__ == "__main__":

    # get input from user
    N,M=map(int,input().split())
    PRICE=[]
    ID=[]
    for _ in range(N):
        x,y=map(int,input().split())
        PRICE.append(x)
        ID.append(y)
    
    # calculate results    
    out_ = Solve(N,M,ID,PRICE)
    
    # print out results
    for i in out_:
        print (i)