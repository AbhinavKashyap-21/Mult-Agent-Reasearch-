from typing import TypedDict



class Claim(TypedDict):
    claim: str
    citations: str    
    
class ResearchState(TypedDict):
    user_text: str
    is_valid: bool
    claims: list[Claim]
    papers: list
    verification_results: list
    final_answer: str
    
