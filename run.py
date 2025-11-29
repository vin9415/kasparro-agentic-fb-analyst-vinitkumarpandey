from src.orchestrator.orchestrator import Orchestrator
import sys
def main():
    orch = Orchestrator()
    # Replace the task description with whatever you want the system to do
    user_task = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Generate a marketing performance summary"


    result = orch.run(user_task)
    print("\n=== FINAL RESULT ===")
    for k, v in result.items():
        print(f"{k}:\n{v}\n")

if __name__ == "__main__":
    main()
