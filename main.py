from code.agent import Agent

if __name__ == "__main__":
    agent = Agent()
    while not agent.quit:
        agent.ask_action()
