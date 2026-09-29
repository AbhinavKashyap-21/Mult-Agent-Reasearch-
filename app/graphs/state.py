from typing import TypedDict

class ResearchState(TypedDict):
    user_question: str
    is_valid: bool
    research_plan: list
    research_findings: list
    sources: list
    verification_results: list
    critic_feedback: str
    final_answer: str