import os
from typing import List, Dict, Any 
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from state import BugAnalyzerState

# Initialize Gemini LLM using Gemini 1.5 Flash (fast & effective for analysis)
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.2,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# -------------------------------------------------------------
# Node 1: Bug Analysis
# -------------------------------------------------------------
class BugAnalysisOutput(BaseModel):
    title: str = Field(description="A concise, descriptive bug title")
    affected_feature: str = Field(description="The feature, component, or module affected")
    issue_summary: str = Field(description="A detailed summary of the reported bug")

def analyze_bug_node(state: BugAnalyzerState) -> Dict[str, Any]:
    """Extracts title, affected feature, and issue summary."""
    prompt = (
        "You are an expert QA Engineer. Analyze the following raw bug description and extract "
        "a clear title, the affected feature/component, and a structured summary.\n\n"
        f"Raw Bug Description:\n{state['raw_description']}"
    )
    
    structured_llm = llm.with_structured_output(BugAnalysisOutput)
    result: BugAnalysisOutput = structured_llm.invoke(prompt)
    
    return {
        "title": result.title,
        "affected_feature": result.affected_feature,
        "issue_summary": result.issue_summary
    }

# -------------------------------------------------------------
# Node 2: Severity Detection
# -------------------------------------------------------------
class SeverityOutput(BaseModel):
    severity: str = Field(
        description="Severity level. MUST be one of: Critical, High, Medium, Low"
    )

def detect_severity_node(state: BugAnalyzerState) -> Dict[str, Any]:
    """Classifies severity as Critical, High, Medium, or Low."""
    prompt = (
        "You are a Senior Software Engineer. Determine the severity level of the following bug.\n"
        "Classification categories: Critical (system crash, data loss, security vulnerability), "
        "High (major feature broken, no workaround), Medium (minor feature broken or workaround available), "
        "Low (cosmetic issue, typo, minor UX bug).\n\n"
        f"Title: {state['title']}\n"
        f"Affected Feature: {state['affected_feature']}\n"
        f"Summary: {state['issue_summary']}\n"
        f"Raw Context: {state['raw_description']}"
    )
    
    structured_llm = llm.with_structured_output(SeverityOutput)
    result: SeverityOutput = structured_llm.invoke(prompt)
    
    return {"severity": result.severity}

# -------------------------------------------------------------
# Node 3: Root Cause Suggestion
# -------------------------------------------------------------
class RootCauseOutput(BaseModel):
    root_causes: List[str] = Field(
        description="List of 2 to 4 potential technical root causes for this issue."
    )

def suggest_root_cause_node(state: BugAnalyzerState) -> Dict[str, Any]:
    """Suggests possible root causes for the bug."""
    prompt = (
        "You are a Lead Software Architect. Provide 2 to 4 plausible technical root causes "
        "or code areas to investigate for the following issue:\n\n"
        f"Title: {state['title']}\n"
        f"Affected Feature: {state['affected_feature']}\n"
        f"Issue Summary: {state['issue_summary']}\n"
        f"Severity: {state['severity']}"
    )
    
    structured_llm = llm.with_structured_output(RootCauseOutput)
    result: RootCauseOutput = structured_llm.invoke(prompt)
    
    return {"root_causes": result.root_causes}

# -------------------------------------------------------------
# Node 4: Format Report
# -------------------------------------------------------------
def format_report_node(state: BugAnalyzerState) -> Dict[str, Any]:
    """Formats the collected details into a clean, readable Markdown bug report."""
    causes_formatted = "\n".join([f"- {cause}" for cause in state.get('root_causes', [])])
    
    report = f"""
==================================================
           🐞 STRUCTURED BUG REPORT 🐞
==================================================

📌 TITLE:
{state.get('title')}

🎯 AFFECTED FEATURE / COMPONENT:
{state.get('affected_feature')}

🚨 SEVERITY LEVEL:
{state.get('severity')}

📝 ISSUE SUMMARY:
{state.get('issue_summary')}

🔍 POTENTIAL ROOT CAUSES & INVESTIGATION POINTS:
{causes_formatted}

==================================================
    """.strip()
    
    return {"formatted_report": report}