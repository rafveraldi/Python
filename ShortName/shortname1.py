import csv

with open('shortname.csv', newline='') as original_file:
    reader = csv.reader(original_file)
    header = next(reader)
    with open('shortname2.csv', 'w', newline='') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(header) # Write header
        for row in reader:
            if row[2] == '': row[2] = 0 # Replace None for 0 so the integer tranformation works in the next line
            row[3] = row[1].split()[:int(row[2])] # Split and slice the words from the first column
            row[3] = " ".join(row[3]) # Transfor the sliced list into a String
            row[3] = row[3].replace(',','') # Clean unwanted commas
            writer.writerow(row) # Write row
    new_file.close()
original_file.close()