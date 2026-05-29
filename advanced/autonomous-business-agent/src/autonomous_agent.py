from retrieve import query_engine
from datetime import datetime

from agents import Runner
from rag_agent import rag_agent


class AutonomousAgent:

    def __init__(self):
        self.logs = []

    def log(self, msg):

        t = datetime.now().strftime("%H:%M:%S")

        entry = f"[{t}] {msg}"

        self.logs.append(entry)

        print(entry)

    def plan(self, user_input):

        self.log("Creating plan...")

        plan = [
            "Understand question",
            "Retrieve relevant context from vector DB",
            "Generate final answer"
        ]

        self.log(f"Plan: {plan}")

        return plan

    def retrieve(self, user_input):

        self.log("Retrieving from RAG system...")

        context = query_engine(user_input)

        self.log("Context retrieved")

        return context

    def generate_answer(self, user_input, context):

        self.log("Generating AI response...")
        
        context_text = "\n\n".join(
        [f"[Chunk {i+1}]\n{c}" for i, c in enumerate(context)]
        )
        final_prompt = f"""
        Context:
        {context_text}

        Question:
        {user_input}
        """

        response = Runner.run_sync(
            starting_agent=rag_agent,
            input=final_prompt
        )

        self.log("Answer generated")

        return response.final_output

    def run(self, user_input):

        self.logs = []

        self.log("Agent started")

        plan = self.plan(user_input)

        context = self.retrieve(user_input)

        final_answer = self.generate_answer(
            user_input,
            context
        )

        self.log("Agent finished")

        return {
            "plan": plan,
            "result": final_answer,
            "logs": self.logs
        }