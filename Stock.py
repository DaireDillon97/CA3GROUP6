import random
import math
import string
stock_items=[]
basket=[]
total=0
boxes=0
class Stock():
    def __init__(self):
        self.name = ''
        self.good = ''
        self.vat = 0
        self.expiration_date = ''
        self.weight = 0
        self.height = 0
        self.width= 0
        self.depth = 0
        self.id = ''
        self.price = 0
        self.quantity = 0

    def setName(self, n):
        self.name=n
    def getName(self):
        return self.name

    def setGood(self, g):
        self.good=g
    def getGood(self):
        return self.good

    def setVat(self, v):
        self.vat=v
    def getVat(self):
        return self.vat

    def setExpiration_date(self, ex):
        self.expiration_date=ex
    def getExpiration_date(self):
        return self.expiration_date

    def setWeight(self, w):
        self.weight=w
    def getWeight(self):
        return self.weight

    def setHeight(self, h):
        self.height=h
    def getHeight(self):
        return self.height

    def setWidth(self, w):
        self.width = w
    def getWidth(self):
        return self.width

    def setDepth(self, l):
        self.depth = l
    def getDepth(self):
        return self.depth

    def setId(self, ID):
        self.id=ID
    def getId(self):
        return self.id

    def setPrice(self, p):
        self.price=p
    def getPrice(self):
        return self.price

    def setQuantity(self, q):
        self.quantity=q
    def getQuantity(self):
        return self.quantity

    def __str__(self):
        return "Product name: " + str(self.name) + "\nProduct type: "+ str(self.good) +  "\nAssociated vat: " +str(self.vat)+  "\nExpiration date: " +str(self.expiration_date)+  "\nProduct weight: " +str(self.weight)+  "\nProduct height: " +str(self.height)+"\nProduct width: " +str(self.width)+"\nProduct depth: " +str(self.depth)+  "\nProduct id: " +str(self.id)+  "\nProduct price: " +str(self.price)+ "\nProduct quantity: " +str(self.quantity)+ "\n"

    def add_item(name, good, vat, expiration_date, weight, height, width, depth, id, price, quantity):
        global stock_items
        


        for a in stock_items:
            if a.getName() == name:
                val = int(a.quantity) + int(quantity)
                a.setQuantity(val) 
                return stock_items

        s = Stock()
        s.setId(id)
        s.setName(name) 
        s.setGood(good)       
        s.setExpiration_date(expiration_date)
        s.setQuantity(quantity)
        s.setVat(vat)
        s.setExpiration_date(expiration_date)
        s.setPrice(price)
        s.setWeight(weight)
        s.setHeight(height)
        s.setWidth(width)
        s.setDepth(depth)

        stock_items.append(s)

        return stock_items

    def view_all_items():
        for i in range(len(stock_items)):
            print(stock_items[i].__str__())
    
    def delete(name):
        for i in range(len(stock_items)):
            if stock_items[i-1].getName() == name:
                stock_items.remove(stock_items[i-1])
    
    def viewType(temp):
        for i in range(len(stock_items)):
            if stock_items[i].getGood() == temp:
                print(stock_items[i].__str__())


    def addbasket(selec, quant):
        global basket
        for i in range(len(stock_items)):
            if stock_items[i-1].getName() == selec:
                basket.append(stock_items[i])
        for a in basket:
            a.setQuantity(quant) 
            return basket
        
    def viewbasket():
        global total
        for i in range(len(basket)):
            print(basket[i].__str__())
            print(f'the total cost of the products in the basket is: {total}')

    def adjustquant(name, quant):
        for a in stock_items:
            if a.getName() == name:
                val = int(a.quantity) - int(quant)
                a.setQuantity(val) 
                return stock_items


    def getTotal(quant):
        global basket
        global total
        for i in basket:
            price = i.getPrice()
            vat = i.getVat()
            curent2 = int(vat*quant)
            curent = int(price*quant)
            curent3 = curent + curent2
            total = total + curent3
            print(total)
        return total

    def packaging(box_wt):
        global boxes
        for i in basket:
            weight = int(i.getWeight())
            quantity = int(i.getQuantity())
            total_weight = float(weight*quantity)
            if total_weight/box_wt <= 1:
                boxes = boxes + 1
                return boxes
            elif total_weight/box_wt > 1:
                temp = math.ceil(total_weight/box_wt)
                boxes = boxes + temp
                return print(f"The amount of boxes required is {boxes}")
    
    def viewboxes():
        global boxes
        print(boxes)