import asyncio
import json
import sys

async def send_request():
    print("Sending request to weather server...", file=sys.stderr)
    
    # Example request for get-alerts
    request = {
        "jsonrpc": "2.0",
        "method": "get-alerts",
        "params": {
            "state": "TX"
        },
        "id": 1
    }
    
    # Write the request to stdout
    json_request = json.dumps(request) + "\n"
    sys.stdout.write(json_request)
    sys.stdout.flush()
    
    print("Waiting for response...", file=sys.stderr)
    # Read the response from stdin
    response = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
    
    try:
        result = json.loads(response)
        print("\nReceived response:", json.dumps(result, indent=2), file=sys.stderr)
    except json.JSONDecodeError:
        print("Error: Invalid JSON response", file=sys.stderr)

if __name__ == "__main__":
    asyncio.run(send_request())
