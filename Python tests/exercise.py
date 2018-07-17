###### EXERCISE 6
### Task 1

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })
    
    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total
    
    @classmethod
    def franchise(cls, store):
        new_store = cls(store.name + ' - franchize')
        return new_store

    @staticmethod
    def store_details(store):
        return '{}, total stock price: {}' .format(store.name, int(store.stock_price()))

Amazon = Store('Amazon')
print(Store.store_details(Amazon))

###### EXERCISE 5
### Task 1

# class Store:
#     def __init__(self, name):
#         self.name = name
#         self.items = []


### Task 2
    # def add_item(self, name, price):
    #     item = {'name': name, 'price': price}
    #     self.items.append(item)


### Task 3
    # def stock_price(self):
    #     total = sum([item['price'] for item in self.items])
    #     return total

# new_store = Store('Fora')
# new_store.add_item('tea', 15)
# new_store.add_item('cofee', 20)
# print(new_store.stock_price())

###### EXERCISE 4
### Task 1

# student = {
#     'name': 'Jose',
#     'school': 'Computing',
#     'grades': (66, 77, 88)
# }


### Task 2

# def avarage_grade(data):
#     grades = data['grades']
#     return sum(grades) / len(grades)


### Task 3

# def avarage_grade_all_students(student_list):
#     total = 0
#     count = 0
#     for student in student_list:
#         total += sum(student['grades'])
#         count += len(student['grades'])
#     return total / count


###### EXERCISE 3
### Task 1

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def even_numbers():
#     evens = []
#     for number in numbers:
#         if number % 2 == 0:
#             evens.append(number)
#     return evens

# print(even_numbers())


### Task 2

# def user_menu(choice):
#     if choice == 'a':
#         return 'Add'
#     elif choice == 'q':
#         return 'Quit'
#     else:
#         return 'Error'

# print(user_menu(input('Enter "a" or "q":' )))