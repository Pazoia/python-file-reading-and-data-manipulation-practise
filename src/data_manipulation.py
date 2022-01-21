from .data_extration import DataExtraction

class DataManipulation:
    def __init__(self):
        self.extract_data = DataExtraction()

    def find_keyword_in_file(self, filename, word):
        data = self.extract_data.get_data_from_file(filename)
        data_to_be_searched = data.split(" ")
        for item in data_to_be_searched:
            if item == word:
                return word
