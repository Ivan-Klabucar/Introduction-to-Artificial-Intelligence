from Algorithms import *

class HeuristicChecker:
    def check_if_optimistic(self, state_space):
        print(f"# HEURISTIC-OPTIMISTIC {state_space.heuristic_path}")
        optimistic = True
        original_start_state = state_space.start_state
        for curr_state in state_space.h:
            state_space.start_state = curr_state
            algorithm = UniformCostSearch(state_space)
            final_node = algorithm.uniform_cost_search()
            if final_node:
                if state_space.h[curr_state] > final_node.cost:
                    print(f'[CONDITION]: [ERR] h({curr_state}) < h*: {state_space.h[curr_state]} < {final_node.cost}')
                    optimistic = False
                else:
                    print(f'[CONDITION]: [OK] h({curr_state}) < h*: {state_space.h[curr_state]} < {final_node.cost}')
            else:
                # idk msm da je onda bilo kakava vrijednost heuristike optimisticna s obzirom da je h* na neki nacin beskonacan
                continue
        if optimistic:
            print("[CONCLUSION]: Heuristic is optimistic.")
        else:
            print("[CONCLUSION]: Heuristic is not optimistic.")
        print()
        state_space.start_state = original_start_state
    
    def check_if_consistent(self, state_space):
        print(f"#  HEURISTIC-CONSISTENT {state_space.heuristic_path}")
        consistent = True
        for curr_state in state_space.h:
            for transition in state_space.succ[curr_state]:
                next_state = transition[0]
                cost = transition[1]
                if state_space.h[curr_state] > state_space.h[next_state] + cost:
                    consistent = False
                    print(f'[CONDITION]: [ERR] h({curr_state}) <= h({next_state}) + c: {state_space.h[curr_state]} <= {state_space.h[next_state]} + {cost}')
                else:
                    print(f'[CONDITION]: [OK] h({curr_state}) <= h({next_state}) + c: {state_space.h[curr_state]} <= {state_space.h[next_state]} + {cost}')
        if consistent:
            print("[CONCLUSION]: Heuristic is consistent.")
        else:
            print("[CONCLUSION]: Heuristic is not consistent.")
        print()
