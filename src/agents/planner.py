# src/agents/planner.py
from typing import List

class PlannerAgent:
    """
    Create a simple ordered plan of steps from a natural language task.
    """

    def __init__(self):
        pass

    def create_plan(self, task: str) -> List[str]:
        # ✅ Make everything lowercase once
        task_lower = task.lower()

        # ✅ Detect if this is a creative-only task
        creative_keywords = [
    "write", "ad", "copy", "creative", "headline", "caption",
    "facebook ad", "instagram ad",
    "black friday", "cyber monday", "shoes", "footwear",
    "discount", "offer", "deal", "sale", "promo"
]


        is_creative = any(kw in task_lower for kw in creative_keywords)

        # ✅ For creative-only tasks: no data/insights needed
        if is_creative:
            # Orchestrator will treat this specially
            return ["generate_creatives"]

        # ✅ Default: analytics-style plan (your original logic)
        plan = [
            "1. Understand task and define subgoals",
            "2. Collect and load relevant data",
            "3. Clean and preprocess data",
            "4. Analyze data and compute metrics",
            "5. Generate insights and recommendations",
            "6. Create final deliverable (summary/report)",
        ]

        # Keep your special case for sales
        if "sales" in task_lower:
            plan.insert(3, "3b. Segment sales by product, time and region")

        return plan
