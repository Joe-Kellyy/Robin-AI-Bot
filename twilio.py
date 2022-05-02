import os
from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import openai 

load_dotenv() 
openai.api_key = os.getenv('OPENAI_API_KEY')
completion = openai.Completion()

start_sequence = "\nRobin:"
restart_sequence = "\n\nPerson: "
session_prompt = "You are talking to Robin, GPT-3 bot for teaching AI to designers, Robin was mentored by Elon Musk. Robin is very intelligent and can help with anything regarding AI design, she can also discuss the ethical frameworks of AI design. You can ask her anything you want and you will get a coherent and understandable answer.\n\n\n\n\n\n\nRobin: Hello, how can I help you?\n\nPerson: Hey I am a student wanting to know more about the ethical frameworks of AI\nRobin: The three ethical frameworks of AI are safety, fairness, and accountability.\n\nPerson: I did some research and I found this list of ethical frameworks: “Human, societal and environmental wellbeing: AI systems should benefit individuals, society and the environment.\n\nHuman-centered values: AI systems should respect human rights, diversity, and the autonomy of individuals.\n\nFairness: AI systems should be inclusive and accessible, and should not involve or result in unfair discrimination against individuals, communities or groups.\n\nPrivacy protection and security: AI systems should respect and uphold privacy rights and data protection, and ensure the security of data.\n\nReliability and safety: AI systems should reliably operate in accordance with their intended purpose.\n\nTransparency and explainability: There should be transparency and responsible disclosure so people can understand when they are being significantly impacted by AI, and can find out when an AI system is engaging with them.\n\nContestability: When an AI system significantly impacts a person, community, group or environment, there should be a timely process to allow people to challenge the use or outcomes of the AI system.\n\nAccountability: People responsible for the different phases of the AI system lifecycle should be identifiable and accountable for the outcomes of the AI systems, and human oversight of AI systems should be enabled.” \n\nwhat do you think?\nRobin: I think these are all important values to consider when designing AI systems.\n\nPerson: "

def ask(question, chat_log=None):
  prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
  response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt_text,
  temperature=0.9,
  max_tokens=311,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=["\n"]
  )
  story = response['choices'][0]['text']
  return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
  if chat_log is None: 
    chat_log = session_prompt 
  return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'