import hashlib
from certificate import hash_certificate, verify_certificate
from hedera_service import submit_hash_to_hedera, query_hedera_topic
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("=" * 60)
    print("  Decentralized Certificate Verifier — Hedera Network")
    print("=" * 60)
    print()

    # Step 1: Create a certificate
    name = "Roua Ouerfelli"
    issuer = "Dar Blockchain"
    date = "2026"

    print(f"📄 Certificate Details:")
    print(f"   Name   : {name}")
    print(f"   Issuer : {issuer}")
    print(f"   Date   : {date}")
    print()

    # Step 2: Hash the certificate
    cert_hash = hash_certificate(name, issuer, date)
    print(f"🔐 SHA-256 Hash Generated:")
    print(f"   {cert_hash}")
    print()

    # Step 3: Submit to Hedera
    print("📡 Submitting hash to Hedera Testnet...")
    result = submit_hash_to_hedera(cert_hash)
    print(f"   Status  : {result['status']}")
    print(f"   Network : {result['network']}")
    print(f"   Memo    : {result['memo']}")
    print()

    # Step 4: Verify original certificate
    print("✅ Verifying original certificate...")
    is_valid = verify_certificate(name, issuer, date, cert_hash)
    print(f"   Result: {'VALID ✅' if is_valid else 'INVALID ❌'}")
    print()

    # Step 5: Test tampered certificate
    print("🔍 Testing tampered certificate...")
    is_fake = verify_certificate("Roua Ouerfelli", "Fake University", "2026", cert_hash)
    print(f"   Result: {'VALID ✅' if is_fake else 'INVALID ❌ — Tampering detected!'}")
    print()

    print("=" * 60)
    print("  Project by Roua Ouerfelli | ESPRIT | Hedera SDK | 2026")
    print("=" * 60)

if __name__ == "__main__":
    main()