from data_formatting import wordlist, vowels, initial_clusters, final_clusters, alignments, rules_noninitial, rules
targetwords = open("util/targetwords/data/targetwords.txt", "r").read().split("\n")

def clusters(finalclusters, initialclusters, vowels, entry):
    """
    Tags targetwords with consonant cluster rules

    Args:
        finalclusters: syllable final clusters
        initialclusters: syllable initial clusters
        vowels: spelling and pronunciation of vowels
        entry: dictionary for the target word
    Returns:
        list of rules
    """

    word = entry["word"]
    ipa = entry["ipa"].replace('?','')
    clusters = []

    for cluster in finalclusters:
        if (
            cluster['ipa'] in ipa 
            and cluster['word'] in word
            and not ipa.endswith(cluster['ipa'])
            and not ipa.startswith(cluster['ipa'])
        ):
            clusters.append(cluster['rules'])
        for vowel in vowels:
            if ipa.endswith(vowel + ' ' + cluster['ipa']) and word.endswith(cluster['word']):
                clusters.append(cluster['rules'])
    
    for cluster in initialclusters:
        if (
            cluster['ipa'] in ipa 
            and cluster['word'] in word
            and not ipa.endswith(cluster['ipa']) 
            and not ipa.startswith(cluster['ipa'])
        ):
            clusters.append(cluster['rules'])
        for vowel in vowels:
            if ipa.startswith(cluster['ipa'] + ' ' + vowel) and cluster['word'] in word:
                clusters.append(cluster['rules'])

    return(return_func(clusters)) 

def r_errors(entry):
    """
    Tags targetwords with r_error rules

    Args:
        entry: dictionary for the target word
    Returns:
        list of rules
    """
    
    word = entry["word"]
    ipa = entry["ipa"]
    r_errors = []
    if ipa.endswith(" 6") and not ipa.endswith(" R 6"):
        if word.endswith("ere"):
            for item in ['er-ere', 'erer-ere', 'er-re', 'rer-re']:
                r_errors.append(item)
        elif word.endswith("re"):
            for item in ['er-re', 'rer-re']:
                r_errors.append(item)
        elif word.endswith('rer'):
            for item in ["re-rer", "er-rer"]:
                r_errors.append(item)

    return(return_func(r_errors)) 

def endings(entry):
    """
    Tags targetwords with ending rules

    Args:
        entry: dictionary for the target word
    Returns:
        list of rules
    """
    
    word = entry["word"]
    ipa = entry["ipa"]
    endings = []

    if ipa.endswith('@ n @'):
        if word.endswith('ene'):
            endings.append('ende-ene')
        elif word.endswith('ende'):
            endings.append('ene-ende')
    if (
        (ipa.endswith('@ D @')
        or ipa.endswith('6 D @'))
        and word.endswith('ede')
    ):
        endings.append('et-ede')
    if ipa.endswith('@ D') and word.endswith('et'):
        endings.append('ede-et')

    return(return_func(endings))

def affixes(entry):
    """
    Tags targetwords with affix rules

    Args:
        entry: dictionary for the target word
    Returns:
        list of rules
    """
    
    word = entry["word"]
    ipa = entry["ipa"]
    affixes = []

    if word.startswith('in') and not word.startswith('ind'):
        affixes.append('im-in')
    if word.startswith('im'):
        affixes.append('in-im')

    if word.startswith('for') and not word.startswith('fore'):
        affixes.append('fore-for')
    if word.startswith('fore'):
        affixes.append('for-fore')

    if 'S o:?1 n' in ipa:
        for pair in [
            ("ssion", "tion-ssion"),
            ("ssion", "sion-ssion"),
            ("tion", "sjon-tion"),
            ("tion", "sion-tion")
        ]:
            if pair[0] in word:
                affixes.append(pair[1])
            elif 'sion' in word and "ssion" not in word:
                affixes.append('sjon-sion')
                affixes.append('tion-sion')
    
    return(return_func(affixes))

def clean_up(entry):
    """
    Cleans word entries in preparation for aligner.
    Removes length and stød markers for ipa and changes some phoneme representations.
    Removes hyphens from spelling.
    Adds end-token '#' to spelling and ipa.

    Args:
        entry: dictionary for the target word
    Returns:
        the cleaned dictionary for the target word
    """

    entry["word"] = entry["word"].replace('-','').replace('\'','') + '#'
    entry["ipa"] = entry["ipa"].replace(' ','').replace(':','').replace('?','').replace('6','V').replace('1','').replace('2','').replace('c','@').replace('$','').replace('w','W') + '#'
    
    return entry

def aligner(alignment, matches, word, ipa):
    """
    Aligns phonemes and letters

    Args:
        alignment: list of possible grapheme-phoneme correspondances
        matches: empty list
        word: word entry
        ipa: ipa entry
    Returns:
        list of alignments  
    """

    if len(word) < 1 and len(ipa) < 1:
        return matches
    for char in alignment[ipa[0]]:
        if word.startswith(char):
            ipa_2 = ipa
            word_2 = word
            matches_2 = matches.copy()
            matches_2.append((ipa[0],char))
            result = aligner(alignment, matches_2, word_2.replace(char,'',1), ipa_2.replace(ipa[0],'',1))
            if result != None:
                return result

def others(entry, rules_noninitial, rules, alignment):
    """
    Tags targetwords with other rules

    Args:
        entry: dictionary for the target word
        rules_noninitial: list of rules for non-initial single consonants
        rules: list of other rules
        alignment: list of possible grapheme-phoneme correspondances
    Returns:
        list of rules
    """

    rule_list = []
    entry = clean_up(entry)
    alignment = aligner(alignment, [], entry["word"], entry["ipa"])

    for rule in rules:
        if rule[1] in str(alignment):
            rule_list.append(rule[0])
    for rule in rules_noninitial:
        if not str(alignment).startswith('[' + rule[1]):
            if rule[1] in str(alignment):
                rule_list.append(rule[0])

    return(return_func(rule_list))

def return_func(return_list):
    if return_list != []:
        return(list(set(return_list)))

def rule_matching(wordlist, targetwords):
    rule_list = []
    for word in targetwords:
        for entry in wordlist:
            if entry["word"] == word:
                word_info = [word]
                word_info.append(clusters(final_clusters, initial_clusters, vowels, entry))
                word_info.append(r_errors(entry))
                word_info.append(endings(entry))
                word_info.append(affixes(entry))
                word_info.append(others(entry, rules_noninitial, rules, alignments))
                rule_list.append(str(word_info).replace('[','').replace(']','').replace(', None','').replace('\'',''))

    rule_list = list(set(rule_list))
    rule_list.sort()

    with open("util/targetwords/targetwords_with_rules.txt", "w") as file:
        for word in rule_list:
            file.write(word + "\n")

if __name__ == "__main__":
    rule_matching(wordlist, targetwords)