from src.data_manipulation import DataManipulation

class App:
    def __init__(self):
        self.data_manipulation = DataManipulation()

    def keyword_finder(self, filename, word):
        data = self.data_manipulation.find_keyword_in_file(filename, word)
        return data

app = App()
found = app.keyword_finder(r"src/data/extract_from_the_rise_of_the_robots.txt", "robot")
print(found)

app = App()
found_1 = app.keyword_finder(r"src/data/extract_from_the_rise_of_the_robots.txt", "laureate")
print(found_1)