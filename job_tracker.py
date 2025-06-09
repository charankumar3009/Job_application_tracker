import csv
from datetime import datetime

class Job:
    def __init__(self, company, role, status="Applied"):
        self.company = company
        self.role = role
        self.status = status
        self.date = datetime.today().strftime('%Y-%m-%d')

    def to_list(self):
        return [self.company, self.role, self.status, self.date]

class JobTracker:
    def __init__(self, filename="job_data.csv"):
        self.filename = filename

    def add_job(self, job):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(job.to_list())

    def view_jobs(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.reader(file)
                print("\nCompany | Role | Status | Date Applied")
                print("---------------------------------------")
                for row in reader:
                    print(" | ".join(row))
        except FileNotFoundError:
            print("No job data found. Add some jobs first.")