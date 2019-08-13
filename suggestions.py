from similarity.levenshtein import Levenshtein
from similarity.jarowinkler import JaroWinkler

levenshtein = Levenshtein()
print(levenshtein.distance('My string', 'My tstring'))

jarowinkler = JaroWinkler()
print(jarowinkler.similarity('My string', 'My tsring'))
print(jarowinkler.similarity('My string', 'My ntrisg'))


def eval_distance(test, ref):
    return levenshtein.distance(test, ref)


def evalSuggestions(testArr, ref, debug= True):
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
