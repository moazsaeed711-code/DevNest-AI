from app.database import SessionLocal, User
from app.auth import get_password_hash

db = SessionLocal()

# Create test user
username = "test"
password = "test123"
email = "test@test.com"

hashed = get_password_hash(password)
user = User(username=username, email=email, hashed_password=hashed)
db.add(user)
db.commit()

print(f"User created: {username}")
print(f"Password: {password}")