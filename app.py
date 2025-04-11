Hello Amar
Good morning Amaimport json

def lambda_handler(event, context):
    # Print the event to the logs for debugging
    print(f"Received event: {json.dumps(event)}")

    # Example of accessing data from the event (API Gateway or other)
    if 'body' in event:
        body = json.loads(event['body'])
        name = body.get('name', 'Unknown')
    else:
        name = 'Guest'

    # Create a response object
    response = {
        'statusCode': 100,
        'body': json.dumps({
            'message': f"Hello, {name}!",
            'input': event
        })
    }

    returnse
