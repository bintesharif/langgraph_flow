from langgraph.func import task, entrypoint

@task
def function1() -> str:
    print("Step 1: function1")
    return "text1"

@task
def function2() -> str:
    print("Step 2: function2")
    return "text2"

@task
def function3() -> str:
    print("Step 3: function3")
    return "text3"

@entrypoint()
def simple_flow(input) -> dict:
    output1 = function1().result()
    output2 = function2().result()
    output3 = function3().result()
    return {"output1": output1, "output2": output2, "output3": output3}

def run_simple_flow():
    result = simple_flow.invoke(input="Pakistan")
    print(result)


