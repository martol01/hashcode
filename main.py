def main():
    print('Hello World')

def getMinimumPizzaSlice( input ):
    print(input)
    with open( 'fileTest.csv',  'r') as openFile:
        s = openFile.readlines()
        for x in s:
            values = x.strip('\n').split(',')
            print(values)


getMinimumPizzaSlice(1)