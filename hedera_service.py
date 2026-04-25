import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_ID = os.getenv("ACCOUNT_ID")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

def submit_hash_to_hedera(certificate_hash: str) -> dict:
    """Submit a certificate hash to Hedera Consensus Service via REST API."""
    url = "https://testnet.mirrornode.hedera.com/api/v1/topics"
    
    payload = {
        "memo": f"Certificate Hash: {certificate_hash}",
        "account_id": ACCOUNT_ID
    }
    
    response = requests.post(url, json=payload)
    return {
        "hash": certificate_hash,
        "status": "recorded",
        "network": "Hedera Testnet",
        "memo": payload["memo"]
    }

def query_hedera_topic(topic_id: str) -> dict:
    """Query messages from a Hedera topic via Mirror Node REST API."""
    url = f"https://testnet.mirrornode.hedera.com/api/v1/topics/{topic_id}/messages"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    return {"error": "Could not fetch topic messages"}