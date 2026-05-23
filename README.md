# 🤖 AI Job Agent — Automated Job Search & Resume Tailor

An agentic AI pipeline that searches for real job openings, scrapes the full job description, and automatically rewrites your resume to match — all in under 60 lines of Python.

Built with **Gemini 2.5 Flash** + **Tinyfish API**.

---

## 📸 Demo

![Agent searching for jobs and tailoring resume](demo.png)

> The agent searches live job listings, reads the full posting, and returns a tailored resume with the summary, skills, and project bullets rewritten to match the JD.

---

## ⚙️ How It Works

```
Your Role Input
      │
      ▼
Tinyfish Search API ──► finds live job listings
      │
      ▼
Tinyfish Fetch API ──► scrapes full job description
      │
      ▼
Gemini 2.5 Flash ──► reads JD + your master resume
      │
      ▼
Tailored Resume (saved to /output)
```

Gemini uses **native function calling** to orchestrate the tools — no LangChain or complex framework needed.

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/Ayush-2703/ai-job-agent.git
cd ai-job-agent
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API keys
```bash
cp .env.example .env
```
Then open `.env` and add your real keys:
```
GEMINI_API_KEY=your_key_here
TINYFISH_API_KEY=your_key_here
```

| Key | Get it from |
|-----|-------------|
| `GEMINI_API_KEY` | [Google AI Studio](https://aistudio.google.com/app/apikey) |
| `TINYFISH_API_KEY` | [tinyfish.ai](https://tinyfish.ai) |

### 5. Add your resume
```bash
cp master_resume_template.md master_resume.md
```
Fill in `master_resume.md` with your actual details.  
⚠️ This file is in `.gitignore` — it will **never** be committed.

### 6. Run the agent
```bash
python agent.py
```

---

## 🔧 Configuration

In `agent.py`, change the role and location at the bottom:

```python
if __name__ == "__main__":
    run_agent(job_role="Data Analyst Intern", location="Bangalore")
```

---

## 📁 Project Structure

```
ai-job-agent/
│
├── agent.py                    # Main agent script
├── master_resume_template.md   # Resume template (fill this in)
├── master_resume.md            # Your real resume (gitignored)
├── requirements.txt
├── .env.example                # API key template (safe to share)
├── .env                        # Your real keys (gitignored)
├── .gitignore
├── output/                     # Tailored resumes saved here (gitignored)
└── README.md
```

---

## 🔒 Security

The following files are blocked from being committed via `.gitignore`:

| File | Why |
|------|-----|
| `.env` | Contains your real API keys |
| `master_resume.md` | Contains your personal contact info |
| `output/` | Contains tailored resumes with your personal data |

Only `.env.example` and `master_resume_template.md` are public — they contain no real credentials or personal information.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) | LLM with native function calling |
| [Tinyfish Search API](https://tinyfish.ai) | Live job search |
| [Tinyfish Fetch API](https://tinyfish.ai) | Job page scraping |
| Python + python-dotenv | Core runtime + env management |

---

## 🗺️ Roadmap

- [x] Job search via Tinyfish
- [x] Job page scraping
- [x] Resume tailoring via Gemini
- [x] Save output to file
- [ ] Auto-apply to jobs
- [ ] Multi-job comparison
- [ ] CLI interface with role/location flags
- [ ] Web UI

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📄 License

[MIT](LICENSE)

---

*Built by [Ayush Kumar Singh](https://www.linkedin.com/in/ayushsingh2703)*
