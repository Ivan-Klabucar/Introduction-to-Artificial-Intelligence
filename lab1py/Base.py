class Node:
    def __init__(self, state, cost, parent, true_cost=None):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.true_cost = true_cost
        self.deleted = False

    def __eq__(self, other):
        if other.cost == self.cost and other.state == self.state: return True
        return False
    
    def __lt__(self, other):
        if self.cost < other.cost: 
            return True
        elif self.cost == other.cost and self.state < other.state:
            return True
        else:
            return False


class SearchAlgorithm:
    def __init__(self, state_space):
        self.state_space = state_space
        self.start_state = state_space.start_state
        self.goal_states = state_space.goal_states
        self.solution = None
        self.visited = set()
    
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
        solution_found = "yes"
        if not self.solution: solution_found = "no"
        print(f"[FOUND_SOLUTION]: {solution_found}")
        if not self.solution: return
        print(f'[STATES_VISITED]: {len(self.visited)}')
        path = self.calc_path()
        print(f'[PATH_LENGTH]: {len(path)}')
        print(f'[TOTAL_COST]: {self.solution.cost}')
        print(f'[PATH]: ', end="")
        while path:
            if len(path) == 1:
                print(path.pop())
            else:
                print(f'{path.pop()} => ', end="")