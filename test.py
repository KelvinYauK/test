from typing import TypedDict
from langgraph.graph import StateGraph, END

# 1) Define shared state
class MyState(TypedDict):
    text: str
    sentiment: str

# 2) Define nodes
def analyze_sentiment(state: MyState) -> MyState:
    text = state["text"].lower()
    if "good" in text or "great" in text or "happy" in text:
        sentiment = "positive"
    elif "bad" in text or "sad" in text or "angry" in text:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    return {**state, "sentiment": sentiment}

def format_output(state: MyState) -> MyState:
    state["text"] = f'Input: "{state["text"]}" -> Sentiment: {state["sentiment"]}'
    return state

# 3) Build graph
graph = StateGraph(MyState)
graph.add_node("analyze", analyze_sentiment)
graph.add_node("format", format_output)

graph.set_entry_point("analyze")
graph.add_edge("analyze", "format")
graph.add_edge("format", END)

app = graph.compile()

# 4) Run graph
result = app.invoke({"text": "Today is a good day!", "sentiment": ""})
print(result["text"])