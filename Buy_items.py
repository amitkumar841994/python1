print('**********','welcome to Shop','**********')
items=float(input('Enter the number of items'))
if(items<10):
    print('Total cost of product is =',120*items)
elif(items>=10 and items<99):
    print('Total cost of product is =',items*100)
elif(items>=100):
    print('Total cost of product is =',items*70)
else:
    print('Invalid input')


