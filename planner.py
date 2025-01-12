from unified_planning.shortcuts import *
unified_planning.shortcuts.get_environment().credits_stream = None

import sys



if __name__ == "__maine__":
    _input = sys.argv[1]
    print(_input)
    words = _input.split(' ')
    
    Word = UserType('Word')
   
class Communicator:
    def __init__(self):
        self.problem = None
        self.solution = None
        self.objects = None
        
    def input(self, _input):
        
        Excomm = UserType('Excomm') # Communicational assumption
        
        index = unified_planning.model.Fluent('index', x=Excomm)
        after = unified_planning.model.Fluent('after', x_after=Excomm, x_before=Excomm)
        termed = unified_planning.model.Fluent('termed', x=Excomm)
        
        move_index = unified_planning.model.InstantaneousAction('move_index', x_from=Excomm, x_to=Excomm)
        x_from = move_index.parameter('x_from')
        x_to = move_index.parameter('x_to')
        move_index.add_precondition(after(x_to, x_from))
        move_index.add_precondition(index(x_from))
        move_index.add_effect(index(x_to), True)
        move_index.add_effect(index(x_from), False)    
        
        term = unified_planning.model.InstantaneousAction('term', x=Excomm)
        x = term.parameter('x')
        term.add_precondition(index(x))
        term.add_effect(termed(x), True)
        
        
        problem = unified_planning.model.Problem('problem')
        problem.add_fluent(index, default_initial_value=False)
        problem.add_fluent(after, default_initial_value=False)
        problem.add_fluent(termed, default_initial_value=False)
        
        problem.add_action(move_index)
        problem.add_action(term)

        objects = []
        for obj in _input.split(' '):
            objects.append(unified_planning.model.Object(obj, Excomm))

        obj0 = objects[0]
        problem.set_initial_value(index(obj0), True)
        problem.add_goal(termed(obj0))
        problem.add_object(obj0)
        for i in range(1, len(objects)):
            problem.add_object(objects[i])
            problem.set_initial_value(after(objects[i], obj0), True)
            obj0 = objects[i]
            problem.add_goal(termed(objects[i]))
            
        with OneshotPlanner(problem_kind=problem.kind) as planner:
            result = planner.solve(problem)
            if result.status in unified_planning.engines.results.POSITIVE_OUTCOMES:
                print(f"{planner.name} found this plan: {result.plan}")
            else:
                print("No plan found.")
        
        self.problem = problem
        self.solution = result.plan
        self.objects = objects
class Builder:
    def __init__(self):
        self.problem = None
        self.solution = None
        
    def incorporate(self, communicator):
        problem = communicator.problem.clone()
        objects = communicator.objects
        
        Excomm = problem.user_type('Excomm')
        
        termed = problem.fluent('termed')
        index = problem.fluent('index')
        for obj in objects:
            problem.set_initial_value(termed(obj), True) # mock executing of terming
            
        ad = unified_planning.model.Fluent('ad', x=Excomm, target=Excomm)
        problem.add_fluent(ad, default_initial_value=False)    
        problem.set_initial_value(ad(problem.object('BWAHHHH'), problem.object('Save-Babies')), True)
        problem.set_initial_value(ad(problem.object('state-baby-save'), problem.object('Save-Babies')), True)
        problem.set_initial_value(index(objects[0]), True)
        
        rooted = unified_planning.model.Fluent('rooted', x=Excomm)
        
        merge = unified_planning.model.InstantaneousAction('merge', x=Excomm, target=Excomm)
        x = merge.parameter('x')
        target = merge.parameter('target')
        merge.add_precondition(ad(x, target))
        merge.add_precondition(termed(x))
        merge.add_precondition(termed(target))
        merge.add_effect(rooted(x), True)
        merge.add_effect(rooted(target), True)
        
        problem.add_fluent(rooted, default_initial_value=False)
        problem.add_action(merge)    
        
        problem.add_goal(rooted(problem.object('BWAHHHH')))
        problem.add_goal(rooted(problem.object('state-baby-save')))

        
        with OneshotPlanner(problem_kind=problem.kind) as planner:
            result = planner.solve(problem)
            if result.status in unified_planning.engines.results.POSITIVE_OUTCOMES:
                print(f"{planner.name} found this plan: {result.plan}")
            else:
                print("No plan found.")
        self.problem = problem
        self.solution = result.plan
    
if __name__ == "__main__":
    c = Communicator()
    c.input(sys.argv[1])
    
    # Execute terming (of chunks)
    b = Builder()
    b.incorporate(c)
    

    
