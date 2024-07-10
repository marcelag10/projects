#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:15:21 2024

@author: marcela
"""

import os
import re

def add_prefix_and_combine(input_dir, temp_file):
    # Check if the input directory exists
    if not os.path.isdir(input_dir):
        print(f"Input directory '{input_dir}' does not exist.")
        return
    
    filenames = os.listdir(input_dir)
    filenames = sort_filenames_numerically(filenames)

    with open(temp_file, 'w') as temp_out:
        for filename in filenames:
            input_file_path = os.path.join(input_dir, filename)
            
            if os.path.isfile(input_file_path):
                try:
                    # Open the input file for reading
                    with open(input_file_path, 'r') as f:
                        # Read all lines from the input file
                        lines = f.readlines()

                    for line in lines:
                        line = line.strip()
                        modified_line = "n:" + line
                        # Write the modified line to the temp file
                        temp_out.write(modified_line + '\n')
                    
                    print(f"Processed '{filename}' and written to temp file.")
                except Exception as e:
                    print(f"An error occurred while processing '{filename}': {e}")
            else:
                print(f"Skipping non-file item: {filename}")

def sort_filenames_numerically(filenames):
    def extract_number(filename):
        match = re.search(r'\d+', filename)
        return int(match.group()) if match else float('inf')

    return sorted(filenames, key=extract_number)

def count_entries_in_file(file_path):
    with open(file_path, 'r') as infile:
        return sum(1 for line in infile if line.strip())

def verify_combined_file(output_file, total_entries):
    with open(output_file, 'r') as outfile:
        combined_entries = sum(1 for line in outfile if line.strip())

    print(f"Total entries in combined file: {combined_entries}")
    print(f"Total entries expected: {total_entries}")

    if combined_entries == total_entries:
        print("The total number of entries matches.")
    else:
        print("The total number of entries does not match.")

if __name__ == "__main__":
    input_dir = input("Enter the path of the input directory: ")
    output_file = input("Enter the path of the output file: ")

    temp_file = "temp_combined_file.txt"
    
    add_prefix_and_combine(input_dir, temp_file)
    
    total_entries = count_entries_in_file(temp_file)
    os.rename(temp_file, output_file)
    verify_combined_file(output_file, total_entries)