import agentboard as ab
from agentboard.utils import function_to_schema

def run_healthcare_agent():
    """
        agentboard --logdir=./log
        # agentboard --logdir=./log --logfile=xxx.log --static=./static --port=5000
    """

    agent_name = "agent_checking_calories"
    
    with ab.summary.FileWriter(logdir="./log", static="./static") as writer:

        ab.summary.agent_loop(name="START", data="This is start stage of %s", agent_name = agent_name, process_id="START", workflow_type="start", duration = 0)

        ## required parameters 
        user_prompt = "Hi, How many calories are there in a Starbucks Frappuccino?"
        ab.summary.agent_loop(name="PROMPT", data={"prompt": user_prompt}, agent_name = agent_name, process_id="QUERY UNDERSTANDING", duration = 0)

        qu_result = {"food": "starbucks frappuccino"}
        ab.summary.agent_loop(name="QU OUTPUT", data=qu_result, agent_name = agent_name, process_id="QUERY UNDERSTANDING", duration = 0)

        ## QU Code of NLP Models, Calling LLM wiht tools [request_other_parameters(), order_coffee()]
        ## Code Ingored
        def request_calories_from_web():
            return
        def request_other_parameters():
            return

        tools = [request_calories_from_web, request_other_parameters]
        ab.summary.agent_loop(name="LLM Function INPUT", data={"tools": [function_to_schema(tool) for tool in tools] }, agent_name=agent_name, process_id="LLM Function Calls 1", duration = 0)
        ab.summary.agent_loop(name="LLM Function OUTPUT", data={"tools": [function_to_schema(request_other_parameters)] }, agent_name=agent_name, process_id="LLM Function Calls 1", duration = 0)

        ## DECISON
        ab.summary.agent_loop(name="IF Make New Request", data={"tools": [ function_to_schema(request_other_parameters) ]}, agent_name = agent_name, process_id="NEW REQUEST", workflow_type="decision",duration = 0)

        ## Make New Request
        tool_name = "request_other_parameters"
        tool_params = {"args": "cup_size"}
        response_text = "Is there any particular cup size of calories you want to know?"

        ab.summary.agent_loop(name="OPTION 1", data={"name": tool_name, "params": tool_params}, agent_name = agent_name, process_id="OPTIONS", duration = 0)
        ab.summary.agent_loop(name="OPTION 2", data={}, agent_name = agent_name, process_id="OPTIONS", duration = 0)

        user_input = "What about a Grande size Frappuccino without cream. How many calories?"
        ab.summary.agent_loop(name="USER INPUT", data=user_input, agent_name=agent_name, process_id="USER", duration = 0)

        ### Calling LLM Tool user
        params =  {"food": "starbucks frappuccino", "cup_size": "grande"}
        ab.summary.agent_loop(name="LLM Function INPUT", data=params, agent_name=agent_name, process_id="LLM Function Calls 2", duration = 0)
        ab.summary.agent_loop(name="LLM Function OUTPUT", data={"name": request_calories_from_web.__name__, "params": params}, agent_name = agent_name, process_id="LLM Function Calls 2", duration = 0)


        ### Final Response generated by ChatGPT
        final_response = """ 
            Grande (16 oz) Starbucks Frappuccino without whipped cream, the calorie count will depend on the flavor and milk choice. Here's a general breakdown for popular options made with 2% milk
            Coffee-Based Frappuccinos (Grande, no whipped cream)
            Coffee Frappuccino: ~230 calories
            Caramel Frappuccino: ~270 calories
            Mocha Frappuccino: ~300 calories
        """
        ab.summary.agent_loop(name="RESPONSE", data={"message": final_response}, agent_name = agent_name, process_id="RESPONSE", duration = 0)

        ## END
        ab.summary.agent_loop(name="END", data="This is End Stage of Agent Ordering Coffee Loop", agent_name = agent_name, process_id="END", workflow_type="start", duration = 0)

if __name__ == "__main__":
    run_healthcare_agent()
