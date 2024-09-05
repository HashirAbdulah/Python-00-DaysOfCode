class Shop:
    def __init__(self, sales, expenditure):
        self.sales = sales
        self.expenditure = expenditure

    def __call__(self):
        print(F"The total profit is {self.sales-self.expenditure}")

s=Shop(15000,12000)
s()


# For more dunders methods refer to the web