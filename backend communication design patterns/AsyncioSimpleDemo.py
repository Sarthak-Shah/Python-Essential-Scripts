import asyncio


async def greet(name, delay):
    """A coroutine that prints a greeting after a delay."""
    print(f"Starting greeting for {name}...")
    await asyncio.sleep(delay)  # Simulate an I/O operation or a long-running task
    print(f"Hello, {name}!")


async def main():
    """The main entry point for the asyncio program."""
    print("Main program started.")

    # Schedule multiple coroutines to run concurrently
    task1 = asyncio.create_task(greet("Alice", 2))
    task2 = asyncio.create_task(greet("Bob", 1))
    task3 = asyncio.create_task(greet("Charlie", 3))

    # Wait for all scheduled tasks to complete
    await asyncio.gather(task1, task2, task3)

    print("Main program finished.")


if __name__ == "__main__":
    asyncio.run(main())