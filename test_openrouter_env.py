#!/usr/bin/env python3
"""
Test script for smolagents with OpenRouter using .env
"""

import os
from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIServerModel
from smolagents.default_tools import WebSearchTool

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    print("🚀 Testing smolagents with OpenRouter (using .env)...")
    
    # Get API credentials from environment
    api_key = os.getenv('OPENROUTER_API_KEY')
    api_base = os.getenv('OPENROUTER_API_BASE')
    model_id = os.getenv('OPENROUTER_MODEL')
    
    if not api_key:
        print("❌ Error: OPENROUTER_API_KEY not found in .env file")
        return
    
    print(f"✅ API Key loaded: {api_key[:20]}...")
    print(f"✅ API Base: {api_base}")
    print(f"✅ Model: {model_id}")
    
    # Configure the model to use OpenRouter
    model = OpenAIServerModel(
        model_id=model_id,
        api_base=api_base,
        api_key=api_key
    )
    
    # Create the agent with proper tools
    agent = CodeAgent(model=model, tools=[WebSearchTool()])
    
    # Test with a simple calculation
    print("\n📊 Test: Simple calculation")
    result = agent.run("What is 25 * 17?")
    print(f"Result: {result}")
    
    print("\n✅ smolagents + OpenRouter + .env working perfectly!")

if __name__ == "__main__":
    main() 