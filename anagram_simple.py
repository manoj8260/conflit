def check_anagram_simple(str1, str2):
    """
    Simple anagram checker using character removal approach.
    No predefined functions used.
    """
    # Convert to lowercase manually
    s1 = ""
    s2 = ""
    
    for char in str1:
        if 'A' <= char <= 'Z':
            s1 += chr(ord(char) + 32)
        elif char != ' ':  # Skip spaces
            s1 += char
    
    for char in str2:
        if 'A' <= char <= 'Z':
            s2 += chr(ord(char) + 32)
        elif char != ' ':  # Skip spaces
            s2 += char
    
    # Check each character of s1 in s2 and remove it
    s2_copy = s2
    
    for char in s1:
        found = False
        new_s2 = ""
        
        # Look for the character in s2_copy and remove first occurrence
        for c in s2_copy:
            if c == char and not found:
                found = True  # Skip this character (remove it)
            else:
                new_s2 += c
        
        if not found:
            return False  # Character not found in s2
        
        s2_copy = new_s2
    
    # If s2_copy is empty, all characters matched
    return s2_copy == ""


def main():
    print("=== Simple Anagram Checker ===")
    print("(Using character removal approach - no predefined functions)")
    print()
    
    test_cases = [
        ("listen", "silent"),
        ("hello", "bello"),
        ("act", "cat"),
        ("evil", "vile"),
        ("anagram", "nag a ram"),
        ("The Eyes", "They See"),
        ("python", "java")
    ]
    
    for str1, str2 in test_cases:
        result = check_anagram_simple(str1, str2)
        status = "✓ ANAGRAM" if result else "✗ NOT ANAGRAM"
        print(f"'{str1}' & '{str2}' -> {status}")


if __name__ == "__main__":
    main()