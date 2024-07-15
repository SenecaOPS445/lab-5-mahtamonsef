#!/usr/bin/env python3
# Author ID: mmonsef

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r') # Open in  read mode
    contents = f.read() # Read thefile
    f.close()  
    return contents # Return the contents 


def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r') # Open 
    read_data = f.read() # Read the entire file 
    f.close() # Close 
    read_data.split('\n')  # Split by newline characters 
    list__line = read_data.split('\n') # Store the lines into list__line
    noempty_lines = [] # describing an empty list to hold noempty_lines
    for line in list__line:
        if line != '': # Check if the line isn't empty
            noempty_lines.append(line) 
    return noempty_lines


if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))