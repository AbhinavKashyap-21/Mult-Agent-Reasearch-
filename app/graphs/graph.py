from langgraph.graph import StateGraph, START,END
from .nodes import validate_question
from .state import ResearchState

graph = StateGraph(ResearchState)
graph.add_node("validate_question",validate_question)
graph.add_edge(START, "validate_question")
graph.add_edge("validate_question", END)
graph = graph.compile()

graph.invoke({"user_question": [{"is_valid": "user", "content": "hi!"}]})
