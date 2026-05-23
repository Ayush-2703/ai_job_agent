import os
import requests
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
TINYFISH_KEY = os.getenv("TINYFISH_API_KEY")


def tinyfish_search(query: str) -> str:
    """Search the web for job openings. Use this to find job links."""
    print(f"🔍 Searching for: {query}")
    r = requests.get(
        "https://api.search.tinyfish.ai",
        headers={"X-API-Key": TINYFISH_KEY},
        params={"query": query}
    )
    return str(r.json())


def tinyfish_fetch(url: str) -> str:
    """Extract text content from a job posting URL. Use this to read the job description."""
    print(f"📄 Reading page: {url}")
    r = requests.post(
        "https://api.fetch.tinyfish.ai",
        headers={"X-API-Key": TINYFISH_KEY},
        json={"urls": [url], "format": "markdown"}
    )
    return str(r.json())


def run_agent(job_role: str = "Machine Learning Intern", location: str = "India"):
    """
    Run the job search and resume tailoring agent.

    Args:
        job_role: The job title to search for (e.g. "Machine Learning Intern")
        location: Location to search in (e.g. "India", "Bangalore")
    """
    resume_path = "master_resume.md"
    if not os.path.exists(resume_path):
        raise FileNotFoundError(
            "master_resume.md not found. "
            "Copy master_resume_template.md to master_resume.md and fill in your details."
        )

    with open(resume_path, "r", encoding="utf-8") as f:
        resume = f.read()

    prompt = (
        f"Find a {job_role} job in {location} and tailor this resume to match the job description:\n\n"
        f"{resume}"
    )

    print("🤖 Gemini is thinking...")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[tinyfish_search, tinyfish_fetch],
            temperature=0.2,
            system_instruction=(
                "You are an expert career agent. "
                "Use the tools to find a real job opening, read its full description, "
                "and tailor the provided resume to match it. "
                "Rewrite the summary, reorder skills, and rephrase project bullets "
                "to align with the job's requirements and keywords."
            )
        )
    )

    print("\n--- FINAL TAILORED RESUME / JOB INFO ---")
    print(response.text)

    # Save output to file
    output_path = f"output/tailored_resume_{job_role.replace(' ', '_')}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"\n✅ Saved to {output_path}")


if __name__ == "__main__":
    # Change these to search for different roles/locations
    run_agent(job_role="Machine Learning Intern", location="India")
