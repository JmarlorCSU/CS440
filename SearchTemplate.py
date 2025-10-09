# Do not change the class name or add any other libraries
from queue import PriorityQueue, Queue

class Problem(object):
    def __init__(self):
        self.set_initial_state()
        self.create_actions()
    
    def set_initial_state(self):
        self.initial_state = [[8, 5, 3],
                              [2, 1, 7],
                              [4, 6, 0]
                              ]
        self.state = self.initial_state

    def create_actions(self):
        self.row = [0, 0, -1, 1]
        self.column = [-1, 1, 0, 0]
        self.moves = ["left", "right", "up", "down"]
    
    def goal_test(self, state):
        goal_state =  [[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 0]
                       ]
        return state == goal_state

    def is_goal(self):
        return self.goal_test(self.state)
    
    def get_cost(self,action):
        return 1
    
    def heuristic(self, state, ucs_flag=False):
        if ucs_flag:
            return 0
        else:
            return self.your_heuristic_function(state)

    def your_heuristic_function(self, state):
        heuristic = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                        number = state[i][j]
                        if number != 0:
                            goal_row = (number - 1) // 3 # 7 - 1 div 3 = 0
                            goal_col = (number - 1) % 3 # 7 - 1 mod 3 = 0 
                            heuristic += abs(i - goal_row) + abs(j - goal_col)
                            # manhattan distance calculation between current and goal positions
        return heuristic
    
    def get_successors(self, state):
        successor_list = []

        # Return coordinates of blank space (i, j)
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    temp_i = i
                    temp_j = j
                    break

        # calculate each move using offset vectors
        for k in range(4):
            # generate coordinates for each move 'left' 'right' 'up' 'down'
            new_i = temp_i + self.row[k]
            new_j = temp_j + self.column[k]
            # check boundaries on coordinates
            if  3 <= new_i <= 0 or 0 <= new_j >= 3:

                state_copy = state[0:2, 0:2] # generate copy of parent state
                state_copy[i][j], state_copy[new_i][new_j] = \
                state_copy[new_i][new_j],  state_copy[i][j]
                successor_list.append(state_copy)

class Node(object):
    def __init__(self, state):
        ''' Feel free to add any additional arguments you need'''
        # You should add whatever fields you need here for your search
    def get_plan(self):
        ''' Return the plan to reach self from the start state'''
        raise NotImplementedError("Your code goes here")
    def get_path_cost(self):
        ''' Return the path cost to reach self from the start state'''
        raise NotImplementedError("Your code goes here")

def astar_graph_search(problem, ucs_flag=False):
    start_state = Node(problem.initial_state)
    # Define fringe and closed list
    path = [] # to track the states taken to reach the goal

    # It should return a Node object
    # You should pass the ucs_flag to the heuristic function
    # and you are only allowed to use the method problem.heuristic() in the search code.
    raise NotImplementedError("Your code goes here")

if __name__ == "__main__":
    ### DO NOT CHANGE THE CODE BELOW ###
    import time
    problem = Problem()
    start = time.time()
    node = astar_graph_search(problem)
    print("Time taken: ", time.time() - start)
    print("Plan: ", node.get_plan())
    print("Path Cost: ", node.get_path_cost())
    # UCS search
    start = time.time()
    node = astar_graph_search(problem, ucs_flag=True)
    print("Time taken: ", time.time() - start)
    print("Plan: ", node.get_plan())
    print("Path Cost: ", node.get_path_cost())


