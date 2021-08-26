def model_1(matches, target, error, wordlist, compare):
    """
    Args:
        matches (list): empty list for matches
        target (str): the target word
        compare (str): the target word
        error (str): the misspelled word
        wordlist (dict): dictionary of targets with rules
    Returns:
        list of rules that map onto the error word
    """

    if compare == error:
        return None

    if len(error) < 1 and len(target) < 1:
        return matches

    for key in wordlist:
        if key == compare:
            for rule in wordlist[key]:
                if target.startswith(rule[1]) and error.startswith(rule[0]):
                    target_2 = target
                    error_2 = error
                    matches_2 = matches.copy()
                    if rule[0] != rule[1]:
                        matches_2.append(rule)

                    result = model_1(
                        matches_2,
                        target_2.replace(rule[1], "", 1),
                        error_2.replace(rule[0], "", 1),
                        wordlist,
                        compare,
                    )

                    if result != None:
                        return result


def model_2(wordpair, wordlist):
    """
    Args:
        wordpair (tuple): string of target and error word
        wordlist (dict): dictionary of targets with rules
    Returns:
        list of rules that map onto the error word
    """

    if wordpair[0] == wordpair[1]:
        return None

    matches = []
    ends = ["sion", "ssion", "tion", "ende", "ene", "rer", "ere", "re"]
    starts = ["for", "fore", "in", "im"]

    for key in wordlist:
        if key == wordpair[0]:
            for rule in wordlist[key]:
                
                if rule[1] not in ends and rule[1] not in starts:
                    if rule[0] in wordpair[1] and not rule[1] in wordpair[1]:
                        matches.append(rule)

                if rule[1] in ends:
                    #these letter combinations must appear at the end of the word
                    if (wordpair[1].endswith(rule[0]) 
                    and not wordpair[1].endswith(rule[1])):
                        matches.append(rule)

                if rule[1] in starts:
                    #these letter combinations must appear at the start of the word
                    if (wordpair[1].startswith(rule[0]) 
                    and not wordpair[1].startswith(rule[1])):
                        matches.append(rule)

    if matches != []:
        return list(set(matches))
