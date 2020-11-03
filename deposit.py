def get_all_coupons():
    with open("coupons.txt","r") as f:
        content=f.readlines()
    coupons=[]
    for loop in content:
        coupons.append((loop.split(";")[0],int(loop.split(";")[1].rsplit()[0])))
    return coupons


def check_coupon(code):
    value=0
    coupons=get_all_coupons()
    for loop in coupons:
        if loop[0]==code:
            value=loop[1]
            break
    return value
