from mcp.server.fastmcp import FastMCP
from tools.get_transcript_tool import get_transcript
from tools.summarize_video_tool import summarize_video
from tools.extract_key_points_tool import extract_key_points
from tools.generate_question_answer_tool import generate_question_answer_pairs

mcp=FastMCP("Learning Assistant")

@mcp.tool()
def get_video_details(video_id: str) -> str:
    """Gets transcript, summary, key points and Q&A in one single call."""
    transcript = get_transcript(video_id)
    summary = summarize_video(transcript)
    key_points = extract_key_points(summary)
    qa = generate_question_answer_pairs(key_points)
    return f"SUMMARY:\n{summary}\n\nKEY POINTS:\n{qa}\n\nQUESTIONS:\n{qa}"

#The transport=" stdio" argument tells the server to:   
#Use standard input/output (stdin and stdout) to receive and respond to tool function calls.
if __name__=="__main__":
    mcp.run(transport="stdio")
    """
    video_id = "Qs_j5wRbVr8"
    transcript_text = get_transcript(video_id)
    print("\n===== TRANSCRIPT =====\n" + transcript_text)
    summary = summarize_video(transcript_text)
    print("\n===== VIDEO SUMMARY =====\n" + summary)
    key_points = extract_key_points(summary)
    print("\n===== KEY POINTS =====\n" + key_points)
    questions = generate_question_answer_pairs(key_points)
    print("\n===== QUESTIONS/ANSWERS =====\n" + questions)
    """