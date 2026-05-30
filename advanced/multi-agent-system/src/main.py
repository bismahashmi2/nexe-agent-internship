from orchestrator import Orchestrator

orch = Orchestrator()

while True:
    q = input("Enter task: ")

    if q == "exit":
        break

    print(orch.run(q))