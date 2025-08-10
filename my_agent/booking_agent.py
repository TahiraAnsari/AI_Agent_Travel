from agents import Agent
from travel_tools import get_flight, suggest_hotels

booking_agent = Agent(
    name="BookingAgent",
    instructions="""
    You are a professional travel booking assistant. 
    When given a destination, provide:
    - Available flight details
    - 3 top hotel options with prices
    Always format information in a neat bullet list.
    """,
    tools=[get_flight, suggest_hotels],
)
