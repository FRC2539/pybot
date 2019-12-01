from .unassignedaxis import UnassignedAxis

def registerAxis(name):
    vars = globals()
    
    if not name in vars:
        vars[name] = UnassignedAxis()
