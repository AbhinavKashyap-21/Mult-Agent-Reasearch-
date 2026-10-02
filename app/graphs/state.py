from typing import TypedDict



class Claim(TypedDict):
    claim: str
    citations: list[str]   

class Paper(TypedDict):
    title: str
    authors: str
    published: str
    abstract: str
    arxiv_id: str
    url: str       
      
class ResearchState(TypedDict):
    user_text: str
    is_valid: bool
    claims: list[Claim]
    papers: list[Paper]
    verification_results: list
    final_answer: str
    

    
