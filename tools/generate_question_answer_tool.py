# This tool is used to generate a question and answers based on the extracted key learning points using Groq.
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
from tools.get_transcript_tool import get_transcript
from tools.summarize_video_tool import summarize_video
from tools.extract_key_points_tool import extract_key_points
import os

load_dotenv()

# Set Groq API key
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
client = ChatGroq(model="openai/gpt-oss-20b")

def generate_question_answer_pairs(key_points):
    """
    Generate a question and answer pairs based on the Key Points and Interview Questions from extracted key proints script using Groq. 
    Args:
        key_points: The key points of the YouTube video summary
    Returns:
        The questions/answers based on the key points
    """
    try:
        response = client.invoke([
            SystemMessage(
                content="You are an expert teachor, mentor, coach that generates relatevant question and answers"
            ),
            HumanMessage(
                content=f"""
                    From the following Key Points and Possible Interview Questions, extract Questions and generate the correct answer
                    Return the output in the following format:

                    Important Interview Questions:
                    Question 1. question 
                        Answer-  answer
                    Question 2. question 
                        Answer-  answer

                    Key Points:
                    {key_points}
                    """
            )
        ])
        return response.content
    except Exception as e:
        return f"Question and answer pairs generation error: {str(e)}"