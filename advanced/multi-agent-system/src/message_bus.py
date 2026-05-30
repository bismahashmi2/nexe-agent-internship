class MessageBus:

    def send(self, agent, message):
        return agent.run(message)