import csv

def convert_csv_to_txt():
    """
    Converts data from csv-file extracted from Jotform into txt-format

    Args:
        filename = name csv-file from Jotform
    Returns:
        textfile in testdata/input folder
    """
    
    dictionary = []
    with open("testdata/jotform/data.csv", "r") as file:
        for row in csv.reader(file):
            for string in row:
                if "name" in string:
                    string = string.replace(" ", "")
                    string = string.replace("name:","").replace("value:","").strip().lower().split(',')
                    string[0] = string[0].replace("aa","å").replace("oe","ø").replace("ae","æ")
                    dictionary.append(string[0] + ", " + string[1])

    with open("testdata/input/data.txt", "w") as file:
        for item in dictionary:
            file.write(item + "\n")

if __name__ == "__main__":
    convert_csv_to_txt()