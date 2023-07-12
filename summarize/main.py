import click 
from transformers import pipeline 
import urllib.request
from bs4 import BeautifulSoup 
import os

os.environ['TF_CPP_MIN_LOG_LEVEL']="3"

def parser(url):
    text=""
    with urllib.request.urlopen(url) as response:
        html = response.read()
    soup = BeautifulSoup(html,'html.parser')
    for para in soup.find_all("p"):
        print(para.text)
        text+=para.text
    return text

def process(text):
    summarizer = pipeline("summarization",model="t5-small")
    result = summarizer(text,max_length=150)
    click.echo("Summary is ready!")
    click.echo("="*80)
    return result[0]["summary_text"]

@click.command()
@click.option('--url')
@click.option('--file')
def main(url,file):
    if url:
        text = parser(url)
    elif file:
        with open(file,'r') as f:
            text = f.read()
    click.echo(f"Summarized text from -> {url or file}")
    click.echo(process(text))



