from message_bus import MessageBus
from agents.retriever_agent import RetrieverAgent
from agents.writer_agent import WriterAgent


class Orchestrator:

    def __init__(self):
        self.bus = MessageBus()
        self.retriever = RetrieverAgent()
        self.writer = WriterAgent()

    def run(self, user_input):

        msg = {
            "from": "user",
            "to": "retriever",
            "data": user_input
        }

        context = self.bus.send(self.retriever, msg)

        msg2 = {
            "from": "orchestrator",
            "to": "writer",
            "data": context
        }

        result = self.bus.send(self.writer, msg2)

        return result