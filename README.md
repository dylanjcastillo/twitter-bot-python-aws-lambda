# Twitter Bot Using Python and AWS Lambda

![Python](https://img.shields.io/badge/Python-v3.8.3-brightgreen) ![License](https://img.shields.io/badge/license-MIT-blue) ![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat) [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/_dylancastillo.svg?style=social&label=Follow%20%40_dylancastillo)](https://twitter.com/_dylancastillo)

This a simple template you can use to build a twitter bot using Python and an AWS Lambda Function. I used it to create [@dereksiversbot](https://twitter.com/dereksiversbot). Learn how to make your own [here.](https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/)
 
Why build a bot this way?
 
 1. It's quick and easy 
 2. You have full control over the bot's actions
 3. It only uses services from AWS free tier (but see [limitations](#limitations) first)
 
## Pre-requisites

To build and use the bot, you'll need to:
 
 1. Register for a [twitter developer account](https://developer.twitter.com/en)  
 2. Create a [twitter app](https://developer.twitter.com/en/portal/projects-and-apps). Make sure to give it **Read and Write** permissions.
 3. Set up an [AWS account](https://aws.amazon.com/)
 4. Create a [Lambda Function](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html) for your bot
 5. Create a [Lambda Layer](https://medium.com/@adhorn/getting-started-with-aws-lambda-layers-for-python-6e10b1f9a5d) to use additional libraries in your Lambda Function 
 
## How to use

To make your own bot follow these steps:

1. Clone this repository on your local machine
2. Create a virtual environment in your project's root directory: `python3 -m venv venv && source venv/bin/activate`
3. Install the required libraries using pip: `pip install -r requirements.txt`
4. Create a file called `.env` in the root directory of your project. Put your twitter App keys there:
```
ACCESS_TOKEN=<YOUR_ACCESS_TOKEN_HERE>
ACCESS_TOKEN_SECRET=<YOUR_ACCESS_TOKEN_SECRET_HERE>
CONSUMER_KEY=<YOUR_CONSUMER_KEY_HERE>
CONSUMER_SECRET=<YOUR_CONSUMER_SECRET_HERE>
```
5. Make changes in the logic of the bot by modyifing `src/lambda_function.py`
6. Test your changes locally by running `python entrypoint.py` from the root directory of your project

## How to deploy

Once you are happy with your bot:

1. Add any additional packages you used to `requirements.txt`
2. Run `sh createlambdalayer.sh` from the root directory of your project. It'll generate a zip file with your libraries called `layer.zip`
3. Update your Lambda Layer using `layer.zip`
4. Run `sh buildpackage.sh` from the root directory of your project. It'll make a zip file with the code for your Lambda Function called `lambda_function.zip`
5. Upload `lambda_function.zip` to your Lambda Function
6. Add your twitter App keys as environment variables in the Lambda Function
7. Add a scheduled trigger to your Lambda Function using [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/run-lambda-schedule.html) 

## Limitations

Read this before using the bot:

- This is free unless you go crazy with it or use **custom events for triggering** the Lambda Function. Check the [AWS Free Tier](https://aws.amazon.com/free/) if you have any questions. Use it at your own risk!
- Current logic is very simple. The bot will post a random tweet (excluding its last 3 tweets). If you want something more complex, you'll need to add it on your own.

## Attributions

The `createlambdalayer.sh` script comes from [this repository](https://github.com/aws-samples/aws-lambda-layer-create-script).
