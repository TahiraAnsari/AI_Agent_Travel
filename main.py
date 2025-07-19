import os
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel
)
from agents.run import RunConfig
from travel_tools import get_flight, suggest_hotels

gemini_key = "AIzaSyAdxJObQdZ-qoDS35s9d3nyf7WwvPDd3e0"

load_dotenv()
client = AsyncOpenAI(
    api_key=gemini_key, 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)
config = RunConfig(
    model=model,
    tracing_disabled=True
)

destination_agent = Agent(
    name="DestinationAgent",
    instructions="You recommend travel destination based on user's mood.",
    model=model
)

booking_agent = Agent(
    name="BookingAgent",
    instructions="You give flight  and hotel info using tools.",
    model=model,
    tools=[get_flight,suggest_hotels]
)

explore_agent = Agent(
    name="ExploreAgent",
    instructions="You suggest food and places to explore in the destination.",
    model=model
)

def main():
    print("\U0001F30D AI Travel Designer\n")
    mood = input("What's your travel mood(relaxing/adventure/etc)")

    result1 = Runner.run_sync(destination_agent,mood,run_config=config)
    dest = result1.final_output.strip()
    print("\nDestination Suggested",dest)

    result2 = Runner.run_sync(booking_agent,dest,run_config=config)
    print("\nBooking Info:",result2.final_output)

    result3 = Runner.run_sync(explore_agent,dest,run_config=config)
    print("\nExplore Tips:",result2.final_output)
    

if __name__ == "__main__":
    main()
