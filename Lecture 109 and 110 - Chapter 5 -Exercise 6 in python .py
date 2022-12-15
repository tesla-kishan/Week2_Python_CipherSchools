def countlist(l):
    count = 0
    for i in l:
        if type(i)== list:
            count += 1
    print(count)

l=['123',['sandarbh'],['7654'],'bajpai']
countlist(l)