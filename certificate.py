import hashlib

def hash_certificate(name: str, issuer: str, date: str) -> str:
    """Generate a unique SHA-256 fingerprint for a certificate."""
    certificate_data = f"{name} - {issuer} - {date}"
    return hashlib.sha256(certificate_data.encode()).hexdigest()

def verify_certificate(name: str, issuer: str, date: str, stored_hash: str) -> bool:
    """Check if a certificate matches a stored hash."""
    generated_hash = hash_certificate(name, issuer, date)
    return generated_hash == stored_hash

if __name__ == "__main__":
    # Test the hashing
    test_hash = hash_certificate("Roua Ouerfelli", "Dar Blockchain", "2026")
    print(f"Certificate hash: {test_hash}")
    
    # Test verification
    is_valid = verify_certificate("Roua Ouerfelli", "Dar Blockchain", "2026", test_hash)
    print(f"Certificate is valid: {is_valid}")
    
    # Test tampered certificate
    is_fake = verify_certificate("Roua Ouerfelli", "Fake Institution", "2026", test_hash)
    print(f"Tampered certificate is valid: {is_fake}")