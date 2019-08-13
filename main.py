import tokenizerForBERT
import BERT_model
import suggestions

debug = True


def correct(text):
    max_iterations = 10

    for c in range(max_iterations):
        bert_input, unk_words = tokenizerForBERT.tokenize(text, debug=debug)

        if len(unk_words) > 0: # altrimenti nessun errore rilevato
            predictions = BERT_model.predict(bert_input, debug=debug)
            ordered_predictions = suggestions.evalSuggestions(predictions,
                                                              unk_words[0], debug=debug)
            print('Best 3 suggestions:', ordered_predictions[:3])

            if len(ordered_predictions) > 0:
                best_suggestion = ordered_predictions[0]['w']
                text = text.replace(unk_words[0], best_suggestion)

                if debug:
                    print('Corrected text:', text)
        else:  # no typo found exit loop
            break
        print('------------------------')

    return text


text = 'I want to buy the car, becaeuse it is cheap. The car is also luxurius.'
corrected = correct(text)
print('Corrected text:', corrected)

