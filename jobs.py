import json

jobs = [
    {"title": "AI Engineer", "company": "Acme", "salary": 60000, "remote": True},
    {"title": "OutSystems Developer", "company": "Beta", "salary": 48000, "remote": True},
    {"title": "Backend Developer", "company": "Gamma", "salary": 52000, "remote": False}
]

def filter_by_salary(jobs: list[dict], minimum: int) -> list[dict]:
    result = []
    for job in jobs:
        if job["salary"] >= minimum:
            result.append(job)
    return result

def filter_remote(jobs: list[dict]) -> list[dict]:
    result = []
    for job in jobs:
        if job["remote"] == True:
            result.append(job)
    return result

good_jobs = filter_by_salary(jobs, 50000)
good_jobs = filter_remote(good_jobs)

""" # 1. Yours: reuse the variable, one step per line
good_jobs = filter_by_salary(jobs, 50000)
good_jobs = filter_remote(good_jobs)

# 2. Separate names, so each step stays inspectable
well_paid = filter_by_salary(jobs, 50000)
good_jobs = filter_remote(well_paid)

# 3. Nested: the inner call runs first
good_jobs = filter_remote(filter_by_salary(jobs, 50000)) """

with open("good_jobs.json", "w") as file:
    json.dump(good_jobs, file, indent=2)

with open("good_jobs.json", "r") as file:
    loaded = json.load(file)

for job in loaded:
    print(f"{job['title']} at {job['company']}: {job['salary']}")