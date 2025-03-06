import gradio as gr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return "😊 Positive"
    elif score <= -0.05:
        return "😠 Negative"
    else:
        return "😐 Neutral"

iface = gr.Interface(
    fn=analyze_sentiment,
    inputs="text",
    outputs="text",
    title="Simple Sentiment Analysis",
    description="Enter text to analyze sentiment (Positive, Negative, Neutral)."
)

iface.launch()
