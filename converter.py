import data_handler
import csv


def converter(tables):
    for table in tables:
        data = data_handler.get_all_data(table)
        fieldnames = [name for name in data[0].keys()]
        with open(str(table) + ".csv", "w+") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for line in data:
                writer.writerow(line)
