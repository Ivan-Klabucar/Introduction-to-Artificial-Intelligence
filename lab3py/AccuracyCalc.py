class AccuracyCalc:
    def __init__(self, dataset, predictions):
        self.dataset = dataset
        self.predictions = predictions

    def print_accuracy(self):
        correct = 0
        for idx, e in enumerate(self.dataset.get_entries()):
            if e[-1] == self.predictions[idx]: correct +=1 
        print(f'[ACCURACY]: {(correct/self.dataset.size()):.5f}')
    
    def print_confusion_matrix(self):
        print('[CONFUSION_MATRIX]:')
        labels = set(lbl for lbl, val in self.dataset.get_num_of_diff_labels().items() if val != 0)
        labels.update(self.predictions)
        col_iterator = lambda: ((lbl, 0) for lbl in labels)
        c_matrix = dict((lbl, dict(col_iterator())) for lbl in labels)  # {row_label: {col_label1: num, col_label2: num2...}...}
        for idx, e in enumerate(self.dataset.get_entries()):
            c_matrix[e[-1]][self.predictions[idx]] += 1
        for row in sorted(list(labels)):
            for col in sorted(list(labels)):
                print(c_matrix[row][col], end=' ')
            print()




