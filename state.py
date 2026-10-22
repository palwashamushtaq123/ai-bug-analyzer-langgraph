from typing import TypedDict, Optional, List, Dict, Any

class BugAnalyzerState(TypedDict):
    """
    State object representing the data flow across the graph nodes.
    """
    raw_description: str
    title: Optional[str]
    affected_feature: Optional[str]
    issue_summary: Optional[str]
    severity: Optional[str]
    root_causes: Optional[List[str]]
    formatted_report: Optional[str]