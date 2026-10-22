import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

from graph import bug_analyzer_app

def main():
    print("--- AI Bug Report Analyzer (LangGraph + Gemini) ---")
    
    # Sample bug description or take input from user
    user_input = input("\nEnter bug description (or press Enter for default sample):\n> ").strip()
    
    if not user_input:
        user_input = (
            "When users try to check out on the web app using PayPal, the payment modal opens "
            "and spins indefinitely after hitting confirm. The console throws a 504 Gateway Timeout "
            "from the /api/v1/payments/paypal endpoint, and money isn't deducted, but the cart item count resets."
        )
        print(f"\n[Using Default Sample Description]:\n{user_input}\n")

    initial_state = {
        "raw_description": user_input,
        "title": None,
        "affected_feature": None,
        "issue_summary": None,
        "severity": None,
        "root_causes": None,
        "formatted_report": None
    }

    print("Analyzing bug report across LangGraph pipeline...\n")
    
    # Invoke graph execution
    final_state = bug_analyzer_app.invoke(initial_state)

    # Display final result
    print(final_state["formatted_report"])

if __name__ == "__main__":
    main()