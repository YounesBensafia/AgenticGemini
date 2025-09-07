from core.client import GeminiClient

def main():
    gemini = GeminiClient()
    response = gemini.generate("Why is the sky blue?")

    print("Model Response")
    print(response.text)

    print("\nUsage Stats:")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
