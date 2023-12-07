from faker import Faker
import random
import json

fake = Faker()

def generate_fake_employee():
    designations = ["Data Scientist, Software Engineer, Front-end developer, Back-end Developer, Devops Engineer"]
    employee = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "designation": random.choice(designations),
        "experience_skills": {
            "python": round(random.uniform(0.5, 5.0), 2),
            "flask": round(random.uniform(0.5, 5.0), 2),
            "mongodb": round(random.uniform(0.5, 5.0), 2),
            "django": round(random.uniform(0.5, 5.0), 2),
            "fastAPI": round(random.uniform(0.5, 5.0), 2),
            "sql": round(random.uniform(0.5, 5.0), 2),
            "data_analysis": round(random.uniform(0.5, 5.0), 2),
            "javascript": round(random.uniform(0, 5.0), 2),
            "react": round(random.uniform(0, 5.0), 2)
        },
        "currently_assigned": random.choice([True, False])
    }
    return employee

def generate_synthetic_data(num_records):
    data = []
    for _ in range(num_records):
        data.append(generate_fake_employee())
    return data

def save_to_file(data, filename="synthetic_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    num_records = 150
    synthetic_data = generate_synthetic_data(num_records)
    save_to_file(synthetic_data)

    print(f"Synthetic data saved to 'synthetic_data.json'")
