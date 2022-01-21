class DataExtraction:
    def __init__(self):
        pass

    def get_data_from_file(self, filename):
        with open(filename, "r") as data:
            return data.read()