from job_tracker import Job, JobTracker

tracker = JobTracker()

while True:
    print("\n1. Add Job\n2. View Jobs\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        company = input("Company Name: ")
        role = input("Role: ")
        job = Job(company, role)
        tracker.add_job(job)
        print("Job added.")
    
    elif choice == "2":
        tracker.view_jobs()
    
    elif choice == "3":
        break