def data_formatting(file):
    """
    Formats input data for use in analysis
    """

    data = []
    text = open(file, "r").read().split("\n")
    for line in text:
        lines = line.split(", ")
        data.append((lines[0], lines[1]))

    return data


def targetwords_formatting(file):
    """
    Formats targetword data for use in analysis
    """

    targetwords = {}
    text = open(file, "r").read().split("\n")
    for line in text:
        lines = line.split(", ")
        targetwords[lines[0]] = lines[1:]

    for key in targetwords:
        valuelist = []
        for value in targetwords[key]:
            values = value.split("-")
            valuelist.append((values[0], values[1]))
        for char in key:
            valuelist.append((char, char))
        targetwords[key] = valuelist

    return targetwords

def goldstandard_formatting(file):
    """
    Formats goldstandard data for use in evaluation
    """

    goldstandard_results = {}
    text = open(file, "r").read().split("\n")
    for line in text:
            lines = line.split("\t")
            target = lines[0].split(", ")[0].replace("(","")
            error = lines[0].split(", ")[1].replace(")","")
            rules = lines[1:]
            wordpair = (target, error)
            
            rulelist = []
            for rule in rules:
                if rule != "None":
                    rule = rule.split(", ")
                    from_part = rule[0].replace("(","")
                    to_part = rule[1].replace(")","")
                    rulelist.append((from_part, to_part))
                else:
                    rulelist.append(None)
            
            goldstandard_results[wordpair] = rulelist
    
    return goldstandard_results

data = data_formatting("testdata/input/data.txt")
wordlist = targetwords_formatting("util/targetwords/targetwords_with_rules.txt")
goldstandard = goldstandard_formatting("testdata/goldstandard/data.txt")
