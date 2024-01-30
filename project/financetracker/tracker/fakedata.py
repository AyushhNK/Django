from .models import Transaction

# Example data for transactions
Transaction.objects.create(description='Groceries', amount=120.50, date='2024-01-15')
Transaction.objects.create(description='Dinner with friends', amount=75.30, date='2024-01-20')
Transaction.objects.create(description='Online shopping', amount=200.00, date='2024-01-25')
Transaction.objects.create(description='Gasoline', amount=40.00, date='2024-02-01')
Transaction.objects.create(description='Rent payment', amount=1200.00, date='2024-02-05')

Transaction.objects.create(description='Electronics purchase', amount=450.99, date='2024-02-10')
Transaction.objects.create(description='Coffee shop', amount=15.50, date='2024-02-15')
Transaction.objects.create(description='Gym membership', amount=80.00, date='2024-02-20')
Transaction.objects.create(description='Movie night', amount=30.00, date='2024-02-25')
Transaction.objects.create(description='Clothing shopping', amount=100.75, date='2024-03-01')

Transaction.objects.create(description='Utility bills', amount=200.00, date='2024-03-05')
Transaction.objects.create(description='Bookstore purchase', amount=25.20, date='2024-03-10')
Transaction.objects.create(description='Car maintenance', amount=150.00, date='2024-03-15')
Transaction.objects.create(description='Vacation expenses', amount=800.00, date='2024-03-20')
Transaction.objects.create(description='Home decor', amount=60.00, date='2024-03-25')

Transaction.objects.create(description='Health insurance', amount=300.00, date='2024-04-01')
Transaction.objects.create(description='Tech gadgets', amount=500.50, date='2024-04-05')
Transaction.objects.create(description='Family dinner', amount=90.25, date='2024-04-10')
Transaction.objects.create(description='Public transportation', amount=15.00, date='2024-04-15')
Transaction.objects.create(description='Fitness class', amount=40.00, date='2024-04-20')
