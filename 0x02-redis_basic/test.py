from exercise import Cache

# Testing the Cache class with various data types
def test_cache():
    cache = Cache()

    TEST_CASES = {
        b"foo": None,  # No conversion
        123: int,  # Convert to integer
        "bar": lambda d: d.decode("utf-8")  # Convert to UTF-8 string
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)  # Store the value in Redis
        retrieved_value = cache.get(key, fn=fn)  # Retrieve the value with fn
        assert retrieved_value == value, f"Test failed for value {value}. Got {retrieved_value} instead."
        print(f"Test passed for value: {value}")

if __name__ == "__main__":
    test_cache()
