import csv


# create csv(comma-separated values) file
def create_csv_file(fname, data):
    with open(fname, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for k, v in data.items():
            writer.writerow([k, v])