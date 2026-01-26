# SentientPluse
# 🌊 SentientPulse: The AI Emotion Bridge

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
 of a conversation using a custom-trained **Naive Bayes Bigram model**, the engine intelligently selects one of **120 unique personas** to guide the AI's response. 

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
## ▶️ How to Run & Test the Engine

This project does not require full deployment to understand or verify its functionality.

A dedicated **demo file** is provided to demonstrate how the SentientPulse engine works independently.

### 🔹 Prerequisites
- Python 3.9+
- Virtual environment recommended

Install dependencies:

```bash
pip install -r requirements.txt
## 🌟 Key Learnings & Engineering Highlights

This project represents a major milestone in my AI Engineering journey. Rather than focusing only on model accuracy, I concentrated on **system design, modular intelligence, and real-world usability**.

### 🔹 Engineering-Level Learnings

- Designed a **stateless AI middleware** that can be plugged into any application without modifying business logic.
- Learned how to separate **preprocessing logic from model inference**, improving clarity and maintainability.
- Implemented **custom text segmentation logic** to handle informal, punctuation-less user input.
- Understood how **feature engineering directly affects classical ML model performance**, especially in sparse high-dimensional text data.
- Applied **Bigram TF-IDF vectorization** to capture contextual sentiment shifts such as negations.
- Built a **Facade design pattern** to hide complex internal prompting logic from end users.
- Developed a reusable emotion engine independent of frontend or LLM provider.

### 🔹 AI & Machine Learning Insights

- Compared multiple algorithms (Naive Bayes, Logistic Regression, Decision Trees, Random Forest, Linear SVM).
- Observed why **Linear SVM performs better for high-dimensional NLP problems**.
- Learned trade-offs between:
  - Accuracy vs interpretability
  - Speed vs complexity
  - Classical ML vs Deep Learning readiness
- Designed the system to support future migration toward **LSTMs or hybrid models**.

### 🔹 System Architecture Understanding

- Engine operates as a **middleware between user input and LLMs**.
- Hidden system directives modify AI behavior without exposing internal instructions.
- Mood classification enables tone-aware AI responses.
- Persona registry abstracts emotional behavior into reusable profiles.

### 🔹 Professional Development

- Improved ability to translate real-world problems into technical architecture.
- Strengthened problem-solving and analytical thinking.
- Learned to design systems that scale conceptually, not just functionally.
- Gained confidence in building AI systems beyond simple API usage.

This project strengthened my foundation in **AI engineering, NLP pipelines, backend integration, and intelligent system design**, preparing me for advanced machine learning and real-world AI applications.
## 🚀 Future Improvements & Roadmap

SentientPulse is designed with extensibility in mind. The current version establishes a strong classical machine learning foundation, while future iterations aim to expand both intelligence depth and system capability.

### Planned Enhancements

- 🔁 **Hybrid ML Models**  
  Combine Linear SVM with Logistic Regression for improved robustness and confidence scoring.

- 🧠 **Deep Learning Integration**  
  Transition toward LSTM or Transformer-based models to better capture long-term contextual dependencies.

- 📊 **Emotion Intensity Scaling**  
  Introduce fine-grained emotion intensity levels instead of binary sentiment labels.

- 🧩 **Expanded Persona Intelligence**  
  Add adaptive persona evolution based on long-term user interaction patterns.

- 🌐 **Multi-language Support**  
  Extend preprocessing and tokenization pipelines to support regional languages.

- ⚙️ **Microservice Deployment**  
  Convert the engine into a standalone API service for scalable enterprise integration.

- 📈 **Analytics Dashboard**  
  Visualize emotional trends, negativity ratios, and behavioral metrics over time.

This roadmap ensures that SentientPulse can evolve from a research-grade middleware into a production-ready emotional intelligence layer.

---

## 👤 Author

**Syed Ameer Mustafa Haider Shah**  
AI Engineering Student | Machine Learning & NLP Enthusiast  

📌 Focus Areas:
- AI Engineering  
- Machine Learning  
- Natural Language Processing  
- Backend Systems  
- Intelligent Automation  

🔗 GitHub: https://github.com/SyedAmeerMustafaHaiderShah  
🔗 LinkedIn: https://www.linkedin.com/in/syedameermustafa/

---

> *“This project reflects my belief that AI should not only be intelligent —  
but emotionally aware, responsible, and human-centric.”*
