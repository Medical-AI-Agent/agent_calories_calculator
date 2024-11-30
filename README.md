# AI Healthcare Agent Workflow Visualization Using Agentboard: AI Agent Calories Calculator

AI Agents act as the role of health coaches nutritionists can
- provide advice on nutrition and calories, such as Dietitians, Health coaches (helping them set nutrition goals and make sustainable behavior changes), Personal trainers (They develop training and nutrition programs and can work in gyms), Sports nutritionists, etc.
- Nutrition
- Weight management
- Chronic disease or illness management

**agent calories calculator** <br>
Here is the workflow of and AI agent who help check the calories of a Starbucks Frappuccino

```

User: Hi, How many calories are there in a Starbucks Frappuccino?

Assistant: The calorie content of a Starbucks Frappuccino varies widely depending on the size, flavor, type of milk, and whether whipped cream or additional toppings are included. 

**Coffee-Based Frappuccinos**  
Coffee Frappuccino (Tall, 12 oz): About 160 calories
Caramel Frappuccino (Tall, 12 oz): About 260 calories
Mocha Frappuccino (Tall, 12 oz): About 280 calories

**Crème-Based Frappuccinos** 
Vanilla Bean Crème Frappuccino (Tall, 12 oz): About 280 calories
Strawberry Crème Frappuccino (Tall, 12 oz): About 250 calories
Double Chocolaty Chip Crème Frappuccino (Tall, 12 oz): About 290 calories

Is there any particular cup size of calories you want to know?

User: What about a Grande size Frappuccino without cream. How many calories?

Assistant:
Grande (16 oz) Starbucks Frappuccino without whipped cream, the calorie count will depend on the flavor and milk choice. Here's a general breakdown for popular options made with 2% milk

Coffee-Based Frappuccinos (Grande, no whipped cream)
Coffee Frappuccino: ~230 calories
Caramel Frappuccino: ~270 calories
Mocha Frappuccino: ~300 calories

```

