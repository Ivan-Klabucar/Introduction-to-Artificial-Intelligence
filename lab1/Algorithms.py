from Base import *
import heapq

class BFS(SearchAlgorithm):
    def __init__(self, state_space):
        super().__init__(state_space)
        self.open = []
    
    def new_nodes(self, l):
        self.open.extend([Node(x[0], x[1], x[2]) for x in l])

    def bfs(self):
        self.new_nodes([(self.start_state, 0.0, None)])
        while open:
            n = self.open.pop(0)
            self.visited.add(n.state)
            if n.state in self.goal_states: return n
            l = []
            for transition in self.succ(n.state):
                if transition[0] not in self.visited: l.append((transition[0], transition[1] + n.cost, n))
            l.sort()
            self.new_nodes(l)
        return None
    
    def solve(self):
        self.solution = self.bfs()
        print('# BFS')
        self.print_solution()

class UniformCostSearch(SearchAlgorithm):
    def __init__(self, state_space):
        super().__init__(state_space)
        self.open = []
        heapq.heapify(self.open)
    
    def new_node(self, state, cost, parent):
        heapq.heappush(self.open, Node(state, cost, parent))

    def uniform_cost_search(self):
        self.new_node(self.start_state, 0.0, None)
        while open:
            n = heapq.heappop(self.open)
            self.visited.add(n.state)
            if n.state in self.goal_states: return n
            for transition in self.succ(n.state):
                if transition[0] not in self.visited: self.new_node(transition[0], n.cost + transition[1], n)
        return None
    
    def solve(self):
        self.solution = self.uniform_cost_search()
        print('# UCS')
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
        self.new_node(self.start_state, 0.0 + self.h(self.start_state), None, 0)
        while open:
            n = heapq.heappop(self.open)
            if n.deleted: continue
            self.visited.add(n.state)
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
        print(f'#  A-STAR {self.state_space.heuristic_path}')
        self.print_solution()