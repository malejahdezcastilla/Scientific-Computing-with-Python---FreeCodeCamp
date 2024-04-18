class Category :
    def __init__ (self, name):
        self.ledger = []
        self.name = name

    
    def deposit (self, amount, description = '') :
        self.ledger.append({'amount': amount, 'description': description})

    
    def withdraw (self, amount, description = '') :
        if self.check_funds (amount) :
            self.ledger.append({'amount': -abs (amount), 'description': description})
            
            return True
        else:
            
            return False

    
    def get_balance (self) :
        sum_balance = 0
        for element in self.ledger :
            value = element ['amount']
            sum_balance = sum_balance + value
            
        return sum_balance

    
    def get_total_spent(self):
        expenses = 0

        for item in self.ledger:
            if item['amount'] < 0:
                expenses += abs(item['amount'])

        return expenses


    def transfer (self, amount, category) :
        if self.check_funds (amount) :
            self.withdraw (amount, 'Transfer to {}'.format (category.name))
            category.deposit (amount,'Transfer from {}'.format (self.name))
            return True
        else :
            return False      


    def check_funds (self, amount) :
        if amount > self.get_balance () :
            return False
        else :
            return True 


    def __str__(self) -> str:
        title = self.name.capitalize ().center (30,'*') + "\n"
        ledger = self.ledger
        result = []

        for element in ledger :
            item = "{:<23}".format(element['description'])
            amount = "{:>7.2f}".format(element['amount'])
            category_list = '{}{}'.format (item[:23], amount[:7]) #item + amount 
            result.append (category_list)
            total = self.get_balance ()

        return title + "\n".join (result) + "\n" + 'Total: ' + str (total)
        
          
def create_spend_chart(categories):
    chart_title = 'Percentage spent by category\n'
      
    size_cat_list = len (categories)
    spacing_dashes = size_cat_list + (2)
    x_axis = '    ' + '-'* (size_cat_list + spacing_dashes + 2)+ '\n'
    
    
    expenses_by_category = {}
    total_spent = 0
    percentaje_per_category = {}

    for category in categories:
        expenses_by_category[category.name] = category.get_total_spent()
        total_spent += expenses_by_category[category.name]
    
    for category in categories:
        percentaje_per_category[category.name] = round ((expenses_by_category[category.name] / total_spent) * 100)

    print (percentaje_per_category)        
    y_axis = []
    
    for label in reversed (range(0, 110, 10)) :
        y_labels = '{:>3}| '.format (label)
        
        for category in categories:
            if percentaje_per_category [category.name] >= label :
                y_labels += 'o  '
            else :
                y_labels += '   '     
        
        y_axis.append (y_labels)


    
    name_of_categories = []

    for category in categories :
        category_name = category.name.capitalize ()
        name_of_categories.append (category_name)
        len_long_word = len(max(name_of_categories, key = len))
    
    for index in range (len (name_of_categories)):
        name_of_categories[index] = name_of_categories [index] + ' ' * (len_long_word - len(name_of_categories[index]))

    ch= ''
    for i in range (len_long_word) :
        ch += '     '

        for letter in name_of_categories :
            ch+= letter[i] + '  '

        ch+='\n'   
   
    return chart_title + "\n".join (y_axis) + "\n" + x_axis + (ch.rstrip('\n'))
