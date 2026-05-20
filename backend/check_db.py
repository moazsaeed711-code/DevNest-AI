import sqlite3

# Connect to database
conn = sqlite3.connect('devnest.db')
cursor = conn.cursor()

print("=" * 60)
print("AI EXPLANATIONS - FULL DATA")
print("=" * 60)

cursor.execute("SELECT id, user_id, code, explanation, code_summary, topics, created_at FROM ai_explanations;")
rows = cursor.fetchall()

print(f"\nFound {len(rows)} entries:\n")

for row in rows:
    print(f"ID: {row[0]}, User: {row[1]}")
    print(f"  Code: {row[2][:50]}..." if row[2] else "  Code: None")
    print(f"  Explanation length: {len(row[3]) if row[3] else 0} characters")
    print(f"  Explanation preview: {row[3][:100]}..." if row[3] else "  Explanation: EMPTY!")
    print(f"  Summary: {row[4][:50]}..." if row[4] else "  Summary: None")
    print(f"  Topics: {row[5]}" if row[5] else "  Topics: None")
    print(f"  Date: {row[6]}")
    print()

print("=" * 60)

conn.close()