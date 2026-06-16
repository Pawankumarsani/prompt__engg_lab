import os 
from groq import Groq
from prompts import ZERO_SHOT, FEW_SHOT, CHAIN_OF_THOUGHT, ROLE_PROMPT, SYSTEM_PROMPT 
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("prompt_engg"))

def evaluate_prompt(pattern_name, prompt_template, test_text):
    prompt = prompt_template.format(text=test_text)
    
    response = client.chat.completions.create(
        model ="llama-3.3-70b-versatile",
        messages =[{"role":"user", "content": prompt}],
        max_tokens = 50
    )
    
    answer = response.choices[0].message.content
    tokens = response.usage.total_tokens
    
    return {
        'pattern': pattern_name,
        'answer' : answer,
        'tokens' : tokens
    }
    
test_texts = [
    "What a lovely weather",
    "This is the worst film I had ever seen",
    "The weather is cloudy today"
]

patterns = {
    'Zero_Shot' : ZERO_SHOT,
    'Few_shot' : FEW_SHOT,
    'Chain_of _thought' : CHAIN_OF_THOUGHT,
    'Role_Prompt' : ROLE_PROMPT,
}

for text in test_texts:
    print(f"\nText: {text}")
    print("-" * 40)
    for name, template in patterns.items():
        result = evaluate_prompt(name, template, text)
        print(f"{result['pattern']}:{result['answer'].strip()} | Tokens: {result['tokens']}") 
    