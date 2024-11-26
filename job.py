def job_scheduling(jobs, m):
    jobs.sort(reverse=True) 
    machines = [0] * m  
    assignment = [] 
    for job in jobs:
        min_machine = min(range(m), key=lambda x: machines[x])
        machines[min_machine] += job  
        assignment.append(min_machine + 1)
    return assignment, machines  
jobs = [10, 20, 30, 40, 50, 60]
machines = 3  
assignment, times = job_scheduling(jobs, machines)
for i, job in enumerate(jobs):
    print(f"Job {i + 1} (Duration: {job}) is assigned to Machine {assignment[i]}")
print("\nTotal time (Makespan) on each machine:", times)
