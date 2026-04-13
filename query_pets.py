import sqlite3

conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

while True:
    user_input = input("Enter a person ID (-1 to exit): ")

    if user_input == "-1":
        break

    cursor.execute("SELECT * FROM person WHERE id=?", (user_input,))
    person = cursor.fetchone()

    if person:
        print(f"{person[1]} {person[2]}, {person[3]} years old")

        cursor.execute("""
        SELECT pet.name, pet.breed, pet.age
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id=?
        """, (user_input,))

        pets = cursor.fetchall()

        for pet in pets:
            print(f"Owns {pet[0]}, a {pet[1]}, {pet[2]} years old")
    else:
        print("Person not found.")

conn.close()
