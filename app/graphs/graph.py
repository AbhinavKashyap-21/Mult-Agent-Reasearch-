from langgraph.graph import StateGraph, START, END

from .nodes import validate_question, route_question, extract_claims
from .state import ResearchState

graph = StateGraph(ResearchState)

graph.add_node("validate_question", validate_question)
graph.add_node("extract_claims", extract_claims)

graph.add_edge(START, "validate_question")

graph.add_conditional_edges(
    "validate_question",
    route_question,
    {
        "extract_claims": "extract_claims",
        "invalid": END
    }
)

graph.add_edge("extract_claims", END)

graph = graph.compile()

initial_state = {
    "user_text": ""
}

result = graph.invoke(initial_state)

print(result)