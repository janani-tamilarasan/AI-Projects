# 🤖 AI Customer Support Multi-Agent System

An AI-powered customer support application built using **FastAPI, LangGraph, Gemini, and tool-calling agents**.

The system receives a customer support ticket, uses an **LLM Supervisor** to identify the ticket category, and routes it to the appropriate specialized support agent.

Currently, the **Billing Agent** is implemented as an actual LLM agent with tool calling.

---

DEMO



# 🚀 Features

- Customer support ticket API using FastAPI
- LLM-powered ticket classification
- LangGraph workflow orchestration
- Supervisor Agent for ticket routing
- Specialized support agents
- Billing Agent with Gemini
- Billing Agent tool calling
- Payment lookup tool
- LangGraph conditional routing
- Billing Agent subgraph
- Swagger API documentation
- Modular project structure

---

# 🛠️ Skills / Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| FastAPI | REST API |
| LangGraph | AI workflow orchestration |
| LangChain | LLM and tool integration |
| Google Gemini | LLM / Supervisor / Billing Agent |
| Pydantic | Request and response validation |
| Swagger / OpenAPI | API testing |
| Git / GitHub | Version control |

---

# 🧠 LangGraph Concepts Practiced

This project is mainly designed to understand **LangGraph workflows and multi-agent architecture**.

### Concepts implemented

- StateGraph
- Graph Nodes
- START / END
- Conditional Edges
- LLM Supervisor
- Agent Routing
- Subgraphs
- Tool Calling
- ToolNode
- `bind_tools()`
- Agent State
- Message State
- Agent loops

---

# 🏗️ Architecture

```text
                     Customer
                        │
                        ▼
                  FastAPI API
                        │
                        ▼
               Main LangGraph
                        │
                        ▼
                  Supervisor
                    (Gemini)
                        │
              ┌─────────┼─────────┐
              │         │         │
              ▼         ▼         ▼
           Billing     Order    Technical
            Agent      Agent      Agent
              │
              ▼
       Billing Subgraph
              │
              ▼
            Gemini
              │
        Tool required?
          /       \
        Yes        No
         │          │
         ▼          ▼
   Billing Tool    END
         │
         ▼
    Payment Data
         │
         ▼
       Gemini
         │
         ▼
    Final Response
