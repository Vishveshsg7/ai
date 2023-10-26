def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(jobs, key=lambda x: x[1])[1]
    schedule = [-1] * (max_deadline + 1)

    total_profit = 0
    scheduled_jobs = []

    for job in jobs:
        job_id, deadline, profit = job
        for i in range(deadline, 0, -1):
            if schedule[i] == -1:
                schedule[i] = job_id
                total_profit += profit
                scheduled_jobs.append(job)
                break

    return total_profit, scheduled_jobs

def main():
    num_jobs = int(input("Enter the number of jobs: "))
    jobs = []
    for i in range(num_jobs):
        job_id = i + 1
        deadline = int(input(f"Enter the deadline for job {job_id}: "))
        profit = int(input(f"Enter the profit for job {job_id}: "))
        jobs.append((job_id, deadline, profit))

    max_profit, scheduled_jobs = job_scheduling(jobs)
    print("\n\nMaximum Profit:", max_profit)
    print("Scheduled Jobs:")
    for job in scheduled_jobs:
        print(f"Job {job[0]} (Deadline: {job[1]}, Profit: {job[2]})")

if __name__ == "__main__":
    main()
    4
    