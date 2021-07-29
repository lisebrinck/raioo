from error_analysis import model_1, model_2
from util.formatting import data, wordlist

def run_analysis():
    """
    Runs the error_analysis on data
    """
    analysis_results = {}
    for wordpair in data:
        if wordpair[0] != wordpair[1]:
            result = model_1([], wordpair[0], wordpair[1], wordlist, wordpair[0])
            if result == None:
                result = model_2(wordpair, wordlist)
            if result != None:
                analysis_results[wordpair] = list(set(result))
            else:
                analysis_results[wordpair] = [None]

    return analysis_results

def write_analysis_to_file():
    """
    Writes the results of the error analysis to a txt-file
    """
    analysis_results = run_analysis()

    with open("testdata/output/data.txt", "w") as file:
        for entry in analysis_results:
            file.write(str(entry) + "\t" + str(analysis_results[entry]) + "\n")

if __name__ == "__main__":
    write_analysis_to_file()