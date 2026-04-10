# This tool is used to extract the key points of a YouTube video transcript using Groq.
import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from tools.summarize_video_tool import summarize_video
from tools.get_transcript_tool import get_transcript
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Groq API key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
client = ChatGroq(model="openai/gpt-oss-20b")

def extract_key_points(summary_text):
    """
    Extract key learning points from a summarized video transcript.
    Args:
        Summary: The summary of the YouTube video
    Returns:
        The key points of the video summary
    """
    try:
        response = client.invoke([
            SystemMessage(
                content="You are an expert learning assistant that extracts educational insights from summaries."
            ),
            HumanMessage(
                content=f"""
                    From the following video summary, extract structured learning points.

                    Return the output in the following format:

                    Key Concepts:
                    - concept 1
                    - concept 2

                    Important Takeaways:
                    - takeaway 1
                    - takeaway 2

                    Possible Interview Questions:
                    - question 1
                    - question 2

                    Summary:
                    {summary_text}
                    """
            )
        ])

        return response.content

    except Exception as e:
        return f"Learning points extraction error: {str(e)}"