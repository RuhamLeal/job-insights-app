from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs = read(path)
    salaries = set()

    for job in jobs:
        if job["max_salary"].isnumeric():
            salaries.add(int(job["max_salary"]))

    highest_salary = max(salaries)

    return highest_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)
    salaries = set()

    for job in jobs:
        if job["min_salary"].isnumeric():
            salaries.add(int(job["min_salary"]))

    lowest_salary = min(salaries)

    return lowest_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])

        if min_salary > max_salary:
            raise ValueError

        elif min_salary <= int(salary) <= max_salary:
            return True

        return False
    except (Exception):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs = []

    for job in jobs:
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]

        try:
            salary_range = dict(max_salary=max_salary, min_salary=min_salary)
            sucessfully_matched = matches_salary_range(salary_range, salary)

            if sucessfully_matched:
                filtered_jobs.append(job)

        except (ValueError):
            None

    return filtered_jobs
