import spacy
import json

def extract_query_info(query):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(query)
    print(f"{doc = }")
    # Initialize variables to store extracted information
    designation = None
    skills = None

    # Extract entities
    for ent in doc.ents:
        print(f"{ent.label_ = }")
        if ent.label_ == "DESIGNATION":
            designation = ent.text
        elif ent.label_ == "SKILLS":
            skills = ent.text
    print(f"Designation: {designation} \n Skills: {skills}")
    return designation, skills

def recommend_employees(query, data):
    designation, skills = extract_query_info(query)

    if designation and skills:
        # Filtering employees based on the provided designation and skills
        recommended_employees = []
        for employee in data:
            if (
                designation.lower() in employee["designation"].lower()
                and skills.lower() in employee["experience_skills"]
            ):
                recommended_employees.append({
                    "name": f"{employee['first_name']} {employee['last_name']}",
                    "currently_assigned": employee["currently_assigned"]
                })

        return recommended_employees
    else:
        return None

if __name__ == "__main__":
    # Load synthetic data from the provided JSON
    with open("synthetic_data.json", "r") as file:
        synthetic_data = json.load(file)

    # Example Query
    user_query = "Recommend good employees for a Data Scientist project using Python."
    # user_query = input("query:-")
    # Get recommended employees based on the query
    recommended_employees = recommend_employees(user_query, synthetic_data)

    # Print the recommended employees
    if recommended_employees:
        print("System:", "Based on your query, here are the top recommended employees:")
        for idx, employee in enumerate(recommended_employees, start=1):
            print(f"{idx}. {employee['name']} - {'Free' if not employee['currently_assigned'] else 'Occupied'}")
    else:
        print("System:", "Unable to extract relevant information from the query.")
