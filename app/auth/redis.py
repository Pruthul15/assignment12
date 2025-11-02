# app/auth/redis.py
"""
Redis token blacklist management.
For now, this is a simple in-memory implementation.
In production, replace with actual Redis connection.
"""

# Simple in-memory token blacklist (for development/testing)
_token_blacklist = set()

async def add_to_blacklist(jti: str, exp: int):
    """Add a token's JTI to the blacklist"""
    _token_blacklist.add(jti)

async def is_blacklisted(jti: str) -> bool:
    """Check if a token's JTI is blacklisted"""
    return jti in _token_blacklist