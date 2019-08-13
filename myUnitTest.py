import main
import unittest


class MyUnitTest(unittest.TestCase):
    pairs = [
        [
            'I want to buy the car, becaeuse it is cheap. The car is also luxurius.',
            'I want to buy the car, because it is cheap. The car is also luxurious.'
        ],
        [
            'How far is it from the churc to the station?',
            'How far is it from the church to the station?'
        ],
        [
            'In 1986 a sever nuclear disaster occurred in the city of Chernobyl. It is considered the worst nuclear '
            'disaster in history.' +
            ' It is belived that the disaster was cauded by human error and reactor\'s design flaws',
            'In 1986 a severe nuclear disaster occurred in the city of Chernobyl. It is considered the worst nuclear '
            'disaster in history.' +
            ' It is believed that the disaster was caused by human error and reactor\'s design flaws'
        ]
    ]

    def test_equals(self):
        for pair in self.pairs:
            test_txt = pair[0]
            ref_txt = pair[1]
            output_txt = main.correct(test_txt)
            self.assertEquals(output_txt, ref_txt)

    def test_not_equals(self):
        text = 'Pontedera is near Pisa'  # il dizionario non riconosce la citta di Pontedera
        self.assertNotEqual(main.correct(text), text)


if __name__ == '__main__':
    test = MyUnitTest()
    test.test_equals()
