pool_volume = int(input())
first_pipe_flow = int(input())
second_pipe_flow = int(input())
worker_absent_hours = float(input())

first_pipe_filled = first_pipe_flow * worker_absent_hours
second_pipe_filled = second_pipe_flow * worker_absent_hours
total_filled = first_pipe_filled + second_pipe_filled


if total_filled <= pool_volume:
    print(f"The pool is {total_filled / pool_volume * 100:.2f}% full. "
          f"Pipe 1: {first_pipe_filled / total_filled * 100:.2f}%. "
          f"Pipe 2: {second_pipe_filled / total_filled * 100:.2f}%.")
else:
    print(f"For {worker_absent_hours} hours the pool overflows with {total_filled - pool_volume} liters.")