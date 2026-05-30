class WriterAgent:
    def run(self, message):
        return "Final answer based on: " + message["data"]