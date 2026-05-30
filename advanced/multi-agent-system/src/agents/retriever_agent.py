class RetrieverAgent:
    def run(self, message):
        return "Retrieved context for: " + message["data"]