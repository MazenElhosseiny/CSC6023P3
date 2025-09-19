import csv

class item: # Creates a class that stores the objects data of the name, value, and volume
    def __init__(self, n, v, h, w, d):
        self.name = n
        self.value = v
        self.volume = int(h) * int(w) * int(d)

    def __repr__(self): # Used to create the Inventory menu before the user input
        return f"{self.name} has a value of ${self.value} and a volume of {self.volume}in\u00b3."

def knapsack(value, volume, cap): # Changed the knapsack funtion to return the unused volume in the knapsack and the total value of all objects, in addition to the indices of the objects in the knapsack
    rvv = []
    for i in range(len(value)):
        rvv.append([value[i] / volume[i], volume[i], value[i], i])
    rvv.sort(reverse=True)
    ans = []
    tvol = 0
    profit = 0 # This will be used to find the value of all items in the knapsack
    found = True
    while found:
        found = False
        for t in rvv:
            if (t[1] + tvol) <= cap:
                ans.append(t[3])
                tvol += t[1]
                profit += t[2]
                found = True
                break
    unused = cap - tvol #Finding the unused space is very simple once we have loaded up our knapsack to the fullest, it is just the capacity minus the total volume taken up
    return ans, unused, profit # We return 3 values since it makes it cleaner in the code to return the indices of the items in the list, unused space, and total profit

def itemCollection(names, items): # To count all instances of each item that we have in our knapsack
    listofItems = {}
    for i, name in enumerate(names): # Iterate through the list through all the list of names
        for num in items: # Iterate through the instances of the item in the knapsack and add to a counter each time we encounter it
            if i == num:
                if name not in listofItems:
                    listofItems[name] = 1
                else:
                    listofItems[name] += 1
    return listofItems

def userInput():
    while True:
        cap = input("Enter the overall limit of the knapsack in in\u00b3: ")
        if not cap:
            print("No input received.")
        else:
            try:
                cap_int = int(cap)
                if cap_int > 0:
                    break
                else:
                    print("The overall limit must be a positive integer.")
            except ValueError:
                print("Invalid Input.")
    return cap_int

def printCollections(collection, unused, totalValue): # returns the statement required for the end
    statement = "The suggested items are: "
    for key, value in collection.items():
        statement += f"{value} {key}, "
    statement += (f"with a total value of ${totalValue}. There were {unused} cubic inches left unused.")
    return statement

def main(): 
    with open('packs.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        inventory = [] # Creating lists of the inventory for the user to see what we have to choose from
        volumes = [] # Houses the volumes of all items
        values = [] # Houses the values of all items
        names = [] # Houses the names of all items
        for row in csv_reader:
            obj = item(row[0], row[1], row[2], row[3], row[4])
            inventory.append(obj)
            names.append(row[0])
            volumes.append(obj.volume)
            values.append(int(row[1]))
    for ele in inventory: # Prints the inventory for the user
        print(ele)


    capacity = userInput() # Returns the user input capacity size of knapsack
    items, unused, totalValue = knapsack(values, volumes, capacity) # Returns the items indices in a list, the unused space, and the total value
    collection = itemCollection(names, items) # Returns a dictionary that kept count of how many instances of each item we have
    print(printCollections(collection, unused, totalValue)) # Prints the statement at the end

main()



    
                
