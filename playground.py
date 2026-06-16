import os 
from groq import Groq
from prompts import ZERO_SHOT, FEW_SHOT, CHAIN_OF_THOUGHT, ROLE_PROMPT, SYSTEM_PROMPT 
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("prompt_engg"))

print("==== Prompt Engineering Playground ====")
print("Patterns: 1-Zero_shot 2-Few_shot 3-Chain_of_thought 4-Role 5- System")

while True:
    choice = input("\nChoose patterns (1-5) or quit: ")
    if choice.lower() == "quit":
        print("Goodbye!")
        break
    
    text = input("Enter text analysis: ")
    
    patterns = {
        '1': ('Zero_Shot', ZERO_SHOT),
        '2': ('Few_Shot', FEW_SHOT),
        '3': ('Chain_of_thought', CHAIN_OF_THOUGHT),
        '4': ('Role_prompt', ROLE_PROMPT),
        '5': ('System_Prompt', SYSTEM_PROMPT)
    }
    
    if choice in patterns:
        name, template = patterns[choice]
        
        if choice == '5':
            response = client.chat.completions.create(
                model='llama-3.3-70b-versatile',
                messages=[
                    {"role":"system","content":SYSTEM_PROMPT},
                    {"role":"user","content":text}
                ],
                max_tokens=50
            )
        else:
            prompt = template.format(text=text)
            response = client.chat.completions.create(
                model ="llama-3.3-70b-versatile",
                messages =[{"role":"user", "content": prompt}],
                max_tokens = 50
            )
            
        answer = response.choices[0].message.content
        tokens = response.usage.total_tokens
        
        print(f"\nPattern: {name}")
        print(f"Result: {answer.strip()}")
        print(f"Tokens used: {tokens}")
        
    else:
        print("Invalid Choice!")