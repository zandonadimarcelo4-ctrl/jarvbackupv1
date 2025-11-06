#!/usr/bin/env python3
"""
Simple interactive chatbot that echoes user input.
"""

def main():
    print("Olá! Eu sou o PitronIA. Como posso ajudar você hoje?")
    while True:
        try:
            user_input = input("Você: ")
        except EOFError:
            print("\nAté mais!")
            break
        if not user_input.strip():
            continue
        if user_input.lower() in {"sair", "exit", "quit"}:
            print("PitronIA: Até logo!")
            break
        # Simple echo response
        print(f"PitronIA: Você disse: '{user_input}'")

if __name__ == "__main__":
    main()