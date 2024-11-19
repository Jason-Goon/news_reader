from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text):
    try:
        summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Summarization failed: {e}")
        return text  

if __name__ == "__main__":
    long_text = "This is a long article that needs summarization."
    print(summarize_text(long_text))
