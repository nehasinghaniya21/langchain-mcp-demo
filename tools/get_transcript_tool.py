# This tool is used to get the transcript of a YouTube video using the youtube_transcript_api library.
from youtube_transcript_api import YouTubeTranscriptApi

# This function is used to get the transcript of a YouTube video using the youtube_transcript_api library.
def get_transcript(video_id):
    """
    Get the transcript of a YouTube video
    Args:
        video_id: The ID of the YouTube video
    Returns:
        The transcript of the YouTube video
    """
    api = YouTubeTranscriptApi()

    try:
        transcript = api.fetch(video_id)

        text = " ".join([segment.text for segment in transcript])
        # Only send the first ~10000 characters to the LLM to avoid blowing up the JSON tool-call limit.
        return text[:10000] 
        # return text

    except Exception as e:
        return f"Transcript error: {str(e)}"

if __name__=="__main__":
    video_id = "Qs_j5wRbVr8"
    transcript_text = get_transcript(video_id)
    print("\n===== TRANSCRIPT =====\n")
    print(transcript_text)