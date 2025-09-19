import csv

class item:
    def __init__(self, n, v, h, w, d):
        self.name = n
        self.value = v
        self.volume = int(h) * int(w) * int(d)

    def __repr__(self):
        return f"{self.name} has a value of ${self.value} and a volume of {self.volume}.\n"

def knapsack(value, volume, cap):
    rvv = []
    for i in range(len(value)):
        rvv.append([value[i] / volume[i], volume[i], value[i], i])
    rvv.sort(reverse=True)
    ans = []
    tvol = 0
    profit = 0
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
    unused = cap - tvol
    return ans, unused, profit

def itemCollection(names, items):
    listofItems = {}
    for i, name in enumerate(names):
        for num in items:
            if i == num:
                if name not in listofItems:
                    listofItems[name] = 1
                else:
                    listofItems[name] += 1
    return listofItems


def main():
    with open('packs.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        menu = []
        volumes = []
        values = []
        names = []
        for row in csv_reader:
            obj = item(row[0], row[1], row[2], row[3], row[4])
            menu.append(obj)
            names.append(row[0])
            volumes.append(obj.volume)
            values.append(int(row[1]))
    print(*menu)

    while True:
        cap = input("Enter the overall limit of the knapsack: ")
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

    items, unused, totalValue = knapsack(values, volumes, cap_int)

    collection = itemCollection(names, items)

    print("The suggested items are:", end=' ')
    for key, value in collection.items():
        print(f"{value} {key},", end=' ')
    print(f"with a total value of ${totalValue}. There were {unused} cubic inches left unused.")


    #print(items, unused)

main()



