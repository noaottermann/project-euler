import time


def solve():
    raise NotImplementedError("Override solve() to return the problem answer.")


def run(solve_fn=solve, problem_id=None):
    start = time.perf_counter()
    result = solve_fn()
    elapsed = time.perf_counter() - start
    label = f"Problem {problem_id}" if problem_id is not None else "Result"
    print(f"{label}: {result} (time: {elapsed:.6f}s)")
    return result, elapsed