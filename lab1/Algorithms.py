from Base import *
import heapq

class BFS(SearchAlgorithm):
    def __init__(self, state_space):
        super().__init__(state_space)
        self.open = []
    
    def new_node(self, state, cost, parent):
        self.open.append(Node(state, cost, parent))
        self.states_opened_cnt += 1

    def bfs(self):
        self.new_node(self.start_state, 0, None)
        while open:
            n = self.open.pop(0)
            if n.state in self.goal_states: return n
            for transition in self.succ(n.state):
                self.new_node(transition[0], 1 + n.cost, n)
        return None
    
    def solve(self):
        self.solution = self.bfs()
        self.print_solution()

class UniformCostSearch(SearchAlgorithm):
    def __init__(self, state_space):
        super().__init__(state_space)
        self.open = []
        heapq.heapify(self.open)
    
    def new_node(self, state, cost, parent):
        heapq.heappush(self.open, Node(state, cost, parent))
        self.states_opened_cnt += 1

    def uniform_cost_search(self):
        self.new_node(self.start_state, 0, None)
        while open:
            n = heapq.heappop(self.open)
            if n.state in self.goal_states: return n
            for transition in self.succ(n.state):
                self.new_node(transition[0], n.cost + transition[1], n)
        return None
    
    def solve(self):
        self.solution = self.uniform_cost_search()
        self.print_solution()

class AStarSearch(SearchAlgorithm):
    def __init__(self, state_space):
        super().__init__(state_space)
        self.open = []
        heapq.heapify(self.open)
        self.node_record = dict()
    
    def new_node(self, state, cost, parent, true_cost):
        node = Node(state, cost, parent, true_cost)
        heapq.heappush(self.open, node)
        self.node_record[state] = node

    def a_star_search(self):
        self.new_node(self.start_state, 0 + self.h(self.start_state), None, 0)
        while open:
            n = heapq.heappop(self.open)
            if n.deleted: continue
            if n.state in self.goal_states: return n
            for transition in self.succ(n.state):
                new_state = transition[0]
                new_true_cost = n.true_cost + transition[1]
                new_cost = new_true_cost + self.h(new_state)
                if new_state in self.node_record:
                    if self.node_record[new_state].true_cost < new_true_cost: 
                        continue
                    else:
                        self.node_record[new_state].deleted = True
                        del self.node_record[new_state]
                self.new_node(new_state, new_cost, n, new_true_cost)
        return None
    
    def solve(self):
        self.solution = self.a_star_search()
        self.states_opened_cnt = len(self.node_record) - len(self.open) + 1
        self.print_solution()