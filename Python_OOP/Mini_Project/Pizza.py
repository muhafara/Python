import random
class Pizza:

    remember_prefrences = 0
    non_veg_pizza_flavours = {
                                1 :'Margherita Pizza with Cheese and Tomatos',
                                2 : 'Hawaiian Pizza with Ham and pineapple',
                                3 :'Peparoni Pizza with Double Peporoni, Onions, green peppers and mushrooms',
                                4 : 'Vegetarian Delight Pizza with Mushroom, olives, sweetcorn, pineapple, green peppers and onion',
                                5 : 'Vegeterian Hot Pizza with Mushroom, olives, green peppers and olives'
                                }
    veg_pizza_flavours = {
                                1 : 'Beef Spicy Pizza with Spicy beef and mushrooms',
                                2 : 'Meat one Pizza with Spicy beef, ham, spicy chicken and peporoni',
                                3 : 'BBQ Chicken Pizza with Chicken, Mushroom and olives'
        }
    pizza_size = [9, 12, 15, 19]
    pizza_type = ['Deep pan', 'Stuffed crust cheesy bites','Stuffed crust garlic and herbs', 'Stuff crust with cheese', 'Thin crust']
    pizza_topping = ['Olives','Beef', 'Black Olives', 'Chinese chicken', 'Fresh Tomatos', 'Green Peppes', 'Jalapenos', 'Mushroom']

    def __init__(self, name, address):
        self.customer_name = name
        self.customer_address = address

    def generate_order_no(self):
        self.customer_orderno = random.randint(55555, 99999)

    def place_order(self):
        place_order = input("Would you like to order press y for yes and n for no")[0]
        if place_order == 'y':
            Pizza.pizza_menu()
            my_order = int(input("Please select you pizza base from using corrosponding number"))
            if my_order == 1:
                pass
                #here
        else:
            print("Thank you for visiting")
        

        

    def pizza_menu(self):
        print("Please select your prefrences")
        try:
            get_prefrences = int(input("Select 1 for vegeterian and 2 for non-vegeterain"))
            if get_prefrences == 1:
                for key, values in self.veg_pizza_flavours.items():
                    print("---",key,"---",values,"---")
            elif get_prefrences == 2:
                for key, values in self.non_veg_pizza_flavours.items():
                    print("---",key,"---",values,"---")
            else:
                print("Please enter 1 0r 2 only")
        except:
            print("It takes positive integer only 1 0r 2 for initial value")
        

P1 = Pizza("Faran","London")
P1.pizza_menu()