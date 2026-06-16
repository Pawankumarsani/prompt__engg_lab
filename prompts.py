#Different prompt patterns

#Zero-Shot
ZERO_SHOT ="""
Classify the sentiment  of this text as 
Posivite, Negative, Neutral:
Text: {text}
Sentiment:
"""

#Few-Shot
FEW_SHOT ="""
Classify sentiment.
Examples:
Text:"I love this!" - Posivite 
Text:"This is terible" - Negative
Text:"It's okay" - Neutral

Now classify:
Text: {text}
Sentiment:
"""

#Chain of thought
CHAIN_OF_THOUGHT="""
Classify sentiment step by step:
1. Read the text carefully
2. Identify emotional words
3. Determine overall tone
4. Classify as Positive/Negative/Neutral

Text: {text}
Let's think step by step:
"""
#Role Prompt
ROLE_PROMPT ="""
You are an expert sentiment analyst
with 10 years of experience.
Analyze this text and classify sentiment:
Text: {text}
Expert Analysis:
"""

#System Prompt
SYSTEM_PROMPT ="""
You are a sentiment classifier.
Rules:
- Only respond with one word
- Choose from: Positive, Negative, Neutral
- No explaination needed

"""



