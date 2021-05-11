from HelperFunctions import entropy, without

class Dataset:
    def __init__(self, features, label, entries=None):
        self.features = features
        self.label = label
        self.entries = []
        self.seen_vals = dict()
        self.name_to_idx = dict((name, idx) for idx, name in enumerate(self.features + [self.label]))
        self.idx_to_name = dict((idx, name) for idx, name in enumerate(self.features + [self.label]))
        for f in self.features + [self.label]: self.seen_vals[f] = set()
        if entries: 
            self.entries = entries
        self.__update_seen_vals(self.entries)
    
    def get_entries(self):
        return iter(self.entries)
    
    def size(self):
        return len(self.entries)

    def get_features(self):
        return list(self.features)
    
    def __add_entry(self, e):
        if len(e) != len(self.features) + 1: raise Exception(f"Wrong number of elements in entry: {e}")
        self.entries.append(e)
        
    def add_entry(self, e):
        self.__add_entry(e)
        self.__update_seen_vals([e])
    
    def f(self, idx):
        return self.idx_to_name[idx]
    
    def i(self, feature):
        return self.name_to_idx[feature]
    
    def __update_seen_vals(self, entries):
        for e in entries:
            for idx, fval in enumerate(e):
                self.seen_vals[self.f(idx)].add(fval)
    
    def get_num_of_diff_labels(self):
        num_of_diff_labels = dict((name, 0) for name in self.seen_vals[self.label])
        for e in self.entries:
            num_of_diff_labels[e[-1]] += 1
        return num_of_diff_labels
    
    def entropy(self):
        num_of_diff_labels = self.get_num_of_diff_labels()
        return entropy(list(num_of_diff_labels.values()))
    
    def most_common_label(self):
        num_of_diff_labels = self.get_num_of_diff_labels()
        max_occurance =  num_of_diff_labels[max(num_of_diff_labels, key=lambda x: num_of_diff_labels.get(x))]
        most_common_labels = [lbl for lbl, val in num_of_diff_labels.items() if val == max_occurance]
        most_common_labels.sort()
        return most_common_labels[0]

    def split_on_feature(self, feature):
        dataset_with_only = dict((fval, Dataset(list(self.features), self.label)) for fval in self.seen_vals[feature])
        for e in self.entries:
            dataset_with_only[e[self.i(feature)]].__add_entry(e)
        for d in dataset_with_only.values(): d.__update_seen_vals(d.entries)
        return dataset_with_only

    def printdata(self):
        print(f'features: {" ".join(self.features)}, label: {self.label}')
        for x in self.entries:
            print(f'{" ".join(x)}')
        print("\nSeen vals:")
        for x in self.seen_vals:
            print(f'{x}: {" ".join([j for j in self.seen_vals[x]])}')
        print("\nName ot idx:")
        print(self.name_to_idx)
        print(f'ENtropy: {self.entropy()}')