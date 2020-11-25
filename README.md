# Bottle

### Task 1:
Newsletter subscription module - AWS service oriented task
Construct a working system with proper AWS services integration to achieve the following flow:
1. A user should be able to enter their email in a simple web interface, and hit the “Subscribe” button
2. If the email provided is not already present in our database table “Subscription emails”, the email should receive a confirmation link. If the email is present, the email should instead receive an email saying “You are already our member!”.
3. This first API should respond 200 OK if successful.
4. Upon clicking the confirmation link (second API), the user’s email should be added to the database table “Subscription emails”, and the user should be redirected to the website: “www.google.com”

### Task 2:
Get top features - Algorithm and Coding oriented task
Construct a working program which takes three parameter inputs: top features number (integer), possible features (array of strings), and feature requests (array of strings).
The goal of the program is to sort through feature requests received, and extract the most requested top number of features as long as it is a part of possible features.

This system would allow us to take in customer feature requests, and pick the top 3 (example) possible features to work on.

get_top_features(topFeaturesNumber=3,
possibleFeatures=["storage", "battery", "hover", "alexa","waterproof", "solar"],
featureRequests=[
"I wish my Kindle had even more storage",
"I wish the battery life on my Kindle lasted 2 years.",
"I read in the bath and would enjoy a waterproof Kindle",
"Waterproof and increased battery are my top two",
"I want to take my Kindle into the shower. Waterproof please waterproof!",
"I wanna make my Kindle hover on my desk",
"How about a solar Kindle!"])

#### Note:
One of the responsibilities of the role is proactively seek clarifications on any confusions and information that are often not explicitly mentioned in a use case.
Therefore feel free to reach out if you require further clarification on any of the use cases.
Also ensure that you have included proper docstrings and comments where applicable, included type hinting if applicable, followed OOP if applicable.
A technical design documentation draft of the approaches taken, problem statement breakdown, assumptions made, etc. would also be very helpful.

#### Constraints
- If your account is still in the sandbox, this address must be verified
- Thus, for the purpose of this assignment the email addresses have been hard coded
