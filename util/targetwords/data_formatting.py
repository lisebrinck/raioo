def wordlist_formatting(file):
    """
    Generates a dictionary from the festival wordlist
    """
    wordlist = []
    #the format is slightly different for inflected and uninflected items, so two lists are needed
    inflectionless_items = []
    inflected_items = []
    text = open(file, "r").read().split("\n")
    
    for line in text:
        if (
            '#en' not in line #to remove English words
            and line.startswith('("')
        ):
            if not line.endswith(')))'):
                inflectionless_items.append(line)
            elif 'e.g.' not in line and ';' not in line: #to remove the items that are just inflections
                inflected_items.append(line)
    
    for item in inflectionless_items:
        info = {}
        info['word'] = item.split()[0].replace('"','').replace('(','').lower() #the word itself
        info['pos'] = item.split()[1] #the part-of-speech
        info['ipa'] = item.split('(')[2].replace('))', '').strip() #the pronunciation
        info['infl'] = 'UNKNOWN' #the inflection, which is missing for these items
        wordlist.append(info)
    for item in inflected_items:
        info = {}
        info['word'] = item.split()[0].replace('"','').replace('(','')
        info['pos'] = item.split()[1]
        info['ipa'] = item.split('(')[2].replace(')', '').strip()
        info['infl'] = item.split('pos')[1].replace(')))', '').replace('"', '').strip() #the inflection
        wordlist.append(info)
    
    return wordlist
    
def vowels_formatting(file):
    """
    List of all vowels and their representations in the wordlist above
    """
    vowels = open(file, "r").read().split("\n")
    return vowels
    
def clusters_formatting(file):
    """
    List of the pronunciation and spelling of consonant clusters
    """
    clusters = []
    text = open(file, "r").read().split("\n")
    for line in text:
        info = {}
        info['word'] = line.split('\t')[0]
        info['ipa'] = line.split('\t')[1]
        info['rules'] = line.split('\t')[2]
        clusters.append(info)
    return clusters
    
def alignments_formatting(file):
    """
    Dictionary with phonemes and their possible spellings for use in phoneme-grapheme alignment
    """
    alignments = {}
    p2g = []
    text = open(file, "r").read().split("\n")
    
    for line in text:
        line = line.split('\t')
        p2g.append((line[0].replace('?','').replace(':',''), line[1]))
        #the length and stød markers are removed
    
    for item in p2g:
        alignments[item[0]] = []
    
    for key in alignments:
        for item in p2g:
            if item[0] == key:
                alignments[key].append(item[1])
    
    return alignments

def rules_formatting(file):
    """
    List of all the spelling rules and the target's pronunciation
    """
    rules = []
    text = open(file, "r").read().split("\n")
    
    for line in text:
        lines = line.split('\t')
        rules.append((lines[0], lines[1]))
    
    return rules

path = "util/targetwords/data/"
wordlist = wordlist_formatting(path + "festival.txt")
vowels = vowels_formatting(path + "vowels.txt")
initial_clusters = clusters_formatting(path + "initialclusters.txt")
final_clusters = clusters_formatting(path + "finalclusters.txt")
alignments = alignments_formatting(path + "bogstavlyd.txt")
rules_noninitial = rules_formatting(path + "rules_noninitial.txt")
rules = rules_formatting(path + "rules.txt")