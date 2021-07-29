from run_analysis import run_analysis
from util.formatting import goldstandard
import pandas as pd
analysis_results = run_analysis()

def get_counts():
    """
    Calculates precision and recall for analysis model and writes it to a txt-file
    """

    total = 0
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0
    almost_positives = 0

    for result in analysis_results:
        for gold in goldstandard:
            if result == gold:
                total += 1

                if (analysis_results[result] == [None]
                and goldstandard[gold] == [None]):
                    true_negatives += 1

                elif (analysis_results[result] == [None]
                and goldstandard[gold] != [None]):
                    false_negatives += 1
                    
                elif (analysis_results[result] != [None]
                and goldstandard[gold] == [None]):
                    false_positives += 1
                
                else:
                    found_rules = 0
                    total_rules = 0

                    for item in goldstandard[gold]:
                        total_rules += 1
                    for item in analysis_results[result]:
                        if item in goldstandard[gold]:
                            found_rules += 1
                    if found_rules == total_rules:
                        true_positives += 1
                    else:
                        almost_positives += 1

    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    f_measure = (2 * precision * recall) / (precision + recall)

    scores = {"Precision": precision,
                    "Recall": recall,
                    "F_measure": f_measure}

    measures = {"True positives": true_positives,
                    "False negatives": false_negatives,
                    "False positives": false_positives,
                    "True negatives": true_negatives}

    info = [str(pd.DataFrame.from_dict(scores, orient="index", columns=["Measures"])),
            "\n--------------------------\n",
            str(pd.DataFrame.from_dict(measures, orient="index", columns=["Measures"]))]
    
    with open("evaluation.txt", "w") as file:
        for df in info:
            file.write(df)

if __name__ == "__main__":
    get_counts()           
