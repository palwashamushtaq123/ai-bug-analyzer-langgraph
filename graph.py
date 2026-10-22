from langgraph.graph import StateGraph, END
from state import BugAnalyzerState
from nodes import (
    analyze_bug_node,
    detect_severity_node,
    suggest_root_cause_node,
    format_report_node
)

def build_bug_analyzer_graph():
    """
    Constructs the LangGraph pipeline:
    User Input -> Node 1 -> Node 2 -> Node 3 -> Node 4 -> END
    """
    workflow = StateGraph(BugAnalyzerState)

    # Add Nodes
    workflow.add_node("bug_analysis", analyze_bug_node)
    workflow.add_node("severity_detection", detect_severity_node)
    workflow.add_node("root_cause_suggestion", suggest_root_cause_node)
    workflow.add_node("format_report", format_report_node)

    # Define Linear Workflow Edges
    workflow.set_entry_point("bug_analysis")
    workflow.add_edge("bug_analysis", "severity_detection")
    workflow.add_edge("severity_detection", "root_cause_suggestion")
    workflow.add_edge("root_cause_suggestion", "format_report")
    workflow.add_edge("format_report", END)

    # Compile Graph
    return workflow.compile()

# Instantiated graph ready to invoke
bug_analyzer_app = build_bug_analyzer_graph()