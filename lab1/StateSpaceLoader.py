class StateSpaceLoader:
    def __init__(self, state_space_path, heuristic_path):
        self.state_space_path = state_space_path
        self.heuristic_path = heuristic_path
    
    def load_lines_and_remove_comments(self, path):
        lines = []
        with open(path, 'r') as state_file:
            for l in state_file.readlines():
                if l[0] != '#':
                    lines.append(l.strip())
        return lines
    
    def load(self):
        succ = dict()
        h = dict()
        #Loading of transition function
        lines = self.load_lines_and_remove_comments(self.state_space_path)
            
        start_state = lines.pop(0)
        goal_states = lines.pop(0).split(' ')
        
        for l in lines:
            raw = l.split(':')
            from_state = raw[0]
            to_states_raw = raw[1].strip().split(' ')
            to_states = []
            for enrty in to_states_raw:
                pair = enrty.split(',')
                to_states.append((pair[0], float(pair[1])))
            succ[from_state] = to_states
        
        #Loading of heuristic function
        lines = self.load_lines_and_remove_comments(self.heuristic_path)
        for l in lines:
            raw = l.split(':')
            state = raw[0]
            value = float(raw[1].strip())
            h[state] = value
        
        return succ, h, start_state, goal_states