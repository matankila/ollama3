# ollama3
This repo uses llama3 with simple yet meaningfull example
of creating document bot.

## What is this repo for
Exploring ollama capabilities & POC.

## How we did it?
we used langchain framework to connect to ollama server
to do embeding of the pdf and creating vector from it later be used to fetch simillar phrases from pdf than all of that goes into prompt to be proccessed by ollama.

## what is ollama3?
ollama3 is Meta LLM which is opensource!

## How to set it up?
in the code we use 2 models:
1. 8b (for GenAI, simillar to gpt, claud, etc.. models)
2. nomic-embed-text (for embedding, simillar to ada2)

we have a Dockerfile containing the ollama server and the 2 models
you can play with it as you want.

you can access it via [dockerhub](https://hub.docker.com/repository/docker/matanxno123/ollama3/general)