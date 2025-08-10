import os
from dotenv import load_dotenv
from agents import Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from my_agent.destination_agent import destination_agent
from my_agent.booking_agent import booking_agent
from my_agent.explore_agent import explore_agent
from my_agent.triage_agent import triage_agent

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

# Apply model to all agents
destination_agent.model = model
booking_agent.model = model
explore_agent.model = model
triage_agent.model = model

config = RunConfig(
    model=model,
    tracing_disabled=True
)

def main():
    print("🌍 AI Travel Designer\n")
    
    while True:
        mood = input("What's your travel mood (type 'quit' to exit): ").strip()
        if mood.lower() == "quit":
            print("Goodbye! Safe travels ✈️")
            break

        # Step 1: Get destination
        result1 = Runner.run_sync(triage_agent, mood, run_config=config)
        dest = result1.final_output.strip()
        print(f"\n🏝 Destination Suggested: {dest}")

        # Step 2: Get booking info
        result2 = Runner.run_sync(booking_agent, dest, run_config=config)
        print(f"\n📅 Booking Info:\n{result2.final_output}")

        # Step 3: Get explore tips
        result3 = Runner.run_sync(explore_agent, dest, run_config=config)
        print(f"\n🗺 Explore Tips:\n{result3.final_output}")
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
