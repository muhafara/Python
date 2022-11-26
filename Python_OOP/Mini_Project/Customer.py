import Pizza
class Customer(Pizza):
    
    def __init__(self, name, address, orderno):
        self.customer_name = name
        self.customer_address = address
        self.customer_orderno = orderno
        #self.customer_order = []

    def receipt(self):
        print("*****************Receipt************************")
        print(f"********Customer name :{self.customer_name}**********")
        print(f"******Customer address :{self.customer_address}*********")
        print(f"********Customer name :{self.customer_orderno}**********")
        print("***************************************************")

    def pizza_menu(self):
        pass

    def place_order(self):
        pass


custome_one = Customer("John", "122 london", "112344")
custome_one.receipt()