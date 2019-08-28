def eval_distance(s, t):
    """
            iterative_levenshtein(s, t) -> ldist
            ldist is the Levenshtein distance between the strings
            s and t.
            For all i and j, dist[i,j] will contain the Levenshtein
            distance between the first i characters of s and the
            first j characters of t
        """
    rows = len(s) + 1
    cols = len(t) + 1
    # creazione matrice
    dist = [[0 for x in range(cols)] for x in range(rows)]
    # matrice con prima colonna e riga numerate
    for i in range(1, rows):
        dist[i][0] = i
    for i in range(1, cols):
        dist[0][i] = i

    for col in range(1, cols):
        for row in range(1, rows):
            cost = 0 if s[row - 1] == t[col - 1] else 1
            dist[row][col] = min(dist[row - 1][col] + 1,  # deletion
                                 dist[row][col - 1] + 1,  # insertion
                                 dist[row - 1][col - 1] + cost)  # substitution
    return dist[row][col]


def evalSuggestions(testArr, ref, debug=True):
    # valuta un array di candidati contro una parola di riferimento
    def word_ref_distance(it):
        return dict(w=it, dist=eval_distance(it, ref))

    res = map(word_ref_distance, testArr)
    res = sorted(res, key=lambda k: k['dist'], reverse=False)

    if debug:
        print('Suggestions:', res)

    return res
