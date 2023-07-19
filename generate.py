from faker import Faker
from faker.providers import BaseProvider, DynamicProvider

import json
import random


skills_file = open("technical_skills.txt")
skills_lines = skills_file.readlines()
f = open("universities.json")
universities = json.load(f)

# skills_provider = DynamicProvider(
#     provider_name="skills",
#     elements=[""]
# )

service_line_provider = DynamicProvider(
    provider_name="service_line",
    elements=["Assurance", "Tax", "Consulting", "Strategy"]
)

personal_interests_provider = DynamicProvider(
    provider_name="personal_interests",
    elements=["Acrobatics", "Acting", "Animals", "Animation", "Aquariums", "Archery", "Architecture", "Astronomy", "Baking", "Beekeeping", "Birdwatching", "Board Games", "Bonsai", "Botany", "Bowling", "Boxing", "Calligraphy", "Camping", "Canoeing", "Chalk Art", "Cheesemaking", "Chess", "Citizen Science", "Coin Collecting", "Collecting", "Comedy", "Comic Books", "Computing & Coding", "Confectionery", "Cooking", "Cosplay", "Crafts", "Creative Writing", "Cultural Activities", "Cycling", "Cosmetics", "Fashion", "DJing", "Dance", "Darts", "Design", "Digital Art", "Drawing", "Electronics", "Embroidery", "Environment", "Fandom", "Farming", "Fashion Design", "Festivals", "Filmmaking", "Fishing", "Fitness", "Floral Design", "Flying", "Game Mods", "Gardening", "Go", "Hiking", "Home Improvement", "Homebrewing", "Horseback Riding", "Improv", "Inline Skating", "Journaling", "Juggling", "Karaoke", "Kayaking", "Kite Flying", "Knitting", "Knowledge Games", "Languages", "Learning", "Magic", "Maker Culture", "Makeup", "Martial Arts", "Media Production", "Metal Detecting", "Metalworking", "Model Building", "Motor Sports", "Mountain Biking", "Music", "Nail Art", "Origami", "Paintball", "Painting", "Photography", "Podcasting", "Pool", "Pottery", "Puzzles", "Quilting", "Reading", "Remote Control Vehicles", "Reuse & Repair", "Robotics", "Rock Climbing", "Roller Skating", "Running", "Sailing & Boating", "Scouting", "Scrapbooking", "Scuba Diving", "Sculpting", "Sewing", "Singing", "Skating", "Skiing & Snowboarding", "Skydiving", "Slow Culture", "Snowshoeing", "Sports", "Stamp Collecting", "Street Art", "Street Fashion", "Subculture", "Surfing & Bodyboarding", "Swimming", "Tactical Urbanism", "Tennis", "Trainspotting", "Travel", "Vegetable Gardening", "Video Games", "Video Production", "Weightlifting", "Winemaking", "Woodworking", "Word Games", "Yoga", "Zumba"]
)

class competency_provider(BaseProvider):
    def competency(self, service_line: str) -> str:
        if service_line == "Assurance":
            return random.choice(["Audit", "CCaSS", "FAAS", "Forensic & Integrity Services"])
        elif service_line == "Tax":
            return random.choice(["Indirect Tax", "Business Tax", "Global Compliance and Reporting", "International Tax and Transaction Services", "People Advisory Services", "Tax Technology & Transformation"])
        elif service_line == "Consulting":
            return random.choice(["Business Consulting", "Technology Consulting", "People Advisory Services"])
        elif service_line == "Strategy":
            return random.choice(["Transactions and Corporate Finance", "Parthenon", "International Tax and Transaction Services"])

class sub_competency_provider(BaseProvider):
    def sub_competency(self, competency: str) -> str:
        if competency == "Business Consulting":
            return random.choice(["Business Transformation", "Enterprise Risk", "Finance", "Financial Services Risk", "Supply Chain & Operations", "Technology Risk"])
        elif competency == "Technology Consulting":
            return random.choice(["Cybersecurity", "Data & Analytics", "Digital & Emerging Technology", "Technology Solution Delivery", "Technology Transformation"])
        elif competency == "People Advisory Services":
            return random.choice(["Workforce Advisory", "Integrated Mobile Talent"])

class education_provider(BaseProvider):
    def education(self):
        return random.choice(universities)["institution"]

fake = Faker()

# fake.add_provider(skills_provider)
fake.add_provider(service_line_provider)
fake.add_provider(competency_provider)
fake.add_provider(sub_competency_provider)
fake.add_provider(personal_interests_provider)
fake.add_provider(education_provider)

out = []
colleagues = []
names = []

for _ in range(10):
    name = fake.name()
    names.append(name)
    service_line = fake.service_line()
    competency = fake.competency(service_line)
    personal_interests = []
    for i in range(random.randrange(3, 6)):
        personal_interests.append(fake.personal_interests())
    skills = []
    for i in range(random.randrange(2,5)):
        skills.append(random.choice(skills_lines).strip())
    

    person = {
        "name": name,
        "number": fake.phone_number(),
        "email": '.'.join(name.split()).lower() + "@email.com",
        "location": fake.city(),
        "education": fake.education(),    
        "language": fake.language_name(),
        "skills": skills,
        "service_line": service_line,
        "competency": competency,
        "personal_interests": personal_interests,
        "people_worked_with": colleagues
    }

    if service_line == "Consulting":
        person["sub_competency"] = fake.sub_competency(competency)

    out.append(person)

for person in out:
    for i in range(random.randrange(10)):
        n = random.choice(names)
        if n not in colleagues:
            colleagues.append(n)
    person["people_worked_with"] = colleagues
    colleagues = []

    person_string = (f'I am {person["name"]}, with email {person["email"]} and phone number {person["number"]}, ' 
    f'educated at {person["education"]}, and from {person["location"]}. I speak the language {person["language"]}. ' 
    f'I work in the {person["service_line"]} service line, in the {person["competency"]} competency. ' 
    f'{"" if person["service_line"] != "Consulting" else "I am also in the " + str(person["sub_competency"]) + " subpractice."}'
    f'My skills are {",".join(person["skills"])}, and my personal interests are {",".join(person["personal_interests"])}. '
    f'During my time at EY, I\'ve worked with {",".join(person["people_worked_with"])}.')

    person["person_string"] = person_string



with open("people.json", "w") as f:
    json.dump(out, f)