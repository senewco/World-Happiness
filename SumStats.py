# Simple program that uses DataFrames to look up information in excel spreadsheets.
import pandas as pd

# Prints a line to improve readability
def writeLine():
    for dash in range(0, 27):
        print('-', end = '')

# Prints an extra line for when the program execution ends
def testEnd(i):
    # Formatting
    if(i != 7):
       writeLine()

# Queries DataFrame for specific country's information
def countryLookup(data):
    cName = ""
    while(cName != "Q"):
        cName = ""
        cName = input('Which country would you like to look up for 2017? (Q to quit)')
        totName = 'Country == \"' + cName + '"'
        output = data.query(totName)
        print(output)

def main():    
    data = pd.DataFrame()
    file = list('2014.csv')
    writeLine()
    
    # Main loop
    for i in range(5,8):
        # Read-in for each csv file
        file[3] = str(i)
        realfile = ''.join(file)
        data = pd.read_csv(realfile)

        # Heading
        print('\nSummary statistics for 201{}'.format(i))
        writeLine()

        # Most happy countries
        head = data.head()['Country']
        print('\nTop ten most happy countries:')
        print(head)

        # Least happy countries
        tail = data.tail()['Country']
        print('\nTop ten least happy countries:')
        print(tail)

        # Calculation for mean happiness score
        mean_happy = data['Happiness Score'].mean()
        print('\nAverage happiness score:', end = '\t')
        print('%.2f'%mean_happy)

        # Calculation for mean level of government corruption
        mean_corr = data['Trust (Government Corruption)'].mean()
        print('\nAverage level of corruption:', end = '\t')
        print('%.2f'%mean_corr)
        
        # Calculation for mean life expectancy
        mean_life = data['Health (Life Expectancy)'].mean()
        print('\nAverage life expectancy:', end = '\t')
        print('%.2f'%(mean_life * 100) + ' years')

        # Calculation for highest life expectancy
        max_life = data['Health (Life Expectancy)'].max()
        print('\nMaximum life expectancy:', end = '\t')
        print('%.2f'%(max_life * 100) + ' years\n')
    
        testEnd(i)
    countryLookup(data)
    
main()