from agents import Agent
from .destination_agent import destination_agent
from .booking_agent import booking_agent
from .explore_agent import explore_agent

triage_agent = Agent(
    name="TriageAgent",
    instructions="""
    Your job is to decide which agent should handle the user's request:
    - If they want to choose where to go → destination_agent
    - If they want flights/hotels → booking_agent
    - If they want activities/food → explore_agent
    """,
    handoffs=[destination_agent, booking_agent, explore_agent],
)
