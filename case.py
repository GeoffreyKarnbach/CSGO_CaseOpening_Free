import random

def get_skin_from_ticket(ID,skins):
    for loop in range(len(skins)):
        if ID>=skins[loop][0] and ID <= skins[loop][1]:
            return (skins[loop][2],skins[loop][3])

def generate_image_series(filename):
    with open(filename,"r") as f:
        content=f.readlines()
    image_list=[]
    
    for loop in content:
        image_list.append(loop.split(";")[2].rstrip())

    sequence=[]

    for loop in range(50):
        sequence.append(random.choice(image_list))
    return sequence

def pull(filename):
    with open(filename,"r") as f:
        content=f.readlines()
    skins=[]
    
    for loop in content:
        skins.append([int(loop.split(";")[0]),int(loop.split(";")[1]),loop.split(";")[2].rstrip(),int(loop.split(";")[3].rstrip())])

    result,price=get_skin_from_ticket(random.randint(0,99999),skins)
    return result,price

def get_expected_value(filename):

    with open(filename,"r") as f:
        content=f.readlines()
    skins=[]
    for loop in content:
        skins.append([int(loop.split(";")[0]),int(loop.split(";")[1]),loop.split(";")[2].rstrip(),int(loop.split(";")[3])])

    drops={}
    total=0
    amountLoop=100000

    for loop in range(amountLoop):
        result,price=get_skin_from_ticket(random.randint(0,99999),skins)
        total+=price
        if result not in drops.keys():
            drops[result]=1
        else:
            drops[result]+=1

    print(drops,total/amountLoop)

#get_expected_value("case3.txt")
#print(pull("case3.txt"))

