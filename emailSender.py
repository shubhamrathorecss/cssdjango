from azure.communication.email import EmailClient
from azure.identity import DefaultAzureCredential

connection_string = "endpoint=https://cssemailcomservice.unitedstates.communication.azure.com/;accesskey=3vMdrlXW4tIH7cgqI7oJysoGePasvbF+J5gcp0qzX87SV5VLaxb3kvBJfE+20gqAwN5/RanYiItWn0GGUdh1dA=="
endpoint="https://cssemailcomservice.communication.azure.com/"
client = EmailClient(endpoint, DefaultAzureCredential())

message = {
    "content": {
        "subject": "This is the subject",
        "plainText": "This is the body",
        "html": "html><h1>This is the body</h1></html>"
    },
    "recipients": {
        "to": [
            {
                "address": "shubhamrathore7567@gmail.com",
                "displayName": "Shubham Rathore"
            }
        ]
    },
    "senderAddress": "DoNotReply@cloudsecurity.space"
}

poller = client.begin_send(message)
result = poller.result()

print(result)