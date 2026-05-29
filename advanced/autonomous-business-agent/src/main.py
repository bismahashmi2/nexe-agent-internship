from autonomous_agent import AutonomousAgent

agent = AutonomousAgent()

print("🔥 Autonomous Business Agent Ready")

print("Type 'exit' to quit\n")

while True:
    user_input = input("\nEnter task: ")

    if user_input.lower() == "exit":
        break

    result = agent.run(user_input)

    print("\n 📌FINAL ANSWER:\n")
    print(result["result"])

    print("\n 📜EXECUTION LOGS:")
    for log in result["logs"]:
        print(log)

    print("\n" + "-"*40)

