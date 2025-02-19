from langgraph.func import task, entrypoint
from dotenv import load_dotenv, find_dotenv
_:bool = load_dotenv(find_dotenv())
from litellm import completion


@task
def function1():
    response = completion(
        model="gemini/gemini-1.5-flash",  
        messages=[
            {"role": "user", "content": "generate any random city name from Pakistan only"}
        ]    
    ) 
    city_name = response["choices"][0]["message"]["content"]
    print("step 1 genrate city name",city_name)
    return city_name  



@task
def function2(city_name):
    response = completion(
        model="gemini/gemini-1.5-flash",  
        messages=[
            {"role": "user", "content": ""f"write some fun fact about{city_name}city?output must be in the  markdown format"}
        ]    
    ) 
    fun_fact = response["choices"][0]["message"]["content"]
    print("step 2 genrate fun_fact")
    return fun_fact

@task
def function3(fun_fact):
    with open("fun_fact.md","w") as f:
            f.write(fun_fact)
    print("step 3 save file")        

@entrypoint()
def run_flow(input={}):
    city = function1().result()
    fun_fact = function2(city).result()
    function3(fun_fact)
    


def run_promte_chaining_flow()->None:
    run_flow.invoke({})

     

        
