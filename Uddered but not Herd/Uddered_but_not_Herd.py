ask = input('')
ask2 = input('')
index,count = 0,0
over = False
while over!=True:
    for z in ask:
        if z==ask2[index]:
            index+=1
            if index==len(ask2):
                print(count+1)
                over=True
                break
    count+=1
