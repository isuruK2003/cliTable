def print_table(table, headers, v_sep='|', h_sep='_'):
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
        
        formatted_header_str = f' {v_sep} '.join(formatted_header)
        print(formatted_header_str)

        # Prints the horizontal seperator line
        print(f'{h_sep}{v_sep}{h_sep}'.join( (h_sep * len(item) for item in formatted_header) ))

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
            
            print(f' {v_sep} '.join(formatted_row))

if __name__ == '__main__':

    # Example

    table = [
                ['13/03/2024', 230.0, '2323', 'Income'], 
                ['13/03/2024', 2356.0, 'Salary', 'Expense'], 
                ['13/03/2024', 23.0, '23', 'Income'], 
                ['13/03/2024', 23.0, '23', 'Expense'], 
                ['13/03/2024', 23.0, '23', 'Income'],
                ['13/03/2024', 23.0, '23', 'Income'],
                ['13/03/2024', 23.0, '23', 'Income'],
                ['13/03/2024', 23.0, '23', 'Income'],
                ['13/03/2024', 23.0, '23', 'Income'],
                ['13/03/2024', 23.0, '23', 'Income'],
            ]

    headers = ['Date', 'Amount', 'Description', 'Type']

    print_table(table, headers, '│', '―')