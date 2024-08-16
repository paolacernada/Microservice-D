import zmq
import random

quotes = [
    "Keep rolling, you got this!",
    "Luck favors the brave!",
    "Every roll is a new opportunity.",
    "Believe in your rolls!",
    "You're on a winning streak!",
    "Don't give up now!",
    "Roll with confidence!",
    "The next roll could be the one!",
    "Stay positive, roll high!",
    "Fortune favors the bold.",
    "Roll like a champion!",
    "Today is your day to shine!",
    "Every roll counts, make it matter.",
    "Success is just a roll away.",
    "Your best roll is yet to come!",
    "Make each roll better than the last.",
    "Victory is in your hands!",
    "The dice are in your favor.",
    "One roll at a time, you got this!",
    "Let the good rolls begin!",
    "Your next roll could change everything!",
    "Keep the momentum going!",
    "Let the dice work their magic!",
    "You're closer to victory with every roll.",
    "You're in control, roll with it!",
    "Trust your instincts and roll!",
    "Stay cool, roll smooth!",
    "Keep pushing, your roll is coming!",
    "You're the master of the dice!",
    "Make every roll count!"
]

# Initialize the ZeroMQ context
context = zmq.Context()

# Create a REP (reply) socket to receive requests
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5558")

print("Microservice D is running...")

while True:
    # Wait for a request from the client
    message = socket.recv_string()
    print(f"Request received: {message}")

    if message == 'get_motivation':
        # Select a random quote from the list
        response = random.choice(quotes)

        # Send the response back to the client
        socket.send_string(response)
        print(f"Sent motivational quote: {response}")
    else:
        # Send a default response if the request is not recognized
        socket.send_string("Invalid request")
        print("Sent response: Invalid request")
