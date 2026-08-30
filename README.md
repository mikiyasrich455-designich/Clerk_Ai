Live Hosted on https://clerkagentv1.vercel.app/
  
  **LIVE COMMERCE RESEARCH AGENT**
  
  

## 🛒 The Problem: Product Noise
Online shopping is broken. Finding the right product requires opening twenty tabs, dodging sponsored junk, reading questionable reviews, and mentally tracking prices across different sites. It’s a manual, exhausting research process that hasn't changed in a decade.

## 🚀 The Solution: Clerk
**Clerk** is an autonomous shopping agent that does the tab-juggling for you. 

Built for the 24-hour Agentic Hackathon, Clerk doesn't just return a list of links. You give it a prompt (e.g., *"comfortable running shoes under $80"*), and it autonomously searches live sources, compares the evidence, checks constraints (like budget), and returns a clear, synthesized buying brief. 

No more tabs. Just the right pick.

---

## 🧠 How It Works: The Agentic Loop

Clerk isn't a standard chatbot; it runs a purpose-built agentic pipeline to ensure speed and accuracy without hallucinations:

1. **Understand:** Deterministically parses the user's natural language to extract hard constraints (e.g., extracting `$80` via regex to form a strict budget).
2. **Plan:** Formulates parallel search strategies (a broad category search + a constraint-specific search).
3. **Act:** Executes parallel, real-time calls to Google Shopping and Organic Web Search to gather live prices, images, and review snippets.
4. **Observe & Decide:** Evaluates the gathered evidence. *Did we find anything under budget? Are the results relevant?* 
5. **Act Again (Self-Correction):** If the results fail the criteria (e.g., all products found are over budget), the agent autonomously refines its query and triggers a fallback search.
6. **Verify:** Scores candidates against the user's initial constraints and ranks the top 6.
7. **Synthesize:** Passes the verified, structured evidence to the LLM to write a concise, persuasive buying brief based *strictly* on the live data—no hallucinations.

---

## ⚡ Tech Stack

Clerk is built to be blisteringly fast, relying on serverless functions and a zero-build frontend.

- **Frontend:** Vanilla HTML/CSS/JS (Clean, instant load, no heavy frameworks).
- **Backend:** Python + FastAPI.
- **LLM Engine:** [Groq](https://groq.com/) running Qwen models for near-instant inference.
- **Live Data:** [SerpAPI](https://serpapi.com/) for real-time Google Shopping and organic search data.
- **Deployment:** Vercel (Serverless Edge API).

---

## 🛠️ Local Development

Want to run Clerk locally? You'll need API keys for Groq and SerpAPI.

### 1. Clone the repository
```bash
git clone https://github.com/mikiyasrich455-designich/clerkagentv1.git
cd clerkagentv1
```

### 2. Set Environment Variables
Create a `.env` file in the root directory (or just export them in your terminal):
```env
GROQ_API_KEY=your_groq_api_key_here
SERP_API_KEY=your_serp_api_key_here
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn requests python-dotenv
```

### 4. Run the Backend
```bash
python -m uvicorn api.index:app --port 8010 --reload
```

### 5. Launch the UI
Simply open `index.html` in your favorite web browser (or use a live server like `python -m http.server 8080`).

---

## 🏆 Hackathon Context
This project was built entirely within a 24-hour hackathon window, focusing on the **Agentic Track**. The goal was to move beyond conversational AI and build a system that can *act* on the web, retrieve live data, make decisions, and format the output into a highly polished consumer UI.
