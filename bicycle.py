class bicycle(object):
    def __init__(self, name, (weight, prod_cost)):
        self.name = name
        self.weight = weight
        self.prod_cost = prod_cost

class bike_shop(object):
    def __init__(self, name, model_list, model_count):
        self.name = name
        self.profit = 0.0
        self.model_count=model_count
        self.model_list = model_list
    
    def sale(self,name):
        for model in self.model_list:
            if model.name == name and self.model_count[name]>0:
                self.model_count[name]-=1
                self.profit += 1.2*model.prod_cost
            elif model.name == name and self.model_count == 0:
                print "Sorry no model {} in stock".format(name)
                   
class customer(object):
    def __init__(self,name,fund):
        self.name = name
        self.fund = fund
        self.bikes = []
    
    def buy(self,name):
        self.bikes.append(name)
        self.fund -= name.prod_cost*1.2
        print self.name + " funds left are " + str(self.fund)
        
            


    