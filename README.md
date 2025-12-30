# SentientPluse
# 🌊 SentientPulse: The AI Emotion Bridge

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![ML](https://img.shields.io/badge of a conversation using a custom-trained **Naive Bayes Bigram model**, the engine intelligently selects one of **120 unique personas** to guide the AI's response. 

Whether the user is in a state of **Crisis, Struggle, Balanced, or Positive**, SentientPulse injects hidden system directives that modify the AI's behavior, setting, and tone—keeping all the complex logic hidden from the user while delivering a deeply personalized experience.

---

## 🚀 Key Features

- **🎭 120 Dynamic Personas:** Automatically maps user moods to 60 animal spirits and 60 pop-culture icons.
- **🧠 ML-Driven Sentiment Engine:** Utilizes a custom-trained Naive Bayes Bigram model with TF-IDF Vectorization for high-accuracy emotion detection.
- **⚡ Stateless Architecture:** Lightweight and independent. No database required within the module—plug it into any existing application.
- **🛡️ Invisible Prompt Engineering:** Generates hidden system directives that guide the AI's behavior without the user ever seeing the internal logic.
- **📊 Granular Metadata:** Provides developers with negativity/positivity ratios and mood labels for internal analytics and daily reporting.

---

## 🛠️ How it Works

1. **Text Processor:** Splits raw input into balanced, sentence-level batches based on punctuation to preserve context.
2. **Sentiment Adapter:** Feeds the batch into the ML model to get real-time sentiment labels.
3. **Mood Aggregator:** Calculates the percentage of negativity (ignoring neutral inputs) to determine the "Mood Bucket."
4. **Persona Registry:** Randomly selects a character (e.g., The Lion, The Owl, Batman) from the appropriate bucket.
5. **Prompt Constructor:** Wraps the original text in a rich, character-driven hidden directive.

---

## 📦 Installation



```bash
# Clone the repository
git clone https://github.com/SyedAmeerMustafaHaiderShah/SentientPulse.git

# Install dependencies
pip install -r requirements.txt
******************************************************************************************************************************************************************************************************************bbbbbb******************************************************************************************************************************************************************************************************************

**Quick Start (Test Code)**
Use the following code to test the module independently. This demonstrates how the engine processes text and generates the "Secret Prompt."
code
Python
from emotion_module import EmotionModule

# 1. Initialize the SentientPulse Engine
engine = EmotionModule()

# 2. Define a sample user input
user_text = "I am so frustrated with this project! Nothing is working and I feel like giving up."

# 3. Process the text to get the AI Instruction
# This single call handles cleaning, ML analysis, and prompt engineering
result = engine.get_ai_instruction(user_text)

# 4. VIEW THE OUTPUTS
print("="*50)
print("📦 PROMPT TO SEND TO YOUR AI (ChatGPT/LLM):")
print("-" * 50)
print(result['secret_prompt'])

print("\n" + "="*50)
print("📊 METADATA FOR YOUR INTERNAL DATABASE:")
print("-" * 50)
print(f"Persona Selected: {result['metadata']['persona_name']}")
print(f"Emotion Label:    {result['metadata']['mood_label']}")
print(f"Negativity Ratio: {result['metadata']['negativity_ratio']}%")
print(f"Positivity Ratio: {result['metadata']['positivity_ratio']}%")
print("="*50)

****************************************************************************************************************************************************************************************************b************************************************************************************************************************************************************************************************************************************
📝 Developer Reference
SentientPulse returns a dictionary with the following keys for easy integration:
Key	Type	Description
secret_prompt	String	The final string to send to your LLM API. Includes the hidden [SYSTEM INSTRUCTION].
metadata	Dict	Contains persona_name, mood_label, negativity_ratio, and positivity_ratio.
Pro Tip: Since the engine is stateless, you should store the metadata in your own database for every chat. This allows you to generate daily reports or parental alerts by averaging the negativity ratios over a 24-hour period.
******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
🤝 Contributing
We are always looking for more characters! If you'd like to add a persona to our 120-character registry, please:
Fork the repo.
Add the persona to persona_registry.py.
Submit a Pull Request.
******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************
