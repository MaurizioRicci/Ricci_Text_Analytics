import main
import unittest


class MyUnitTest(unittest.TestCase):
    pairs = [
        [
            'I want to buy the car, becaeuse it is cheap. The car is also luxurius.',
            'I want to buy the car, because it is cheap. The car is also luxurious.'
        ],
        [
            'how far is it from the churc to the station?',
            'how far is it from the church to the station?'
        ],
        [
            'in 1986 a severe nuclear disaster occurred in the city of Chernobyl. It is considered the worst nuclear '
            'disaster in history.' +
            ' it is belived that the disaster was cauded by human error and reactor\'s design flaws',
            'in 1986 a severe nuclear disaster occurred in the city of Chernobyl. It is considered the worst nuclear '
            'disaster in history.' +
            ' it is believed that the disaster was caused by human error and reactor\'s design flaws'
        ]
    ]

    def test_equals(self):
        for pair in self.pairs:
            test_txt = pair[0]
            ref_txt = pair[1].lower()
            output_txt = main.correct(test_txt)
            self.assertEqual(output_txt, ref_txt, output_txt + ' != ' + ref_txt)

    def test_not_equals(self):
        text = 'Pontedera is near Pisa'  # il dizionario non riconosce la citta di Pontedera
        self.assertNotEqual(main.correct(text), text.lower())


if __name__ == '__main__':
    test = MyUnitTest()
    test.test_equals()
