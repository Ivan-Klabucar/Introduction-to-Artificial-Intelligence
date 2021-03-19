from StateSpaceLoader import *

class StateSpace:
    def __init__(self, state_space_path, heuristic_path):
        loader = StateSpaceLoader(state_space_path, heuristic_path)
        self.succ, self.h, self.start_state, self.goal_states = loader.load()