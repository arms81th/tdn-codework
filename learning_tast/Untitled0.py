def generate_message():
    """Generate 'i love python' message from character combinations"""
    words = ["learn", "about", "string", "variable", "in", "python"]

    # i + l + o + v + e + u = "iloveu" which means "i love python"
    return (
        words[2][3] + words[0][0] + words[1][2] +
        words[3][0] + words[3][-1] + words[1][-2]
    )

if __name__ == "__main__":
    print(f"Secret message: {generate_message()}")
    print("Decoded: i love python")
