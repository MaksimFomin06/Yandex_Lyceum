class Goal:
    def __init__(self, *goals):
        self.goals = list(goals)
    
    def target(self, current):
        index_to_remove = None
        for i, goal in enumerate(self.goals):
            if goal <= current:
                index_to_remove = i
                break
        
        if index_to_remove is not None:
            return self.goals.pop(index_to_remove)
        else:
            return self.goals.pop()
    
    def set_goal(self, new_goal):
        if new_goal not in self.goals:
            self.goals.append(new_goal)
    
    def optimus_goal(self):
        if not self.goals:
            return None
        
        if len(self.goals) == 1:
            return self.goals[0]
        
        differences = []
        for i in range(1, len(self.goals)):
            if self.goals[i] > self.goals[i - 1]:
                diff = self.goals[i] - self.goals[i - 1]
                differences.append((diff, self.goals[i]))
        
        if not differences:
            return self.goals[0]
        
        min_diff = min(diff for diff, _ in differences)
        
        for diff, goal in reversed(differences):
            if diff == min_diff:
                return goal
        
        return self.goals[0]
    
    def __str__(self):
        return ", ".join(str(g) for g in self.goals)