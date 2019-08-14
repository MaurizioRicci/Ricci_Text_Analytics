import bertInput
import BERT_model
import suggestions

debug = True
MAX_ITERATIONS = 10

def correct(text):
    text = text.lower()

    for c in range(MAX_ITERATIONS):
        # creo l'input per BERT e ottengo la lista delle parole errate
        bert_input, unk_words = bertInput.format_str(text, debug=debug)

        if len(unk_words) > 0: # altrimenti nessun errore rilevato
            predictions = BERT_model.predict(bert_input, debug=debug)  # ottengo predizioni da BERT
            ordered_predictions = suggestions.evalSuggestions(predictions,  # confronto le predizioni con l'input errato
                                                              unk_words[0], debug=debug)
            print('Best 3 suggestions:', ordered_predictions[:3])

            if len(ordered_predictions) > 0:
                best_suggestion = ordered_predictions[0]['w']
                text = text.replace(unk_words[0], best_suggestion)  # rimpiazzo la parola errata con la miglior scelta e cerco altri errori

                if debug:
                    print('Corrected text:', text)
        else:  # no typo found exit loop
            break
        print('------------------------')

    return text


text = 'I want to buy the car, becaeuse it is cheap. The car is also luxurius.'
corrected = correct(text)
print('Corrected text:', corrected)

