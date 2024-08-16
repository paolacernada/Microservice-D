
# Microservice D - Motivational Quotes Provider

## Overview
This microservice provides a random motivational quote when requested by the main application. It is intended to encourage the user after dice rolls.

## Functionality
- Responds with a random motivational quote.

## Communication
- **Protocol:** ZeroMQ (REP-REQ)
- **Port:** `tcp://*:5558`
- **Endpoint:** Sends a motivational quote upon request.

## Requirements
- ZeroMQ library.

## How to Run
1. Ensure ZeroMQ is installed.
2. Run the script using Python:
   ```bash
   python microservice_d.py
