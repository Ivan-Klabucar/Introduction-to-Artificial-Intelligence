from Dataset import *

class DatasetParser:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
    
    def parse(self):
        with open(self.dataset_path, 'r') as f:
            lines = [l.strip() for l in f.readlines()]
            header = lines.pop(0).split(',')
            entry_len = len(header)
            entries = []
            for idx, l in enumerate(lines):
                entry = l.split(',')
                if len(entry) != entry_len: raise Exception(f"Wrong number of elements on line {idx + 1}")
                entries.append(entry)
            return Dataset(features=header[:-1], label=header[-1], entries=entries)

