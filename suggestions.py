from similarity.levenshtein import Levenshtein
from similarity.optimal_string_alignment import OptimalStringAlignment

levenshtein = Levenshtein()
#print('Levenshtein:', levenshtein.distance('My goem', 'My home'))
#print('Levenshtein:', levenshtein.distance('My goem', 'My go'))

#optimalStringAlignment = OptimalStringAlignment()
#print('Optimal:', optimalStringAlignment.distance('My goem', 'My home'))
#print('Optimal:', optimalStringAlignment.distance('My goem', 'My go'))

def eval_distance(test, ref):
    return levenshtein.distance(test, ref)


def evalSuggestions(testArr, ref, debug= True):
    # valuta un array di candidati contro una parola di riferimento
    res = []
    for testW in testArr:
        res.append({
            'w': testW,
            'dist': eval_distance(testW, ref)
        })
    res.sort(key=lambda k: k['dist'], reverse=False)

    if debug:
        print('Suggestions:', res)

    return res
