import asyncio
import json
from pathlib import Path
from typing import List

from openai import OpenAI, AsyncOpenAI

with open(Path.home() / 'secrets.json') as f:
    api_key = json.load(f)['OPENAI_API_KEY_ARA_MAIN']

VALID_MODELS = ('gpt-4o-mini', 'gpt-4o', 'gpt-4', 'gpt-3.5-turbo')

def llm_call(prompt, model_name='gpt-4o-mini', context=None, temperature=0.0, img_urls=None, max_tokens=4096, force_json=False):
    if model_name not in VALID_MODELS:
        raise ValueError(f'Invalid model name: {model_name}. Must be one of: {VALID_MODELS}')

    client = OpenAI(api_key=api_key)
    
    messages = []
    
    if context:
        for context_item in context:
            messages.append({
                'role': 'system', 
                'content': [{'type': 'text', 'text': context_item}]
            })
            
    user_message = {
        'role': 'user', 
        'content': [{'type': 'text', 'text': prompt}]
    }
    
    if img_urls:
        for img_url in img_urls:
            img_data = {
                'type': 'image_url',
                'image_url': {'url': img_url},
            }
            user_message['content'].append(img_data)

    messages.append(user_message)
    
    response = client.chat.completions.create(
        model=model_name,
        temperature=temperature,
        response_format={'type': 'json_object'} if force_json else None,
        max_tokens=max_tokens,
        messages=messages,
    )
    return response.choices[0].message.content

async def async_llm_call(prompt, model_name='gpt-4o-mini', context=None, temperature=0.0, img_urls=None, max_tokens=4096, force_json=False):
    if model_name not in VALID_MODELS:
        raise ValueError(f'Invalid model name: {model_name}. Must be one of: {VALID_MODELS}')

    client = AsyncOpenAI(api_key=api_key)
    
    messages = []
    
    if context:
        for context_item in context:
            messages.append({
                'role': 'system', 
                'content': [{'type': 'text', 'text': context_item}]
            })

    user_message = {
        'role': 'user', 
        'content': [{'type': 'text', 'text': prompt}]
    }
    
    if img_urls:
        for img_url in img_urls:
            img_data = {
                'type': 'image_url',
                'image_url': {'url': img_url},
            }
            user_message['content'].append(img_data)

    messages.append(user_message)
    
    response = await client.chat.completions.create(
        model=model_name,
        temperature=temperature,
        response_format={'type': 'json_object'} if force_json else None,
        max_tokens=max_tokens,
        messages=messages,
    )
    return response.choices[0].message.content

async def _llm_call_batch_async(prompts: List[str], **kwargs) -> List[str]:
    tasks = [async_llm_call(prompt, **kwargs) for prompt in prompts]
    return await asyncio.gather(*tasks)

def run_llm_batch(prompts: List[str], **kwargs) -> List[str]:
    kwargs.setdefault('model_name', 'gpt-4o-mini')
    return asyncio.run(_llm_call_batch_async(prompts, **kwargs))

def test_run_llm_batch(model_name: str, temperature: float):
    print(f"Testing run_llm_batch with {model_name}:")
    prompts = [
        "What's 2 + 2?",
        "Name a primary color.",
        "What's the capital of France?",
        "How many legs does a cat have?",
        "Is the Earth flat or round?"
    ]
    
    responses = run_llm_batch(prompts, model_name=model_name, temperature=temperature, max_tokens=128)
    
    for prompt, response in zip(prompts, responses):
        print(f"Q: {prompt}")
        print(f"A: {response.strip()}\n")

if __name__ == '__main__':
    # Test with default model (gpt-4o-mini)
    test_run_llm_batch(model_name='gpt-4o-mini', temperature=0.3)
    
    print("="*50 + "\n")