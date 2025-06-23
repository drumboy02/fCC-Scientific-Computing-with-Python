class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.balance = 0

    def __str__(self):
        result = ''
        tchars = (30 - len(self.name)) // 2
        title = tchars * '*' + self.name + tchars * '*'
        # print(title)
        result += title + '\n'

        for item in self.ledger:
            ispaces = 23 - len(item['description'])
            litem = item['description'][0:23] + ' ' * ispaces
            lamount = str(format(item['amount'], '.2f'))[0:7]
            aspaces = 7 - len(lamount)
            lamount = ' ' * aspaces + lamount 
            #print(litem + lamount)
            result += litem + lamount + '\n'
        total = 'Total: ' + format(self.balance, '.2f')
        # print('Total:', format(self.balance, '.2f'))
        result += total
        # print(result)
        return result

    def deposit(self, amount, description=''):
        deposit = {
            'amount': amount,
            'description': description
        }
        self.ledger.append(deposit)
        self.balance += amount

    def withdraw(self, amount, description=''):
        if self.balance < amount:
            return False
        withdraw = {
            'amount': -amount,
            'description': description
        }
        self.ledger.append(withdraw)
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category):
        if self.balance < amount:
            return False
        withdraw = {
            'amount': -amount,
            'description': 'Transfer to ' + category.name
        }
        self.ledger.append(withdraw)
        self.balance -= amount
        deposit = {
            'amount': amount,
            'description': 'Transfer from ' + self.name
        }
        category.ledger.append(deposit)
        category.balance += amount
        return True

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True

def create_spend_chart(categories):
    result = 'Percentage spent by category\n'
    total_spent = 0
    cnames = []
    cspent = []
    for category in categories:
        ctotal = 0
        cname = category.name
        cnames.append(cname)
        cledger = category.ledger
        for item in cledger:
            if item['amount'] < 0:
                if item['description'][0:8] != 'Transfer':
                    total_spent += item['amount']
                    ctotal += item['amount']
        cspent.append(ctotal)
    print('cnames', cnames)
    print('cspent', cspent)
    print('total_spent', total_spent)

    for n in range(100, -1, -10):
        p = str(n)
        while len(p) < 4:
            p = ' ' * (3 - len(p)) + p + '|'
            # print(p)
        result += p + '\n'
    # bar chart
    # chart shows the % spent in each category
    # % calculated with withdraws only and will
    # be % of amount spent for each category to
    # total spent for all categories

    # left side labels 0 - 100
    # bars made from 'o' char
    # bar height rounded down to nearest 10
    # horizontal line below bars goes 2 spaces
    # past final bar

    # category names vertically below bar    

    return result

'''
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g   
'''

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
# print(food)

clothing = Category('Clothing')
clothing.deposit(200, 'initial deposit')
clothing.withdraw(100, 'shoes')

auto = Category('Auto')
auto.deposit(150, 'initial deposit')
auto.withdraw(65, 'gas')
auto.transfer(16, food)

print(create_spend_chart([food, clothing, auto]))