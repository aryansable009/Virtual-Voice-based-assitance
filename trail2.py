import pandas as pd
df2 = pd.read_csv('Book2.csv')
df2= df2.set_index('Lodin_ID')
tf = True
while tf == True:   
    id1 = int(input('ENTER LOGN ID : '))
    password = input('ENTER Password : ')
    try:
        passw = df2.loc[id1,'Password'] 
        if passw== password:
            tf = False
        else:
            print('invalid Password')
    except KeyError:
        print ("Invalid Login ID")
order = df2.loc[id1, 'order']
ordp =  df2.loc[id1, 'Order_price']
add = df2.loc[id1, 'shipping_address']

def edit(x,y,z):
    df2.loc[x, y ] = z
