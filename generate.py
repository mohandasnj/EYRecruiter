from faker import Faker
from faker.providers import BaseProvider, DynamicProvider

import random

skills_provider = DynamicProvider(
    provider_name="skills",
    elements=[""]
)

service_line_provider = DynamicProvider(
    provider_name="service_line",
    elements=["Assurance", "Tax", "Consulting", "Strategy"]
)

class sub_service_line_provider(BaseProvider):
    def sub_service_line(self, service_line: str) -> str:
        if service_line == "Assurance":
            return random.choice(["Audit", "CCaSS", "FAAS", "Forensic & Integrity Services"])
        elif service_line == "Tax":
            return random.choice(["Indirect Tax", "Business Tax", "Global Compliance and Reporting", "International Tax and Transaction Services", "People Advisory Services", "Tax Technology & Transformation"])
        elif service_line == "Consulting":
            return random.choice(["Business Consulting", "Technology Consulting", "People Advisory Services"])
        elif service_line == "Strategy":
            return random.choice(["Transactions and Corporate Finance", "Parthenon", "International Tax and Transaction Services"])

class competency_provider(BaseProvider):
    def competency(self, competency: str) -> str:
        if competency == "Business Consulting":
            return random.choice(["Business Transformation", "Enterprise Risk", "Finance", "Financial Services Risk", "Supply Chain & Operations", "Technology Risk"])
        elif competency == "Technology Consulting":
            return random.choice(["Cybersecurity", "Data & Analytics", "Digital & Emerging Technology", "Technology Solution Delivery", "Technology Transformation"])
        elif competency == "People Advisory Services":
            return random.choice(["Workforce Advisory", "Integrated Mobile Talent"])
     
fake = Faker()

fake.add_provider(skills_provider)
fake.add_provider(service_line_provider)
fake.add_provider(sub_service_line_provider)
fake.add_provider(competency_provider)

name = fake.name(),


service_line = fake.service_line()
sub_service_line = fake.sub_service_line(service_line)

out = {
    "name": name[0],
    "number": fake.phone_number(),
    "email": '.'.join(name[0].split()).lower() + "@email.com",
    "location": fake.city(),
    "language": fake.language_name(),
    "skills": fake.skills(),
    "service_line": service_line,
    "sub_service_line": sub_service_line,
}

if service_line == "Consulting":
    out["competency"] = fake.competency(sub_service_line)

print(out)