# dblmapi.py

import re

def invert_bytes(content):
    byte_array = bytearray(content)
    for i in range(len(byte_array)):
        byte_array[i] = ~byte_array[i] & 0xFF
    inverted_content = bytes(byte_array)
    return inverted_content

def process_file(content):
    # Invert the bytes of the file content
    inverted_content = invert_bytes(content)

    try:
        # Convert bytes to a string to perform replacements
        file_str = inverted_content.decode("utf-8", errors="replace")

        # Use regex to find the substring between "characterShards_": [ and ],
        match = re.search(r'"characterShards_": \[.*?\],', file_str, re.DOTALL)
        if match:
            # Extract the matched substring
            substring = match.group()

            # Use regex to find and replace values between 100 and 9999 that are preceded by "count":
            def replace_count(match):
                value = int(match.group(1))
                return f'{9999 if 100 <= value <= 9999 else value}'

            pattern = r'(?<="count":\s)(\d+)'
            processed_substring = re.sub(pattern, replace_count, substring)

            # Replace the original substring with the processed substring in the file content
            processed_content = file_str.replace(substring, processed_substring)
        else:
            raise ValueError("No 'characterShards_' found in the file.")

        # Convert the modified string back to bytes
        processed_content = processed_content.encode("utf-8", errors="replace")

        # Invert the bytes again
        processed_content = invert_bytes(processed_content)

        return processed_content
    except UnicodeDecodeError:
        raise ValueError("File content is not valid UTF-8 format.")

def zenkai_file(content):
    # Invert the bytes of the file content
    inverted_content = invert_bytes(content)

    try:
        # Convert bytes to a string to perform replacements
        file_str = inverted_content.decode("utf-8", errors="replace")

        # Use regex to find the substring between "characterPlentyShards_": [ and ],
        match = re.search(r'"characterPlentyShards_": \[.*?\],', file_str, re.DOTALL)
        if match:
            # Extract the matched substring
            substring = match.group()

            # Use regex to find and replace values between 100 and 9999 that are preceded by "count":
            def replace_count(match):
                value = int(match.group(1))
                return f'{7000 if 0 <= value <= 7000 else value}'

            pattern = r'(?<="count":\s)(\d+)'
            processed_substring = re.sub(pattern, replace_count, substring)

            # Replace the original substring with the processed substring in the file content
            processed_content = file_str.replace(substring, processed_substring)
        else:
            raise ValueError("No 'characterShards_' found in the file.")

        # Convert the modified string back to bytes
        processed_content = processed_content.encode("utf-8", errors="replace")

        # Invert the bytes again
        processed_content = invert_bytes(processed_content)

        return processed_content
    except UnicodeDecodeError:
        raise ValueError("File content is not valid UTF-8 format.")
