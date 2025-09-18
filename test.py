import csv

class item:
    def __init__(self, n, v, l, w, h):
        self.name = n
        self.value = v
        self.volume = int(l) * int(w) * int(h)

def knapsack(value, volume, cap):
    rvv = []
    for i in range(len(value)):
        rvv.append(value[i]/volume[i], volume[i], value[i], i)
    rvv.sort(reverse=True)
    ans = []
    tvol = 0
    found = True
    while found:
        found = False
        for t in rvv:
            if (t[1] + tvol) <= cap:
                ans.append(t[3])
                tvol += t[1]
                found = True
                break
    openSpace = cap - tvol
    return ans, openSpace

def main():
    with open('packs.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        items = []
        for row in csv_reader:
            obj = item(row[0], row[1], row[2], row[3], row[4])
            items.append(obj)
        print(items)
    
    while True:
        cap = input("Enter the overall limit of the knapsack: ")
        if not cap:
            print("No input recieved.")
        else:
            try:
                cap_int = int(cap)
                if cap_int > 0:
                    break
                else:
                    print("The overall limit must be a positive integer.")
            except ValueError:
                print("Invalid Input.")

                
main()

          
    
                
