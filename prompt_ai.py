from openai import OpenAI
import os
from datetime import datetime
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ ERROR: No API key found. Create a .env file with OPENAI_API_KEY=your_key_here")
    exit()

client = OpenAI(api_key=api_key)


def generate_prompt(topic, purpose="idea generation", model_type="chatgpt"):
    """Generate a structured, high-quality prompt for a given topic and purpose."""
    user_input = f"""
    You are a professional prompt engineer.
    Create a high-quality prompt for a {model_type}-style AI.
    Topic: {topic}
    Purpose: {purpose}

    The prompt should be detailed, clear, and ready to use.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Use gpt-3.5-turbo if you prefer
        messages=[{"role": "user", "content": user_input}],
        temperature=0.8
    )

    return response.choices[0].message.content.strip()


def main():
    print("\n🤖 Welcome to Prompt-Making AI (Loop Mode)")
    print("Type 'exit' anytime to quit.\n")

    while True:
        topic = input("📝 Enter topic: ")
        if topic.lower() == "exit":
            print("\n👋 Exiting... Goodbye!\n")
            break

        purpose = input("🎯 Enter purpose (e.g., idea generation, creative writing, code help): ")
        if purpose.lower() == "exit":
            print("\n👋 Exiting... Goodbye!\n")
            break

        model_type = input("⚙️ Enter model type (chatgpt / dalle / midjourney): ")
        if model_type.lower() == "exit":
            print("\n👋 Exiting... Goodbye!\n")
            break

        print("\n⏳ Generating your prompt...\n")

        try:
            prompt = generate_prompt(topic, purpose, model_type)
            print("✅ Here is your AI-ready prompt:\n")
            print("--------------------------------------")
            print(prompt)
            print("--------------------------------------")

            # Save to file
            with open("saved_prompts.txt", "a", encoding="utf-8") as f:
                f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
                f.write(f"Topic: {topic}\nPurpose: {purpose}\nModel: {model_type}\n")
                f.write(prompt + "\n")
                f.write("--------------------------------------\n")

            print("💾 Prompt saved to 'saved_prompts.txt'\n")

        except Exception as e:
            print(f"❌ Error: {e}\n")


if __name__ == "__main__":
    main()
