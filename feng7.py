#逢7就跳
for i in range(1,101):
    if int(i)%7==0 or int(i)%10==7 or int(i)//10==7:
	    continue
	else:
	    print(i)