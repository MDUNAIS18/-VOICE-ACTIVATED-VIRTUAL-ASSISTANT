from openai import OpenAI
#client = OpenAI()

client = OpenAI(
    api_key= # add your openAI key, 
)

completion = client.chat.completions.create(
    model= "gpt-4o-mini",
    messages= [
        { "role": "system", "content": "You are a helpful assistant." },
        {"role": "user", "content": "Write a haiku about recursion in programming.",}
]
)

print(completion.choices[0].message.content)
