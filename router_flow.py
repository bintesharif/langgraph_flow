from langgraph.func import task, entrypoint, route
import random


@task
def function1():
    # Randomly select a topic from the list
    topic = random.choice(["tech", "health", "other"])
    return topic


@route(function1)
def function2(topic: str):
    # Route the topic to the correct category
    if topic == "tech":
        return "tech"
    elif topic == "health":
        return "health"
    else:
        return "other"


@listen("tech")
def tech_handler(topic: str):
    # Handle the "tech" topic
    print("Step 3 from tech_handler:", topic)


@listen("health")
def health_handler(topic: str):
    # Handle the "health" topic
    print("Step 4 from health_handler:", topic)


@listen("other")
def other_handler(topic: str):
    # Handle the "other" topic
    print("Step 5 from other_handler:", topic)


@entrypoint()
def main():
    # Start the LangGraph flow
    function1()
    function2(function1())
