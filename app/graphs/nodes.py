from .state import ResearchState

def validate_question(state: ResearchState):
    question =  state["user_text"].strip().lower()
    
    greetings = {"hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"}
    
    if not question:
        return {"is_valid":False}
    
    elif question in greetings:
        return {"is_valid":False}
    else:
        return {"is_valid":True}
    
def route_question(state):
    validate = state["is_valid"]
    if validate == True:
        return "extract_claims"
    else:
        return "invalid"
    
def extract_claims(state):
    text = state["user_text"]
        
            
        
        