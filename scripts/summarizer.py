from transformers import pipeline

# Initialize summarization model
summarizer = pipeline("summarization")

# Function to summarize long content
def summarize_text(text):
    try:
        # Summarize the content using DistilBERT
        summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Summarization failed: {e}")
        return text  # In case of failure, return the original text

# Example usage
if __name__ == "__main__":
    long_text = "This is a long article that needs summarization."
    print(summarize_text(long_text))
