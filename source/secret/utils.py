from datetime import timedelta, datetime
from cryptography.fernet import Fernet

from source.settings import HEX_ENCODE_KEY


KEY = bytes.fromhex(HEX_ENCODE_KEY)
cipher_suite = Fernet(KEY)


def encode(data: str) -> bytes:
    """
    Encrypts the input data using a cipher suite and returns the encrypted bytes.
    Args:
        data (str): The input data to be encrypted.
    Returns:
        bytes: Encrypted data in bytes format.
    """
    encrypted_data = cipher_suite.encrypt(data.encode('utf-8'))
    return encrypted_data


def decode(data: bytes) -> str:
    """
    Decrypts the input encrypted data and returns the original string.
    Args:
        data (bytes): The encrypted data in string format.
    Returns:
        str: Decrypted original data as a string.
    """
    decrypted_data = cipher_suite.decrypt(data).decode('utf-8')
    return decrypted_data


def calculate_ttl(created_at: datetime, living_time: str) -> datetime:
    """
    func for calculating expiration time for a Secret object
    """
    match living_time:
        case '1 hour':
            return created_at + timedelta(hours=1)
        case '3 hours':
            return created_at + timedelta(hours=3)
        case '1 day':
            return created_at + timedelta(days=1)
        case '3 days':
            return created_at + timedelta(days=3)
        case '1 week':
            return created_at + timedelta(days=7)
