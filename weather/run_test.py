import subprocess
import sys
import json
import time

def main():
    # Start the server
    server_process = subprocess.Popen(
        ['uv', 'run', 'src/weather/server.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Give the server a moment to start
    time.sleep(1)
    
    # Prepare the request
    request = {
        "jsonrpc": "2.0",
        "method": "get-alerts",
        "params": {
            "state": "TX"
        },
        "id": 1
    }
    
    # Send the request
    print("Sending request to server...")
    json_request = json.dumps(request) + "\n"
    server_process.stdin.write(json_request)
    server_process.stdin.flush()
    
    # Read the response
    print("Waiting for response...")
    response = server_process.stdout.readline()
    
    try:
        result = json.loads(response)
        print("\nReceived response:", json.dumps(result, indent=2))
    except json.JSONDecodeError:
        print("Error: Invalid JSON response")
    
    # Clean up
    server_process.terminate()
    server_process.wait()

if __name__ == "__main__":
    main()
