<!-- .slide: class="with-code-bg-dark"-->

# 🦜🕸️ LangGraph

```python[1|3-5|7-29|30-31]
workflow = StateGraph(AgentState)

workflow.add_node("Researcher", research_node)
workflow.add_node("Chart Generator", chart_node)
workflow.add_node("call_tool", tool_node)

workflow.add_conditional_edges(
    "Researcher",
    router,
    {"continue": "Chart Generator", "call_tool": "call_tool", "end": END},
)
workflow.add_conditional_edges(
    "Chart Generator",
    router,
    {"continue": "Researcher", "call_tool": "call_tool", "end": END},
)

workflow.add_conditional_edges(
    "call_tool",
    # Each agent node updates the 'sender' field
    # the tool calling node does not, meaning
    # this edge will route back to the original agent
    # who invoked the tool
    lambda x: x["sender"],
    {
        "Researcher": "Researcher",
        "Chart Generator": "Chart Generator",
    },
)
workflow.set_entry_point("Researcher")
graph = workflow.compile()
```

Notes:
Décrire d'autre possibilités :
* Agent_supervisor
* agents hierarchiques

##==##

<!-- .slide: class="full-center" -->

# LangSmith

![h-900](./assets/images/langsmith.png)

##==##

<!-- .slide: -->

# LangSmith

* [LangSmith - https://docs.smith.langchain.com/](https://docs.smith.langchain.com/)
<br><br>

* self-managed
![h-100](./assets/images/docker.png)
![h-100](./assets/images/kubernetes.png)
<br><br>

* 3 Offres de pricing
<br><br>

* Gestion des prompts, Monitoring, Tokens
<br><br>

* Evaluation, Etiquette

<!-- .element: class="credits" -->

Notes:
Pricing Dev, Plus, Enterprise

Feature SSO (Enterprise)
