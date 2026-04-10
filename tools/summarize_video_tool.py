# This tool is used to summarize a YouTube video transcript using Groq.
import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from tools.get_transcript_tool import get_transcript
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# Set Groq API key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
client = ChatGroq(model="openai/gpt-oss-20b")

def summarize_video(transcript_text):
    """
    Generate a concise summary of a YouTube video transcript using Groq.
    Args:
        transcript: The transcript of the YouTube video
    Returns:
        The summary of the transcript
    """
    try:
        response = client.invoke([
            SystemMessage(
                content="You summarize educational video transcripts into clear and concise summaries."
            ),
            HumanMessage(
                content=f"Summarize the following YouTube video transcript:\n\n{transcript_text}"
            )
        ])
        return response.content
    except Exception as e:
        return f"Summary error: {str(e)}"


def summarize_video_in_chunks(transcript: str) -> str:
    """
    Generate a concise summary of a YouTube video transcript using Groq.
    Args:
        transcript: The transcript of the YouTube video
    Returns:
        The summary of the transcript
    """
    try:
        # 1. Split text into 3000-character chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=200)
        chunks = text_splitter.split_text(transcript)
        
        summaries = []
        for chunk in chunks:
            # Call your LLM here to summarize this specific chunk
            response = client.invoke([
                SystemMessage(
                    content="You summarize educational video transcripts into clear and concise summaries."
                ),
                HumanMessage(
                    content=f"Summarize the following YouTube video transcript:\n\n{chunk}"
                )
            ])
            summaries.append(response.content)
        
        # 2. Combine and summarize the summaries
        final_combined = " ".join(summaries)
        final_summary = client.invoke(f"Provide a concise final summary of these notes: {final_combined}")
        
        return final_summary.content
    except Exception as e:
                return f"Summary error: {str(e)}"