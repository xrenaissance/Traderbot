import csv

HOUR = 3600
DAY = HOUR * 24

def main():
    pass

class Report(object):
    """docstring for Report."""
    def __init__(self,):
        super(Report, self).__init__()

    def write_csv(self, data, file_name, header):
        """
        Creates csv file and writes data into csv file.

        Inputs
        data: a list of a dictionary or dictionaries.
        file_name: name in the form of a string for csv file that you
        want to create. Exclude the '.csv' suffix. It will be added on
        within this method.
        header: A list of headers for the `.csv` file.

        Exceptions Raised
        PermissionError: when the file being written to is already open.
        ValueError: when the header does not contain the keys provided
        of all dictionaries from within the data parameter.
        """

        file_name = file_name + '.csv'
        try:
            with open(file_name, 'w') as f:
                # `lineterminator = '\n'` is used to prevent the rows from being
                # spaced apart.
                writer = csv.DictWriter(
                    f, fieldnames=header,
                    lineterminator='\n')
                writer.writeheader()
                writer.writerows(data)
        except PermissionError:
            print()
            print("PermissionError:")
            print("Unable to write to csv file \""+file_name+"\".")
            print("Make sure that the excel document\" "+file_name+"\" is closed.\n")
        except ValueError as err:
            print()
            print("ValueError: '+ str(err)")
            print("The header parameter should contain all keys present within")
            print("the list of dictionaries provided in the data parameter.\n")

if __name__ == '__main__':
    main()
