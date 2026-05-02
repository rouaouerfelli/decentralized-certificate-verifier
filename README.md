# Decentralized Certificate Verifier
### Built on Hedera Network | 2026

**Author:** Roua Ouerfelli  
**Status:** Core Implementation Complete

---

## Overview
A decentralized system for verifying digital certificates using the Hedera blockchain network. Each certificate is hashed using SHA-256 and recorded on the Hedera Consensus Service, making it tamper-proof and publicly verifiable without any central authority.

## How It Works
1. A certificate is hashed using SHA-256
2. The hash is submitted to the Hedera Testnet via Mirror Node REST API
3. Anyone can verify a certificate by comparing its hash to the on-chain record
4. Tampered certificates are automatically detected

## Technology
- Python 3.13
- Hedera Consensus Service (HCS)
- Hedera Mirror Node REST API
- SHA-256 Cryptographic Hashing

## Project Structure
- `main.py` — Main application
- `certificate.py` — Hashing and verification logic
- `hedera_service.py` — Hedera network interaction

## Results
- Certificate hashing ✅
- Hedera Testnet submission ✅
- Certificate verification ✅
- Tamper detection ✅