And I used agent loop visualization tool [agentboard](https://ai-hub-admin.github.io/agentboard/) to help log the agent loop and visualize it. The complete agent loop goes like this: 

```
## User request starts -> Query Understand -> Calling LLM tool use -> Request for Clarification -> User Input -> Revise Response

```

To visualize the coffee ordering AI agent running loop for quick debugging. 


Sample Usage for a Healthcare AI Agent of Calories Calculating

```

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


```

I wrapped up the complete code of workflow of an coffee ordering agent in "run_healthcare_agent_visualization.py"



To install and start agentboard to visualize the workflow

```
    pip install agentboard

    agentboard --logdir=./log
```


## Agents Related Pipeline Workflow and Document
### AI Services Reviews and Ratings <br>
##### AI Agent Search Engine
[AI Agent Search: Find AI Agent and Apps Search Engine](http://www.deepnlp.org/search/agent) <br>
##### AI Agent
[Microsoft AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-microsoft-ai-agent) <br>
[Claude AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-claude-ai-agent) <br>
[OpenAI AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-openai-ai-agent) <br>
[AgentGPT AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-agentgpt) <br>
[Saleforce AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-salesforce-ai-agent) <br>
[Google AI Agents Reviews](http://www.deepnlp.org/store/pub/pub-google-ai-agent) <br>
[Google AI Agents Space](http://www.deepnlp.org/store/ai-agent/ai-agent/pub-google-ai-agent/google-ai-agents-space-review) <br>
##### Chatbot
[OpenAI o1 Reviews](http://www.deepnlp.org/store/pub/pub-openai-o1) <br>
[ChatGPT User Reviews](http://www.deepnlp.org/store/pub/pub-chatgpt-openai) <br>
[Gemini User Reviews](http://www.deepnlp.org/store/pub/pub-gemini-google) <br>
[Perplexity User Reviews](http://www.deepnlp.org/store/pub/pub-perplexity) <br>
[Claude User Reviews](http://www.deepnlp.org/store/pub/pub-claude-anthropic) <br>
[Qwen AI Reviews](http://www.deepnlp.org/store/pub/pub-qwen-alibaba) <br>
[Doubao Reviews](http://www.deepnlp.org/store/pub/pub-doubao-douyin) <br>
[ChatGPT Strawberry](http://www.deepnlp.org/store/pub/pub-chatgpt-strawberry) <br>
[Zhipu AI Reviews](http://www.deepnlp.org/store/pub/pub-zhipu-ai) <br>
##### AI Image Generation
[Midjourney User Reviews](http://www.deepnlp.org/store/pub/pub-midjourney) <br>
[Stable Diffusion User Reviews](http://www.deepnlp.org/store/pub/pub-stable-diffusion) <br>
[Runway User Reviews](http://www.deepnlp.org/store/pub/pub-runway) <br>
[GPT-5 Forecast](http://www.deepnlp.org/store/pub/pub-gpt-5) <br>
[Flux AI Reviews](http://www.deepnlp.org/store/pub/pub-flux-1-black-forest-lab) <br>
[Canva User Reviews](http://www.deepnlp.org/store/pub/pub-canva) <br>
##### AI Video Generation
[Luma AI](http://www.deepnlp.org/store/pub/pub-luma-ai) <br>
[Pika AI Reviews](http://www.deepnlp.org/store/pub/pub-pika) <br>
[Runway AI Reviews](http://www.deepnlp.org/store/pub/pub-runway) <br>
[Kling AI Reviews](http://www.deepnlp.org/store/pub/pub-kling-kwai) <br>
[Dreamina AI Reviews](http://www.deepnlp.org/store/pub/pub-dreamina-douyin) <br>
##### AI Education
[Coursera Reviews](http://www.deepnlp.org/store/pub/pub-coursera) <br>
[Udacity Reviews](http://www.deepnlp.org/store/pub/pub-udacity) <br>
[Grammarly Reviews](http://www.deepnlp.org/store/pub/pub-grammarly) <br>
##### Robotics
[Tesla Cybercab Robotaxi](http://www.deepnlp.org/store/pub/pub-tesla-cybercab) <br>
[Tesla Optimus](http://www.deepnlp.org/store/pub/pub-tesla-optimus) <br>
[Figure AI](http://www.deepnlp.org/store/pub/pub-figure-ai) <br>
[Unitree Robotics Reviews](http://www.deepnlp.org/store/pub/pub-unitree-robotics) <br>
[Waymo User Reviews](http://www.deepnlp.org/store/pub/pub-waymo-google) <br>
[ANYbotics Reviews](http://www.deepnlp.org/store/pub/pub-anybotics) <br>
[Boston Dynamics](http://www.deepnlp.org/store/pub/pub-boston-dynamic) <br>
##### AI Agent Tools
[DeepNLP AI Tools](http://www.deepnlp.org/store/pub/pub-deepnlp-ai) <br>
[Equation Search and Documentation](http://www.deepnlp.org/search/equation/) <br>
##### AI Widgets
[Apple Glasses](http://www.deepnlp.org/store/pub/pub-apple-glasses) <br>
[Meta Glasses](http://www.deepnlp.org/store/pub/pub-meta-glasses) <br>
[Apple AR VR Headset](http://www.deepnlp.org/store/pub/pub-apple-ar-vr-headset) <br>
[Google Glass](http://www.deepnlp.org/store/pub/pub-google-glass) <br>
[Meta VR Headset](http://www.deepnlp.org/store/pub/pub-meta-vr-headset) <br>
[Google AR VR Headsets](http://www.deepnlp.org/store/pub/pub-google-ar-vr-headset) <br>
##### Social
[Character AI](http://www.deepnlp.org/store/pub/pub-character-ai) <br>
##### Self-Driving
[BYD Seal](http://www.deepnlp.org/store/pub/pub-byd-seal) <br>
[Tesla Model 3](http://www.deepnlp.org/store/pub/pub-tesla-model-3) <br>
[BMW i4](http://www.deepnlp.org/store/pub/pub-bmw-i4) <br>
[Baidu Apollo Reviews](http://www.deepnlp.org/store/pub/pub-baidu-apollo) <br>
[Hyundai IONIQ 6](http://www.deepnlp.org/store/pub/pub-hyundai-ioniq-6) <br>

### Related Blogs <br>
[AgentBoard AI Agent Visualization Toolkit](http://www.deepnlp.org/blog/agentboard-ai-agent-visualization-toolkit-agent-loop-workflow) <br>
[DeepNLP AI Agents Designing Guidelines](http://www.deepnlp.org/blog?category=agent) <br>
[Introduction to multimodal generative models](http://www.deepnlp.org/blog/introduction-to-multimodal-generative-models) <br>
[Generative AI Search Engine Optimization](http://www.deepnlp.org/blog/generative-ai-search-engine-optimization-how-to-improve-your-content) <br>
[AI Image Generator User Reviews](http://www.deepnlp.org/store/image-generator) <br>
[AI Video Generator User Reviews](http://www.deepnlp.org/store/video-generator) <br>
[AI Chatbot & Assistant Reviews](http://www.deepnlp.org/store/chatbot-assistant) <br>
[Best AI Tools User Reviews](http://www.deepnlp.org/store/pub/) <br>
[AI Boyfriend User Reviews](http://www.deepnlp.org/store/chatbot-assistant/ai-boyfriend) <br>
[AI Girlfriend User Reviews](http://www.deepnlp.org/store/chatbot-assistant/ai-girlfriend) <br>
[AI Agent User Reviews](http://www.deepnlp.org/store/ai-agent) <br>


