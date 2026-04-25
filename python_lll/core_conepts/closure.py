import functools

def retry(max_attempts=3):                                          # Layer 1: The factory
    def decorator(func):                                            # Layer 2: The Decorator

        @functools.wraps(func)                                      # Metadata preservation 
        def wrapper(*args, **kwargs):                               # Layer 3: The wrapper
            for attempt in range(1, max_attempts+1):
                try:
                    return func(*args, **kwargs)                    # Target execution
                except Exception as e:
                    if attempt == max_attempts:
                        raise e
                    print(f"Retrying... ({attempt}/{max_attempts})")

        return wrapper   # Return layer 3
    return decorator     # Return layer 2 
                    