from bicycle import bicycle
from bicycle import customer
from bicycle import bike_shop

bikes = {'Colnago':(5.0,100.0),
            'Raleigh':(10.5,20.0),
            'Diamond':(6.4,80.0),
            'BMX':(8.2,55.50),
            'Mountain Bike':(5.5,90.0),
            'Scooter':(12.5,200.0)}          
                 
customers = {'James': 200.0, 'Martin': 100.0, 'Nara': 1000.0}

model_count = {'Colnago':2,
            'Raleigh':1,
            'Diamond':3,
            'BMX':3,
            'Mountain Bike':5,
            'Scooter':1}

model_list = []
for bike in bikes:
    model_list.append(bicycle(bike,bikes[bike]))

Halfords= bike_shop('Halfords', model_list, model_count)

customer_list=[]
for cust in customers:
        customer_list.append(customer(cust,customers[cust]))

print "The inventory of "+Halfords.name+" is : "
print Halfords.model_count

for cust in customer_list:
    can_buy = []
    for model in model_list:
        if cust.fund > model.prod_cost*1.2:
            can_buy.append(model.name)
    print cust.name +" can buy a "+",".join(can_buy)
            
for cust in customer_list:
    for model in model_list:
        if cust.fund > model.prod_cost*1.2 and Halfords.model_count[model.name]>0:
            print cust.name + " buying a " + model.name +" which costs "+str(1.2*model.prod_cost)
            Halfords.sale(model.name)
            print "There are now: "+str(Halfords.model_count[model.name])+" " + model.name+" left"
            cust.buy(model)
            break
            
print "The remaining inventory is: "
print Halfords.model_count
print "The profit made is: {}".format(Halfords.profit)