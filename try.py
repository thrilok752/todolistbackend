import requests
import json

# --- Configuration ---
REGISTER_URL = "http://127.0.0.1:8000/auth/users/"

# Data for the initial user (must be unique before Test 1)
VALID_DATA = {
    "username": "TestUserA",
    "email": "unique_test@example.com",
    "password": "Passw0rd1!",
    "re_password": "Passw0rd1!",
}

# Data for the duplicate attempt (same email)
DUPLICATE_DATA = {
    "username": "TestUserB", # Different username
    "email": "unique_test@example.com", # <--- SAME EMAIL
    "password": "Passw0rd2!",
    "re_password": "Passw0rd2!",
}

# Data for the successful third attempt (new email)
SUCCESS_DATA = {
    "username": "TestUserC", 
    "email": "another_unique_test@example.com", # <--- NEW EMAIL
    "password": "Passw0rd3!",
    "re_password": "Passw0rd3!",
}

def run_test(name, payload):
    """Sends a POST request and prints the status and response."""
    print(f"\n=======================================================")
    print(f"TEST: {name}")
    print(f"Sending Email: {payload['email']}")
    
    try:
        response = requests.post(
            REGISTER_URL,
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        # Print Status Code
        print(f"RESULT: HTTP Status {response.status_code}")
        
        # Print Response Body
        try:
            print(f"Response Body: {response.json()}")
        except json.JSONDecodeError:
            print(f"Response Body (Non-JSON): {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not connect to the Django server. Is it running on http://127.0.0.1:8000?")
        
    print("=======================================================")


if __name__ == "__main__":
    
    # ----------------------------------------------------
    # TEST 1: SUCCESS - Register the first user
    # ----------------------------------------------------
    run_test("1. SUCCESSFUL INITIAL REGISTRATION", VALID_DATA)
    
    # ----------------------------------------------------
    # TEST 2: FAILURE - Attempt registration with the same email
    # This proves the UniqueValidator is running.
    # ----------------------------------------------------
    run_test("2. FAILURE: DUPLICATE EMAIL CONSTRAINT CHECK", DUPLICATE_DATA)
    
    # ----------------------------------------------------
    # TEST 3: SUCCESS - Change only the email, proving all other data is valid
    # ----------------------------------------------------
    run_test("3. SUCCESS: DIFFERENT EMAIL", SUCCESS_DATA)