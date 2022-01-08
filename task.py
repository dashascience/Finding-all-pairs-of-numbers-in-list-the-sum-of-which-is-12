import itertools
import json


class NumberPairsError(Exception):
    """Exception raised for errors in NumbersPairs methods

    Attributes:
        msg -- error explanation
    """

    def __init__(self, msg=""):
        self.msg = msg
        super().__init__(self.msg)


def calculate_all_comb(data: list):
    all_data_combinations = list(itertools.combinations(data, 2))
    return all_data_combinations


class NumbersPairs:

    """Finds all pairs of numbers in list the sum of which is 12

    Attributes:
        input_path -- path to the input file
        output_path -- path to the output_file
    """

    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path

    def read_file(self):
        try:
            with open(self.input_path, 'r') as input_file:
                data = json.loads(input_file.read())
        except FileNotFoundError:
            raise NumberPairsError("The input file path is wrong")
        return data

    def find_pairs(self, data: list = []):
        if not data:
            data = self.read_file()
        result = []
        if len(data) > 1:
            all_data_combinations = calculate_all_comb(data)
            while all_data_combinations:
                num_1, num_2 = all_data_combinations[0]
                if num_1 + num_2 == 12:
                    result.append([num_1, num_2])
                    data.remove(num_1)
                    data.remove(num_2)
                    all_data_combinations = calculate_all_comb(data)
                else:
                    all_data_combinations.remove((num_1, num_2))
        else:
            raise NumberPairsError("The length of input data should be greater than 1")
        return result

    def save_result(self):
        result = self.find_pairs()
        with open(self.output_path, 'w') as output_file:
            output_file.write(json.dumps(result))


number_pairs_init = NumbersPairs('data.txt', 'output.txt')
number_pairs_init.save_result()