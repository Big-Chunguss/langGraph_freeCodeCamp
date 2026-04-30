# langGraph_freeCodeCamp

This repository documents my hands-on work from a LangGraph bootcamp. I used a series of notebooks and small Python agents to learn how to model workflows as graphs, manage state between nodes, route execution conditionally, and connect LLMs to tools, memory, and retrieval.
Link to the video: https://www.youtube.com/watch?v=jGg_1h0qzaM

## What I built during the bootcamp

### Core LangGraph exercises

- `hello_world.ipynb`: built a minimal one-node graph that updates and returns a message.
- `sequential_agent.ipynb`: created a sequential workflow with multiple nodes connected by edges.
- `multiple_inputs.ipynb`: passed multiple values through graph state and processed them in a node.
- `looping.ipynb`: added a loop with conditional edges and a counter to control repeated execution.
- `conditional_agent.ipynb`: routed execution to different nodes based on an operation in the state.
- `ex_graph3.ipynb`: extended a sequential graph to combine multiple pieces of user information into one result.
- `ex_graph4.ipynb`: chained multiple routing steps to handle more than one decision in the same graph.
- `ex_graph5.ipynb`: built a small number-guessing game with setup, guessing, hinting, and loop control.

### Agent projects

- `agent/agent_bot.py`: created a basic chatbot using LangGraph and Mistral.
- `agent/memory_agent.py`: added conversation history so the bot could keep context across turns and save logs.
- `agent/ReAct.py`: built a tool-using agent that can decide when to call arithmetic tools.
- `agent/Drafter.py`: created a document drafting assistant with update and save tools.
- `agent/RAG_Agent.py`: built a retrieval-augmented generation agent using PDF loading, chunking, embeddings, and Chroma vector storage.

## Skills covered

- Graph-based workflow design with `StateGraph`
- State management with `TypedDict`
- Entry points, finish points, and explicit edges
- Conditional routing and looping
- Tool calling with LangGraph and LangChain tools
- Multi-turn memory and conversation logging
- Retrieval pipelines with embeddings, vector stores, and document search
- LLM integration with Mistral models and environment-based configuration

## Outcome

By the end of this bootcamp, I had moved from simple LangGraph examples to more complete agent patterns such as tool use, memory, drafting workflows, and RAG. This repo serves as both my learning log and a set of working reference examples for future LangGraph projects.
