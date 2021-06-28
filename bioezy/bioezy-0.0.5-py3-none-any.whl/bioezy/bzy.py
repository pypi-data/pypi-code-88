import random
import math
import itertools
from collections import defaultdict


def pattern_count(text, pattern):
    """[finds all occurences of a pattern in a text of bases]

    Args:
        text ([string]): [input string]
        pattern ([string]): [pattern to search for in string]

    Returns:
        [int]: [running tally of how many occurrences of text were found in pattern]
    """
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count = count+1
    return count


def frequency_map(text, k):
    """[computes the frequency map of a given string text and integer k, returns a dictionary of each supplied k-mer value]

    Args:
        text ([string]): [input string]
        k ([int]): [determine length of kmer]

    Returns:
        [dict]: [for every length of kmer specified by k(keys), returns how many times it occurs in text(values)]
    """
    freq = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freq[pattern] = 0
        for j in range(n-k+1):
            if text[j:j+k] == pattern:
                freq[pattern] = freq[pattern] + 1
    return freq


def frequent_words(text, k):
    """[list of all keys that have value in freq == k]

    Dependancies: 
        frequency Map

    Args:
        text ([string]): [input string]
        k ([int]): [standard for values returned by frequency map; equal valued kmers are sought out]

    Returns:
        [list]: [when kmer from frequency map occurs as many times as specified k in this function, it is appended to the returned list]
    """
    words = []
    freq = frequency_map(text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            pattern = key
            words.append(pattern)
    return words


def reverse_compliment(pattern):
    """[finds the complement strand of a DNA strand]

    Dependancies: 
        reverse, compliment
    Args:
        pattern ([string]): [string of DNA to be used to find the reverse compliment]

    Returns:
        [string]: [pattern has been reversed and the complimentary base replaces the current one in string pattern]
    """
    pattern = reverse(pattern)  # reverse all letters in a string
    pattern = compliment(pattern)  # complement each letter in a string
    return pattern
    # OR return(pattern[::-1].replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper())


def reverse(pattern):
    """[reverses a string]

    Args:
        pattern ([string]): [string to be reversed]

    Returns:
        [string]: [reversed version of inputted string "pattern"]
    """
    rev = ''.join(reversed(pattern))
    return rev
    # OR return pattern[::-1]


def compliment(pattern):
    """[finds the complimentary strand of DNA "pattern"]

    Args:
        pattern ([string]): [DNA strand of which compliment is found]

    Returns:
        [string]: [compliment of DNA pattern: A -> T, G -> C, T -> A, C -> G]
    """
    basepairs = {"A": "T", "G": "C", "T": "A", "C": "G"}
    complement = ""
    for base in pattern:
        complement += basepairs.get(base)  # Get returns value for key
    return complement


def pattern_matching(pattern, genome):
    """[find all occurrences of a pattern in a string]

    Args:
        pattern ([string]): [input string]
        genome ([string]): [text to be parsed, locating all occurrences of "pattern"]

    Returns:
        [list]: [returns location where text "pattern" is found in text "genome"]
    """
    positions = []
    for i in range(len(genome)-len(pattern)+1):
        if pattern == genome[i:i+len(pattern)]:
            positions.append(i)
    return positions

# -------------------------------------------------------------------------

# def SymbolArray(genome, symbol):
#     array = {}
#     n = len(genome)
#     Extendedgenome = genome + genome[0:n//2]
#     for i in range(n):  # i-th element is the number of occurrences of the symbol in window length len(genome)//2 starting at pos i of Extended genome
#         array[i] = pattern_count(symbol, Extendedgenome[i:i+(n//2)])
#     return array


# FasterSymbol array - takes genome and symbol but computes it quicker by using a better for loop
# uses pattern_count


def symbol_array(genome, symbol):
    """[helps to count the number of C in a window of Extended genome, along with pattern count]

    Dependancies:
        pattern_count

    Args:
        genome ([string]): [string to be parsed]
        symbol ([string]): [whichever nucleotide base to be searched for, ATGC]

    Returns:
        [dict]: [symbol array of genome corresponding to symbol]
    """
    array = {}
    n = len(genome)
    Extendedgenome = genome + genome[0:n//2]

    # look at the first half of genome to compute first array value
    array[0] = pattern_count(symbol, genome[0:n//2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if Extendedgenome[i-1] == symbol:
            array[i] = array[i]-1
        if Extendedgenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array


def skew_array(genome):
    """[keeps track of total no of occurrences of C and G encountered so far in genome]

    Args:
        genome ([string]): [string to be parsed]

    Returns:
        [list]: [tracks how many times nucleotide bases C and G appear in genome]
    """
    Skew = [0]
    for i in range(len(genome)):
        if genome[i] == 'C':
            Skew.append(Skew[i] - 1)
        elif genome[i] == 'G':
            Skew.append(Skew[i] + 1)
        else:
            Skew.append(Skew[i])
    return Skew


def minimum_skew(genome):
    """[location where skew diagram obtains a minimum(location of ori)]

    Dependancies:
        skew_array

    Args:
        genome ([string]): [string to be parsed]

    Returns:
        [list]: [wherever skew diagram obtains a minimum, it is appended to the list]
    """
    positions = []
    array = skew_array(genome)
    positions = []
    count = 0
    minarray = min(array)
    for i in array:
        if i == minarray:
            positions.append(count)
        count += 1
    return positions


def hamming_distance(p, q):
    """[Total no. of mismatches bt strings p and q, pos i in kmers p and q is a mismatch if the symbols at pos i of the 2 strings are not the same]

    Args:
        p ([string]): [first reference string]
        q ([string]): [second reference string]

    Returns:
        [int]: [number of mismatches at every point along strings p[i] and q[i]]
    """
    count = 0
    for x, y in zip(p, q):
        if x != y:
            count += 1
    return count


def approx_pattern_match(text, pattern, d):
    """[find all approximate occurrences of a pattern in a string with at most d mismatches]

    Dependancies:
        hamming_distance

    Args:
        text ([string]): [input string to be searched]
        pattern ([string]): [string that is searched for in text]
        d ([int]): [how many mismatches are permitted]

    Returns:
        [list]: [positions that pattern are located in text with at most d mismatches in that relationship]
    """
    positions = []
    for i in range(len(text)-len(pattern)+1):
        if hamming_distance(text[i:i+len(pattern)], pattern) <= d:
            positions.append(i)
    return positions


def approx_pattern_count(pattern, text, d):
    """[find DnaA boxes by identifying frequent kmers, with d possible mismatches]

    Args:
        text ([string]): [input string to be searched]
        pattern ([string]): [string that is searched for in text]
        d ([int]): [how many mismatches are permitted]

    Returns:
        [int]: [frequent kmers with at most d mismatches]
    """
    count = 0  # initialize count variable
    for i in range(len(text)-len(pattern)+1):
        if hamming_distance(pattern, text[i:i+len(pattern)]) <= d:
            count += 1
    return count

# -------------------------------------------------------------------------


def count(Motifs):
    """[creates a dictionary with all the nucleotides and how much they are present in the j-th column of the Motif matrix]

    Args:
        Motifs ([string matrix]): [holds several DNA strings as kmers - motifs]

    Returns:
        [dict]: [lists of int with nucleotids as keys]
    """
    count = {}
    k = len(Motifs[0])
    for symbol in 'ACGT':
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def profile(Motifs):
    """[frequency of i-th nucleotide in the j-th column of the Motif matrix]

    Dependancies:
        count 

    Args:
        Motifs ([string matrix]): [holds several DNA strings as kmers - motifs]

    Returns:
        [dict]: [all elements of count matrix divided by the number of rows in motifs]
    """
    profile = count(Motifs)
    t = len(Motifs)
    for letter, values in profile.items():
        new_vals = [v / t for v in values]
        profile[letter] = new_vals
    return profile


def consensus(Motifs):
    """[string formed from the most frequent nucleotide per row in Motif matrix]

    Dependancies:
        count

    Args:
        Motifs ([string matrix]): [holds several DNA strings as kmers - motifs]

    Returns:
        [string]: [most popular nucleotides in each column of motif matrix. If Motifs seen correctly from collection of upstream regions, consensus provides a candidate regulatory motif for these regions]
    """
    k = len(Motifs[0])
    Count = count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if Count[symbol][j] > m:
                m = Count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def score(Motifs):
    """[summing the number of symbols in the j-th column of Motifs that do not match the symbol in position j of the consensus string]

    Dependancies:
        consensus, count

    Args:
        Motifs ([string matrix]): [holds several DNA strings as kmers - motifs]

    Returns:
        [int]: [number of unpopular letters in motif matrix, minimizing this score results in the most conservative matrix]
    """
    Count = count(Motifs)
    Consensus = consensus(Motifs)
    letters = {'A', 'C', 'T', 'G'}
    running_sum = 0
    for i, letter in enumerate(Consensus):
        losers = letters - set(letter)
        for remaining_letter in losers:
            running_sum += Count[remaining_letter][i]
    return running_sum


def probability_kmer(text, profile):
    """[Probability of finding a chosen kmer given the profile matrix]

    Args:
        text ([string]): [string to be searched against]
        profile ([dict]): [contains the probability of finding each nucleotide]

    Returns:
        [int]: [multiplication of the probability of each nucleotide's position in text against the listed probability in profile]
    """
    p = 1
    k = len(text)
    for i in range(k):
        char = text[i]
        p *= profile[char][i]
    return p


def profile_most_probable_kmer(text, k, profile):
    """[ a kmer that was most likely to have been generated by profile among all kmers in text]

    Dependancies:
        probability_kmer

    Args:
        text ([string]): [string to be searched against]
        k ([int]): [determines length of kmer]
        profile ([dict]): [contains the probability of finding each nucleotide]

    Returns:
        [string]: [kmer that has the highest probability of being generated]
    """
    n = len(text)
    m = 0
    x = text[1:k]
    for i in range(n-k+1):
        pattern = text[i:i+k]
        p = probability_kmer(pattern, profile)
        if p > m:
            m = p
            x = pattern
    return x


def entropy(nucleotide, probability):
    """[Measure of the uncertainty of a probability distribution]

    Args:
        nucleotide ([string]): [the 4 nucleotides ATGC]
        probability ([int]): [probability of each of the 4 nucleotides in a column]

    Returns
        [int]: [represents conservation of the column. lower entropy is better as it means probability distribution is most likely to occur]
    """
    prob_dist = zip(nucleotide, probability)
    H = 0
    for j in prob_dist:
        for i in j:
            H = H + i*(math.log(i, 2))

    return(-H)

# -------------------------------------------------------------------------


def count_with_pseudocounts(Motifs):
    """[Takes a list of strings Motifs as input and returns the count matrix of Motifs with pseudocounts as a dict of lists]

    Args:
        Motifs ([list]): [list of strings, motifs]

    Returns:
        [dict]: [count matrix of Motifs with pseudocounts as a dict of lists]
    """
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def profile_with_pseudocounts(Motifs):
    """[Takes a list of strings Motifs as input and returns the profile matrix of Motifs with pseudocount as a dict of lists]

    Args:
        Motifs ([list]): [list of strings, motifs]

    Returns:
        [dict]: [profile matrix of Motifs with pseudocount as a dict of lists]
    """
    k = len(Motifs[0])
    profile = {}
    count = count_with_pseudocounts(Motifs)
    total = 0
    for symbol in "ACGT":
        total += count[symbol][0]
        for k, v in count.items():
            profile[k] = [x/total for x in v]
    return profile


def greedy_motif_with_pseudocounts(Dna, k, t):
    """[Generates each profile matrix with pseudocounts]

    Dependancies:
         score,consensus,count,Pr,profile_most_probable_kmer, profile_with_pseudocounts, count_with_pseudocounts

    Args:
        Dna ([string]): [reference sequence to be searched]
        k ([int]): [determines length of kmer]
        t ([int]): [total length parameter (range)]

    Returns:
        [list]: [A collection of strings BestMotifs resulting from running greedy_motif_search(Dna, k, t) with
                pseudocounts. If at any step you find more than one Profile-most probable k-mer in a given string,
                use the one occurring first.]
    """
    BestMotifs = []
    for i in range(t):
        BestMotifs.append(Dna[i][:k])
    n = len(Dna[0])
    for _ in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = profile_with_pseudocounts(Motifs[0:j])
            Motifs.append(profile_most_probable_kmer(Dna[j], k, P))
        if score(Motifs) < score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


def motifs(profile, Dna):
    """[takes a profile Matrix profile corresponding to a list of strings Dna as input and returns a list of the profile most probable k-mers in each string from Dna]

    Dependancies:
        profile_most_probable_kmer

    Args:
        profile ([string]): [reference sequence to be searched]
        Dna ([string]): [profile Matrix profile corresponding to a list of strings]

    Returns:
        [type]: [description]
    """
    Motifs = []
    t = len(Dna)
    k = 4
    for i in range(t):
        motif = profile_most_probable_kmer(Dna[i], k, profile)
        Motifs.append(motif)
    return motifs


def random_motifs(Dna, k, t):
    """[choose a random kmer from each of t different strings Dna and returns a list of t strings which continuously iterates for as long as the score of the constructed motifs keep improving]

    Args:
        Dna ([string]): [reference sequence to be searched]
        k ([int]): [determines length of kmer]
        t ([int]): [total length parameter (range)]

    Returns:
        [list]: [lowest scoring motifs which would represent the most conservative ones.]
    """
    t = len(Dna)
    l = len(Dna[0])
    RandomMotif = []
    for i in range(t):
        r = random.randint(0, l-k)
        RandomMotif.append(Dna[i][r:r+k])
    return RandomMotif


def random_motif_search(Dna, k, t):
    """[starts by generating a collection of random motifs using the random_motifs function which we set as the best scoring collection of motifs. It continuously runs until motif score stops improving.]

    Dependancies: 
        random_motifs, profile_with_pseudocounts, Motifs, score

    Args:
        Dna ([string]): [reference sequence to be searched]
        k ([int]): [determines length of kmer]
        t ([int]): [total length parameter (range)]

    Returns:
        [list]: [best scoring motifs representing the most conservative ones from a RANDOM MOTIF SELECTION]
    """
    M = random_motifs(Dna, k, t)
    BestMotifs = M

    while True:
        profile = profile_with_pseudocounts(M)
        M = motifs(profile, Dna)
        if score(M) < score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs


def repeated_random_motif_search(Dna, k, t):
    """[finds best scoring motif]

    Dependancies:
        uses randommotif, profile_with_pseudocounts,count_with_pseudocounts,score,consensus,count,motifs,Pr,random_motif_search

    Args:
        Dna ([string]): [reference sequence to be searched]
        k ([int]): [determines length of kmer]
        t ([int]): [total length parameter (range)]

    Returns:
        [list]: [The best scoring motif in Dna]
    """
    Bestscore = float('inf')
    BestMotifs = []
    for i in range(len(Dna)):
        Motifs = random_motif_search(Dna, k, t)
        Currscore = score(Motifs)
        if Currscore < Bestscore:
            Bestscore = Currscore
            BestMotifs = Motifs
    return BestMotifs


def normalize(Probabilities):
    """[rescale a collection of probabilities so that they sum to 1. It takes a dict Probabilities whose keys are kmers values are probabilities of these kmers. It then divides each value in Probabilities by the sum of all values in Probabilities,returning the resulting dict.]

    Args:
        Probabilities ([dict]): [keys are kmers and values of probabilities of these kmers to occur]

    Returns:
        [dict]: [original keys with values rescaled so they sum to 1]
    """
    sumd = sum(Probabilities.values())
    for key in Probabilities.keys():
        Probabilities[key] /= sumd
    return Probabilities


def weighted_die(Probabilities):
    """[takes a dict Probabilities whose keys are kmers and values are Prob of these Kmers]

    Args:
        Probabilities ([dict]): [keys are kmers and values of probabilities of these kmers to occur]

    Returns:
        [string]: [most probable kmer with respect to values in probabilities]
    """
    kmer = ''  # output variable
    num = random.uniform(0, 1)
    sumd = 0
    for key in Probabilities.keys():
        sumd += Probabilities[key]
        if num < sumd:
            kmer = key
            break
    return kmer


def profile_generated_string(text, profile, k):
    """[returns a randomly generated kmer from text whose probabilities are generated from profile]

    Dependancies:
        normalize, weighted_die, profile_most_probable_kmer

    Args:
        Dna ([string]): [reference sequence to be searched]
        k ([int]): [determines length of kmer]
        t ([int]): [total length parameter (range)]

    Returns:
        [string]: [randomly generated kmer from text whose probabilities are generated from profile]
    """
    n = len(text)
    probabilities = {}
    for i in range(n-k+1):
        probabilities[text[i:i+k]] = probability_kmer(text[i:i+k], profile)
    probabilities = normalize(probabilities)
    return weighted_die(probabilities)


def gibbs_sampler(Dna, k, t, N):
    """[ discards a single kmer from the current set of motifs at each iteration and decides to either keep or replace one
# continuously to generate a suboptimal solution particularly for different search problems with elusive motifs (local optimum)]

    Dependancies:
        randommotifs, count_with_pseudocounts,profile_with_pseudocounts,profilegeneratingstring,normalize,weighteddie, pr,score,consensus,count

    Args:
        Dna ([string]): [reference sequence to be searched]
        k ([int]): [determines length of kmer]
        t ([int]): [total length parameter (range)]
        N ([int]): [iterator]

    Returns:
        [list]: [GibbsSampler(Dna, k, t, N)]
    """
    BestMotifs = []
    Motifs = random_motifs(Dna, k, t)
    BestMotifs = Motifs
    for _ in range(N):
        i = random.randint(0, t-1)
        new_Motif = []
        for k1 in range(t):
            if k1 != i:
                new_Motif.append(Motifs[k1])
        profile = profile_with_pseudocounts(new_Motif)
        motif_i = profile_generated_string(Dna[i], profile, k)
        Motifs[i] = motif_i
        if score(Motifs) < score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

# ------------------------------------------------------------------------------------------------------


def list_to_string(mylist):
    """[# A simple function to convert a list of values to a string of values with no separators
]

    Args:
        s ([list]): [list of values]

    Returns:
        [string]: [joint values from list]
    """
    return ' '.join(str(word) for word in mylist)


def find_clumps(genome, k, L, t):
    """[ Returns all distinct k-mers forming (L, t)-clumps in Genome]

    Dependancies:
        pattern_count
    Args:
        genome ([string]): [genome / nucleotide sequence to be parsed]
        k ([int]): [length of k-mer / DnaA box]
        L ([int]): [length of ori]
        t ([int]): [occurrence expected in genome - clump expected to be found at least 't' times]
    """
    # k is len of k-mer/DnaA box, L is length of genome, t is occurence
    count = {}
    for i in range(L):
        pattern = genome[i:i+k]
        if (pattern_count(genome, pattern) == t):
            count[pattern] = pattern_count(genome, pattern)
    print(" ".join(count.keys()))
    return count


def permute_motif_once(motif, alphabet={"A", "C", "G", "T"}):
    """
    Gets all strings within hamming distance 1 of motif and returns it as a
    list.
    """

    return list(set(itertools.chain.from_iterable([[
        motif[:pos] + nucleotide + motif[pos + 1:] for
        nucleotide in alphabet] for
        pos in range(len(motif))])))


def permute_motif_distance_times(motif, d):
    workingSet = {motif}
    for _ in range(d):
        workingSet = set(itertools.chain.from_iterable(map(permute_motif_once, workingSet)))
    return list(workingSet)


def freq_words_mismatch(Genome, k, d):
    """[A most frequent k-mer with up to d mismatches in Text is
        simply a string Pattern maximizing Countd(Text, Pattern) among all k-mersary]

    Dependancies:
        permute_motif_once, permute_motif_distance_times

    Args:
        Genome ([string]): [string to be parsed]
        k ([int]): [determines length of kmer]
        d ([int]): [mismatch allowance]

    Returns:
        [list]: [most frequent kmers]
    """
    aprox_frq_words = []
    frequencies = defaultdict(lambda: 0)
    # all existent kmers with d mismatches of current kmer in genome
    for index in range(len(Genome) - k + 1):
        curr_kmer_and_neighbors = permute_motif_distance_times(Genome[index: index + k], d)
        for kmer in curr_kmer_and_neighbors:
            frequencies[kmer] += 1

    for kmer in frequencies:
        if frequencies[kmer] == max(frequencies.values()):
            aprox_frq_words.append(kmer)
    return aprox_frq_words


def pattern_matching_with_mismatch(text, pat, d):
    count = 0
    for i in range(0, len(text)):
        p = text[i:i+len(pat)]
        if len(p) != len(pat):
            break
        if hamming_distance(p, pat) <= d:
            count = count+1
    return count


def pattern_to_number(pattern):
    if len(pattern) == 0:
        return
    SymbolToNumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    if len(pattern) == 1:
        return SymbolToNumber[pattern]
    n = len(pattern)
    symbol = pattern[n-1]
    prefix = pattern[:n-1]
    return (4*pattern_to_number(prefix)+SymbolToNumber[symbol])


def number_to_pattern(index, k):
    NumberToSymbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    if k == 1:
        return NumberToSymbol[index]
    prefix_index = index//4
    r = index % 4
    symbol = NumberToSymbol[r]
    return number_to_pattern(prefix_index, k-1)+symbol


def mismatches_and_reverse_compliment(text, k, d):
    """[account for both mismatches and reverse complements.
        Recall that Patternrc refers to the reverse complement of Pattern.]

    Dependancies:
        pattern_to_number,number_to_pattern,pattern_matching,hamming_distance,reverse_compliment


    Args:
        text ([string]): [string to be parsed]
        k ([int]): [determines length of kmer]
        d ([int]): [mistmatch allowance]

    Returns:
        [dict]: [performs pattern matching accounting for both reverse compliments of regular and mismatches]
    """
    frequencyarray = {}
    rev_text = reverse_compliment(text)
    for i in range(0, 4**k):
        frequencyarray[i] = 0
    for i in frequencyarray:
        count, r_count = 0, 0
        count = pattern_matching_with_mismatch(text, number_to_pattern(i, k), d)
        r_count = pattern_matching_with_mismatch(rev_text, number_to_pattern(i, k), d)
        frequencyarray[i] = count+r_count
    return frequencyarray


def neighbors(Pattern, d):
    """[Our idea for generating neighbors(Pattern, d) is as follows. If we remove the first symbol of Pattern
        then we will obtain a (k − 1)-mer sequence denoted SuffixNeighbors. Find all possible combinations for each base and each SuffixNeighbor
        k-neighbors of any k-mer is an easy way of generating all kmers.]

    Args:
        Pattern ([string]): [string to be parsed]
        d ([int]): [mismatch allowance]

    Returns:
        [list]: [all suffixes in d-neighborhood]
    """
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        return {"A", "C", "G", "T"}
    Neighborhood = []
    Suffixneighbors = neighbors(Pattern[1:], d)
    for Text in Suffixneighbors:
        if hamming_distance(Pattern[1:], Text) < d:
            for x in {"A", "C", "G", "T"}:
                Neighborhood.append(x + Text)
        else:
            Neighborhood.append(Pattern[0] + Text)
    return Neighborhood

#---------------------------------------------------------------------------------------

def suffix(Pattern):
    """ 
    return every symbol in pattern except the first
    """
    if len(Pattern) == 1:
        return ""
    Sufx = Pattern[1:]
    return Sufx


def first_symbol(Pattern):
    """ 
    return first symbol of pattern
    """ 
    x = Pattern[0]
    return x

def motif_enumeration(Dna, k, d):
    """[A kmer is a k,d motif if it appears in every string
       from Dna with at most d mismatches]
    
    Dependancies:
        neighbours,suffix,first_symbol,hamming_distance

    Args:
        Dna ([string]): [space separated string sequences of nucleotides]
        k ([int]): [determines length of kmer]
        d ([int]): [mismatch allowance]

    Returns:
        [string]: [Returns all (k,d)-motifs in Dna]
    """
    patterns = set()
    n = len(Dna)
    AllKmers = []
    for j in range(n):
        a = Dna[j]
        kmers = []
        n_1 = len(a)
        for i in range(n_1 - k + 1):
            kmers.append(a[i:i+k])
        neigh = []
        for i in range(len(kmers)):
            l = UpdateNeighbours(kmers[i], d)
            for val in l:
                neigh.append(val)
        AllKmers.append(neigh)
    x1 = set(AllKmers[0])
    x2 = set(AllKmers[1])
    patterns = x1 and x2
    for y in range(2, len(AllKmers)):
        patterns = patterns and set(AllKmers[y])
    patterns = list(patterns)
    string = ""
    for i in patterns:
        string = string + i + " "
    return string


def median_string(Dna, k):
    """[a fast algorithm for generating Motifs(Pattern,Dna), a collection of Motifs(Pattern,Dna) as a collection
        of kmers that minimize d(Pattern,Motifs) where d is the hamming distance]
        **NB: fails as long as a single sequence does not have the transcription factor binding sight.
        Runtime: len(dna) * (k+ k**d) * len(dna) * k

    Dependancies
        neighbors, hamming_distance
        
    Args:
        Dna ([string]): [space separated string sequences of nucleotides]
        k ([int]): [determines length of kmer]

    Returns
        [string]: [kmer pattern minimizing d(Pattern,Dna) among all possible choices of kmer]
    """

    def get_distance(Pattern, Text):
        n = len(Text)
        k = len(Pattern)
        min_distance = hamming_distance(Text[:k], Pattern)
        for i in range(n - k + 1):
            distance = hamming_distance(Text[i:i + k], Pattern)
            if distance < min_distance:
                min_distance = distance
        return min_distance

    def get_total_distance(Pattern, Dna):
        total_distance = 0
        for text in Dna:
            distance = get_distance(Pattern, text)
            total_distance += distance
        return total_distance

    min_pattern = first_symbol(Pattern)
    min_total_distance = get_total_distance(min_pattern, Dna)
    for pattern in Suffix(Pattern):
        total_distance = get_total_distance(pattern, Dna)
        if total_distance < min_total_distance:
            min_pattern = pattern
            min_total_distance = total_distance

    return min_pattern


def distance_between_pattern_and_string(Pattern, Dna):
    """[the sum of distances between Pattern and each string in Dna = {Dna1, ..., Dnat}]

    Dependancies:
        hamming_distance
    
    Args:
        Pattern ([string]): [k-mer pattern reference to be searched for in Dna]
        Dna ([string]): [space separated string sequences of nucleotides]

    Returns:
        [int]: [the distance between Pattern and Dna - score]
    """
    k = len(Pattern)
    d = 0
    for text in Dna:
        d_temp = float('Inf')
        for i in range(len(text) - k + 1):
            if d_temp > hamming_distance(Pattern, text[i:i+k]):
                d_temp = hamming_distance(Pattern, text[i:i+k])
        d += d_temp
    return d

def profile_most_probable_kmer_noPR(text, k, profile):
    """[a kmer that was most likely to have been generated by profile among all kmers in text]

    Dependancies:
        probability_kmer

    Args:
        text ([string]): [string to be searched against]
        k ([int]): [determines length of kmer]
        profile ([dict]): [contains the probability of finding each nucleotide]

    Returns:
        [string]: [kmer that has the highest probability of being generated]
    """
    probability = []
    for i in range(len(text)-k+1):
        compute = 1
        for j in range(k):
            compute = compute*(profile[text[i+j]][j])
        probability.append(compute)
    idx = probability.index(max(probability))
    return text[idx:idx+k]

def greedy_motif_search(Dna, k, t):
    """[selects the most attractive candidate from the profile using profile_most_probable_kmer]

    Dependancies:
        score,profile,profilemostprobablekmer

    Args:
        Dna ([string]): [reference sequence to be searched]
        k ([int]): [determines length of kmer]
        t ([int]): [total length parameter (range)]

    Returns:
        [list]: [A collection of strings BestMotifs]
    """
    bestmotifs = [string[:k]for string in Dna]
    for j in range(len(Dna[0])-k+1):
        motifs = [Dna[0][j:j+k]]
        for i in range(1, t):
            motifs += [profile_most_probable_kmer_noPR(Dna[i], k, profile(motifs))]
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs