#!/bin/bash
echo "Alright, shit's about to go down."
sleep 2
echo "Look, this is how it's going to work."
sleep 2
echo "I'm going to have a conversation with you, while I do stuff to your computer in the background."
sleep 2
echo "It's all legal. Mostly :D"
sleep 2
echo "Firstly, what's your name?"
read name
echo "Welcome dumbass!"
sleep 1
echo "HAHA! Hi $name"
sleep 2
echo "Are you ready? [Yes, No]"
read whocares
if [ $whocares ==  "Yes" ]; then
    echo "LEGGO!"
else
    echo "Well I was never programmed to give a jack about your answer"
fi
sleep 2
echo "SO, $name! We're going to install a virtual environment now called venv. SO, you know..."
sleep 2
echo "We don't mess things up in your computer"
sleep 2
echo "Installing virtual env..."
python3 -m venv venv
echo "Done!"
sleep 2
echo "Let's move over to this new virtual environment"
sleep 2
source venv/bin/activate
sleep 2
echo "In it now!"
sleep 2
echo "Okay, I got to get up early for work tomorrow. Let's wrap this up quickly"
sleep 2
echo "Installing packages from requirements.txt..."
echo "You'll see some messages now. In 3, 2, 1..."
sleep 2
pip3 install -r requirements.txt
echo "Done!"
echo "Finally running the script we wrote"
sleep 3
echo "See you on the other side, this is where I say good night!"
python3 main.py
