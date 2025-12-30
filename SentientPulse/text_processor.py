import re

class TextProcessor:
    """
    Step 1: The TextProcessor.
    Goal: Transform raw user input into a batch list of clean sentences.
    Splits by punctuation to preserve the context for the TF-IDF Bigram model.
    """

    def __init__(self):
        # Regex to split by . ! or ? while keeping the sentence logic intact
        self.split_pattern = r'(?<=[.!?])\s+'

    def process_to_sentences(self, raw_text):
        """
        Takes raw string and returns a list of individual sentences.
        """
        if not raw_text or not isinstance(raw_text, str):
            return []

        # 1. Basic cleaning: remove newlines and extra spaces
        clean_text = raw_text.replace("\n", " ").strip()
        clean_text = re.sub(r'\s+', ' ', clean_text)

        # 2. Split text into a list based on sentence-ending punctuation
        sentences = re.split(self.split_pattern, clean_text)

        # 3. Final cleaning: remove any empty strings that might occur from split
        batch_list = [s.strip() for s in sentences if s.strip()]

        return batch_list

# ==========================================
# TESTING FUNCTION (Verification Block)
# ==========================================
def test_step_1():
    print("--- Testing Step 1: TextProcessor ---")
    processor = TextProcessor()

    # Scenario 1: Multiple sentences with different punctuation
    text_1 = "I am so happy today! But why is the weather so bad? I hope the Owl helps me."
    result_1 = processor.process_to_sentences(text_1)
    
    # Scenario 2: Single long sentence with no punctuation
    text_2 = "This is just one long sentence without any split marks"
    result_2 = processor.process_to_sentences(text_2)

    # Scenario 3: Text with extra spaces and newlines
    text_3 = "   Hello world.    This has   too many   spaces. \n And a new line!   "
    result_3 = processor.process_to_sentences(text_3)

    # Verifying Results
    print(f"Test 1 (Standard): {result_1}")
    assert len(result_1) == 3, f"Expected 3 sentences, got {len(result_1)}"

    print(f"Test 2 (No Punctuation): {result_2}")
    assert len(result_2) == 1, "Expected 1 sentence"

    print(f"Test 3 (Cleaning): {result_3}")
    assert "too many spaces." in result_3[1], "Cleaning failed to preserve text correctly"

    print("\n[SUCCESS] Step 1 passed all tests. Data is ready for the Batch loop.")








