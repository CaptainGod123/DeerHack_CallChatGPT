# DeerHack_CallGPT \newline
CallGPT

About \newline
An application that allows user to make a phone call to ChatGPT for easier access. Our goal with this project is make the use of ChatGPT more convenient and accessible. People can access it with just Wifi and a phone number. Future changes that we can make include: facetiming ChatGPT through our website TBD URL, refining and creating a better UI/UX for the website, and potentially create ad space.

How it works \newline
We use the TWILIO API to setup the call service. The call is connected to our backend code which is made using Flask and Twilio API. The code will receive speech from the user and translate it into text so that ChatGPT can understand it. The code will feed the text to ChatGPT through the OpenAi API. Final, the result from ChatGPT will be feed back to the user through the call, and the user may choose between continuing the call or hanging up.

Website \newline
Link to project github can be found through our website credability.tech until October 2023. The website is also in the same repository, except it is hosted under a different branch.

Requirements \newline
Python 3.9+ to run API \newline
Requests \newline
Openai \newline
Flask \newline
Twilio \newline

Made by: \newline
Guivir Sasan \newline
Weiming Quan \newline
Simran Mattu \newline
Kai Zheng \newline
