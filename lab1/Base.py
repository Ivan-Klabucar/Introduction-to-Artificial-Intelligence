class Node:
    def __init__(self, state, cost, parent, true_cost=None):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.true_cost = true_cost
        self.deleted = False

    def __eq__(self, other):
        if other.cost == self.cost: return True
        return False
    
    def __lt__(self, other):
        if self.cost < other.cost: 
            return True
        else:
            return False


class SearchAlgorithm:
    def __init__(self, state_space):
        self.state_space = state_space
        self.start_state = state_space.start_state
        self.goal_states = state_space.goal_states
        self.solution = None
        self.states_opened_cnt = 0
    
    def calc_path(self):
        if not self.solution:
            raise "Can't calc path when there is no solution"

        path = []
        curr_node = self.solution
        while curr_node:
            path.append(curr_node.state)
            curr_node = curr_node.parent
        return path
    
    def succ(self, state):
        return self.state_space.succ[state]
    
    def h(self, state):
        return self.state_space.h[state]
    
    def print_solution(self):
        if not self.solution:
            print("No goal state could be reached.")
            return

        print(f'States opened = {self.states_opened_cnt}')
        path = self.calc_path()
        print(f'Found path of length {len(path)} with total cost {self.solution.cost}:')
        
        while path:
            if len(path) == 1:
                print(path.pop())
            else:
                print(f'{path.pop()} =>')