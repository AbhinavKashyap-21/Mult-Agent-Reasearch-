from .state import ResearchState

def validate_question(state: ResearchState):
    question =  state["user_question"].strip().lower()
    
    greetings = {"hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"}
    
    if not question:
        return {"is_valid":False}
    
    elif question in greetings:
        return {"is_valid":False}
    else:
        return {"is_valid":True}
        
        