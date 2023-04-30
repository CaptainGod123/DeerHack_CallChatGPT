# DeerHack_CallGPT
**CallGPT**

# About
An application that allows users to make a phone call to ChatGPT for easier access. Our goal with this project is to make ChatGPT more convenient and accessible. People can access it with just Wifi and a phone number. Future changes that we can make include: facetiming ChatGPT through our website TBD URL, refining and creating a better UI/UX for the website, and potentially create ad space.

# How it works
We use the TWILIO API to set up the call service. The call is connected to our backend code, which uses Flask and Twilio API. The code will receive speech from the user and translate it into text so that ChatGPT can understand it. The code will feed the text to ChatGPT through the OpenAi API. Finally, the result from ChatGPT will be fed back to the user through the call, and the user may choose between continuing the call or hanging up.

# Website
Link to project github can be found through our website credability.tech until October 2023. The website is also in the same repository, except it is hosted under a different branch.

# Requirements
- Python 3.9+ to run API 
- Requests
- Openai
- Flask
- Twilio

# Made by:
- Guivir Sasan
- Weiming Quan
- Simran Mattu
- Kai Zheng
