import json
import os
from datetime import datetime
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

USERS_FILE = "users_registry_v101.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        default_users = {
            "admin": {
                "password": "Admin@1",
                "email": "admin@wealthspark.com",
                "phone": "+15550199",
                "activated": True,
                "activation_token": "verified",
                "sec_question": "What is your pet's name?",
                "sec_answer": "sparky",
                "last_login": str(datetime.now()),
                "audit_log": ["Account created and activated."]
            }
        }
        save_users(default_users)
        return default_users
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

def get_user_db_filename(username):
    safe_name = "".join(c for c in username.lower() if c.isalnum() or c in ('_', '-')).strip()
    return f"db_{safe_name}_v101.json"

def load_user_data(username):
    db_file = get_user_db_filename(username)
    default_data = {
        "accounts": [],
        "credit_health": {"score": 720, "utilization": 12.0, "payment_history": 100.0},
        "custom_assets": [],
        "custom_debts": [],
        "transactions": [],
        "security_settings": {
            "pin": "",
            "app_lock": False,
            "auto_lock_mins": 15,
            "two_fa": True,
            "last_backup_date": "Never"
        },
        "audit_log": [f"[{datetime.now()}] Initialized WealthSpark V101 profile."]
    }
    if not os.path.exists(db_file):
        save_user_data(username, default_data)
        return default_data
    try:
        with open(db_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            for key in default_data:
                if key not in data:
                    data[key] = default_data[key]
            return data
    except Exception:
        return default_data

def save_user_data(username, data):
    db_file = get_user_db_filename(username)
    with open(db_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def generate_encrypted_backup(data_dict, password):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    f = Fernet(key)
    json_bytes = json.dumps(data_dict).encode("utf-8")
    encrypted_data = f.encrypt(json_bytes)
    return base64.urlsafe_b64encode(salt + encrypted_data).decode("utf-8")

def decrypt_backup(encrypted_str, password):
    try:
        decoded_bytes = base64.urlsafe_b64decode(encrypted_str.encode("utf-8"))
        salt = decoded_bytes[:16]
        encrypted_data = decoded_bytes[16:]
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        f = Fernet(key)
        decrypted_bytes = f.decrypt(encrypted_data)
        return json.loads(decrypted_bytes.decode("utf-8"))
    except Exception:
        return None
