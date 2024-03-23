def print_table(table, headers, seperator='|'):
    if len(headers) == len(table[0]):

        full_table = [headers] + table # Generates a nested list where the first element is the header
        
        # Calculating the maximum column width for each column
        max_col_lengths = []
        for col_num in range(len(headers)): # Iterates through the column number
            col_lengths = []
            for row in full_table:
                item_length = len(str(row[col_num])) # Finds the length of the item (string)
                col_lengths.append(item_length)
            max_col_lengths.append(max(col_lengths)) # Appends the maximum of the col_length to max_col_lengths
        
        max_row_num_length = len(str(len(table))) # Finds the string length the total number of rows excluding the header

        # Printing the header
        formatted_header = [' ' * max_row_num_length]

        for max_len, item in zip(max_col_lengths, headers):
            space = ' ' * (max_len - len(str(item)))
            formatted_header.append(f'{item}{space}')
        
        # Prints the horizontal seperator line
        formatted_header_str = f' {seperator} '.join(formatted_header)
        print(formatted_header_str)
        print('-' * len(formatted_header_str))

        # Printing table content
        for row_num, row in enumerate(table):

            row_num = str(row_num)
            # Initialize a list that contains space character(s) as the first element
            formatted_row = [f'{' ' * (max_row_num_length - len(row_num))}{row_num}']

            for item, max_len in zip(row, max_col_lengths):
                item = str(item)
                space = ' ' * (max_len - len(item))
                formatted_item = f'{item}{space}'
                formatted_row.append(formatted_item)
            
            print(f' {seperator} '.join(formatted_row))

table = [['13/03/2024', 230.0, '2323', 'Income'], 
         ['13/03/2024', 2356.0, 'Salary', 'Expense'], 
         ['13/03/2024', 23.0, '23', 'Income'], 
         ['13/03/2024', 23.0, '23', 'Expense'], 
         ['13/03/2024', 23.0, '23', 'Income']]

headers = ['Date', 'Amount', 'Description', 'Type']



print_table(table, headers, '|')

'''
Simplest Alternative

def view_transactions():
    if transactions != []:
        print('Format:', ', '.join(table_columns))
        for num, transaction in enumerate(transactions):
            print('')
            print(f'Transaction {num}')
            transaction = [str(item) for item in transaction]
            print(', '.join(transaction))
    else:
        print('--- No transactions ---')

version 01
----------
def print_table(data, headers=[]):
    transpose = [[] for i in range(len(data[0]))]
    for row in data:
        for i, item in enumerate(row):
            transpose[i].append(item)
    
    ## Compute maximum column lengths
    max_col_lengths = []
    for row in transpose:
        col_lengths = [len(str(item)) for item in row]
        max_col_lengths.append(max(col_lengths))

    # Print the transposed data with proper spacing


    for item, length in zip(headers, max_col_lengths):
        space = " " * (length - len(str(item)))
        print(f'  | {item}{space} ', end='')
    print('|')

    for index, row in enumerate(data):
        for item, length in zip(row, max_col_lengths):
            space = " " * (length - len(str(item)))
            print(f'{index} | {item}{space} ', end='')
        print('|')
'''

'''
version simpler
----------
def print_table(table):
    for row in table:
        print("\t".join(map(str, row)))

print_table(table)
'''