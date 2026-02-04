# User Authentication Documentation

## Acceptance Criteria
- Users can register with a unique username and password
- Users can log in using their registered credentials
- Passwords are securely stored using hashing
- Invalid login or registration attempts display clear error messages
- Successful login starts a user session

---

## Registration Flow

### Steps
1. User selects **Register**
2. User enters:
   - Username
   - Password
3. System validates input and checks for username uniqueness
4. Password is hashed before being stored
5. User data is saved to the database
6. User receives confirmation of successful registration
7. User is redirected to the login screen

---

## Login Flow

### Steps
1. User selects **Login**
2. User enters:
   - Username
   - Password
3. System validates credentials
4. On success:
   - User is authenticated
   - User session begins
   - User is redirected to the main application
5. On failure:
   - An error message is displayed
   - Access is denied
