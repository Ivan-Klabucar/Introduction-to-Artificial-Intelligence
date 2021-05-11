import sys
from Parsers import *
from ID3 import ID3
from HelperFunctions import *
from AccuracyCalc import *

path_to_train_data = sys.argv[1]
path_to_test_data = sys.argv[2]
max_depth = None
if len(sys.argv) == 4: max_depth = int(sys.argv[3])
train_dataset = DatasetParser(path_to_train_data).parse()
decision_tree = ID3(max_depth=max_depth)
decision_tree.fit(train_dataset)
decision_tree.print_fit_result()

test_dataset = DatasetParser(path_to_test_data).parse()
predictions = decision_tree.predict(test_dataset)
print_predictions(predictions)
a_calc = AccuracyCalc(test_dataset, predictions)
a_calc.print_accuracy()
a_calc.print_confusion_matrix()

