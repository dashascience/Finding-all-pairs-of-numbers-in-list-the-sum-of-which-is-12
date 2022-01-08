import json
from unittest import TestCase, main
from task import NumbersPairs, NumberPairsError

test_inputs = [[4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0],
               [4, 9, 8, 10, 2, 6, 6, 6], []]

test_outputs = [[[4, 8], [0, 12], [1, 11], [4, 8], [12, 0]],
                [[4, 8], [10, 2], [6, 6]], [[4, 8], [0, 12], [1, 11], [4, 8], [12, 0]]]


class Test(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number_pairs_init = NumbersPairs('data.txt', 'output.txt')

    def test_find_pairs(self):
        for test_input, test_output in zip(test_inputs, test_outputs):
            self.assertEqual(test_output, self.number_pairs_init.find_pairs(test_input))

    def test_one_number_input(self):
        with self.assertRaises(NumberPairsError):
            self.number_pairs_init.find_pairs([3])

    def test_read_file(self):
        self.assertEqual([4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 8, 11, 12, 0],
                         self.number_pairs_init.read_file())

    def test_save_result(self):
        self.number_pairs_init.save_result()
        with open('output.txt', 'r') as output_file:
            output_data = json.loads(output_file.read())
        self.assertEqual([[4, 8], [0, 12], [1, 11], [4, 8], [12, 0]],
                         output_data)


if __name__ == '__main__':
    main()
