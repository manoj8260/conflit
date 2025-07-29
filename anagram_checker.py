def check_anagram(str1, str2):
    """
    Check if two strings are anagrams without using predefined functions.
    Returns True if they are anagrams, False otherwise.
    """
    # Convert to lowercase for case-insensitive comparison
    str1_lower = ""
    str2_lower = ""
    
    # Manual conversion to lowercase
    for char in str1:
        if 'A' <= char <= 'Z':
            str1_lower += chr(ord(char) + 32)
        else:
            str1_lower += char
    
    for char in str2:
        if 'A' <= char <= 'Z':
            str2_lower += chr(ord(char) + 32)
        else:
            str2_lower += char
    
    # Remove spaces manually
    str1_clean = ""
    str2_clean = ""
    
    for char in str1_lower:
        if char != ' ':
            str1_clean += char
    
    for char in str2_lower:
        if char != ' ':
            str2_clean += char
    
    # Check if lengths are different
    len1 = 0
    len2 = 0
    
    for _ in str1_clean:
        len1 += 1
    
    for _ in str2_clean:
        len2 += 1
    
    if len1 != len2:
        return False
    
    # Count frequency of each character manually
    # Create character frequency arrays
    freq1 = {}
    freq2 = {}
    
    # Count characters in first string
    for char in str1_clean:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1
    
    # Count characters in second string
    for char in str2_clean:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1
    
    # Compare frequencies
    # Check if all characters in freq1 exist in freq2 with same count
    for char in freq1:
        if char not in freq2 or freq1[char] != freq2[char]:
            return False
    
    # Check if all characters in freq2 exist in freq1 with same count
    for char in freq2:
        if char not in freq1 or freq2[char] != freq1[char]:
            return False
    
    return True


def get_string_length(s):
    """Get length of string without using len() function"""
    count = 0
    for _ in s:
        count += 1
    return count


def to_lowercase_manual(s):
    """Convert string to lowercase without using lower() function"""
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result


def remove_spaces_manual(s):
    """Remove spaces from string without using replace() function"""
    result = ""
    for char in s:
        if char != ' ':
            result += char
    return result


def main():
    """Main function to test the anagram checker"""
    print("=== Anagram Checker Program ===")
    print("(Without using predefined functions like sorted(), count(), etc.)")
    print()
    
    # Test cases
    test_cases = [
        ("listen", "silent"),
        ("elbow", "below"),
        ("study", "dusty"),
        ("night", "thing"),
        ("act", "cat"),
        ("evil", "vile"),
        ("a gentleman", "elegant man"),
        ("conversation", "voices rant on"),
        ("hello", "world"),
        ("python", "java"),
        ("anagram", "nag a ram"),
        ("The Eyes", "They See")
    ]
    
    print("Testing predefined cases:")
    print("-" * 50)
    
    for i in range(get_string_length(test_cases)):
        str1, str2 = test_cases[i]
        result = check_anagram(str1, str2)
        status = "✓ ANAGRAM" if result else "✗ NOT ANAGRAM"
        print(f"'{str1}' & '{str2}' -> {status}")
    
    print()
    print("-" * 50)
    print("Interactive Mode:")
    
    while True:
        print("\nEnter two strings to check if they are anagrams:")
        print("(Press Enter without input to exit)")
        
        str1 = input("Enter first string: ")
        if str1 == "":
            break
            
        str2 = input("Enter second string: ")
        if str2 == "":
            break
        
        result = check_anagram(str1, str2)
        
        if result:
            print(f"✓ '{str1}' and '{str2}' are ANAGRAMS!")
        else:
            print(f"✗ '{str1}' and '{str2}' are NOT anagrams.")
        
        print()


if __name__ == "__main__":
    main()