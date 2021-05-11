
class ID3:
    def __init__(self, already_split=None, max_depth=None):
        self.feature = None
        self.label_decision = None
        self.edges = dict()
        self.information_gain = dict()
        self.already_split = set()
        self.max_depth = max_depth
        self.most_common_label = None
        if already_split: self.already_split.update(already_split)
    
    def add_child(self, fval, child):
        self.edges[fval] = child

    def print_info_gain(self):
        l = [(ig, fval) for fval, ig in self.information_gain.items()]
        l.sort()
        l.reverse()
        for ig, fval in l:
            print(f'IG({fval})={round(ig,4)} ', end='')
        print()

    def __best_feature(self):
        best = self.information_gain[max(self.information_gain, key=lambda x: self.information_gain.get(x))]
        candidates = [f for f, val in self.information_gain.items() if val == best]
        candidates.sort()
        return candidates[0]
    
    def fit(self, dataset, depth=0):
        def become_leaf():
            self.label_decision = self.most_common_label
            return self

        if dataset.size() == 0: raise Exception("Cannot run ID3 on empty dataset!")
        total_entropy = dataset.entropy()
        self.most_common_label = dataset.most_common_label()
        if total_entropy == 0 or self.max_depth == depth: return become_leaf()
        total_size = dataset.size()
        for f in dataset.get_features():
            if f in self.already_split: continue
            self.information_gain[f] = total_entropy
            possible_split = dataset.split_on_feature(f)
            for fval, curr_dataset in possible_split.items():
                self.information_gain[f] -= (curr_dataset.size()/total_size) * curr_dataset.entropy()
        if not self.information_gain: return become_leaf()
        self.print_info_gain()
        chosen_feature = self.__best_feature()
        #if self.information_gain[chosen_feature] == 0: return become_leaf()
        self.feature = chosen_feature
        self.already_split.add(chosen_feature)
        final_split = dataset.split_on_feature(chosen_feature)
        for fval, curr_dataset in final_split.items():
            self.add_child(fval, ID3(already_split=self.already_split, max_depth=self.max_depth).fit(curr_dataset, depth=depth + 1))
        return self
    
    def predict(self, dataset):
        result = []
        for e in dataset.get_entries():
            curr_id3 = self
            while not curr_id3.label_decision:
                fval = e[dataset.i(curr_id3.feature)]
                if fval in curr_id3.edges:
                    curr_id3 = curr_id3.edges[fval]
                else:
                    break
            decision = curr_id3.most_common_label
            if curr_id3.label_decision: decision = curr_id3.label_decision
            result.append(decision)
        return result
    
    def print_fit_result(self):
        print('[BRANCHES]:')
        self.print_branches()
    
    def print_branches(self, depth=1, history=''):
        if self.label_decision: 
            print(history + self.label_decision)
            return
        history += f'{depth}:{self.feature}='
        results = []
        for fval, child in self.edges.items():
            curr_history = history + fval + ' '
            child.print_branches(depth+1, curr_history)


