import openai
import os
import requests
import json
import datetime

from_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
to_date = datetime.datetime.now().strftime("%Y-%m-%d")

api_key = os.environ.get("openai")

# Set the API key
openai.api_key = 'INPUT YOUR OPEN AI KEY'

# Get the latest and trending news from the internet
response = requests.get("https://newsapi.org/v2/everything?q=climate+change&from={2023-01-07}&to={2023-01-14}&pageSize=1&apiKey=INPUT YOUR NEWS API KEY")
data = json.loads(response.text)
print(response.json())

# Use the news as prompts for GPT-3 to generate articles
articles = []
for news in data["articles"]:
    prompt = (f"Write an article script about the following topic:\n{news['title']}\n\n"
              f"Generated text should be between 300-500 words. Add a sense of humor and make it sound interesting and eyecatching")
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    articles.append(message)

# Print the generated articles
for article in articles:
    print(article)

