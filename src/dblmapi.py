import re
import csv

# Constants for file parts and their descriptions
FILE_PARTS_DESCRIPTIONS = {
    "characterShards_": "Character stars. Edit the count under the unit ID to 9999 for 14 stars. "
                        "\"count\": {zpowernum} is the Z Power.",
    "characterPlentyShards_": "Character Zenkai Power. Edit the count to a maximum of 7000 for Zenkai 7.",
    "equipItems_": "Equip data. You can edit the rank and other attributes.",
    "unlockItems_": "Items you have unlocked.",
    "invisibleUnlockItems_": "Unobtained items.",
    "otherItems_": "Other items.",
    "unit": "Characters' information. Edit the level, artsboost, soulboost, etc. (Level can be edited to anything).",
    "party": "Your party information. You can change the characters as long as you have them.",
    "tutorial": "Tutorial progress. Replace all the 0's with 1's if any, and the tutorial should be complete.",
    "backGroundId": "The game's background ID."
}

def generate_csv_table(filename="file_parts_description.csv"):
    """
    Generates a CSV table with file parts and their descriptions.

    This function creates a CSV file with two columns: "File Parts" and "Description". It iterates over the
    FILE_PARTS_DESCRIPTIONS dictionary and writes each key-value pair as a row in the CSV file. The resulting
    CSV file can be used as a reference for understanding the different file parts and their corresponding
    descriptions.

    Args:
        filename (str): The name of the CSV file to save. Default is "file_parts_description.csv".

    Returns:
        None
    """
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["File Parts", "Description"])
        for part, description in FILE_PARTS_DESCRIPTIONS.items():
            writer.writerow([part, description])

def invert_bytes(content):
    """
    Inverts the bytes of the input content.

    This function takes a bytes object as input and inverts each byte by performing a bitwise NOT operation
    and masking the result with 0xFF (to ensure the byte value remains within the range of 0-255). The inverted
    bytes are then returned as a new bytes object.

    Args:
        content (bytes): The content to invert.

    Returns:
        bytes: The inverted content.
    """
    byte_array = bytearray(content)
    for i in range(len(byte_array)):
        byte_array[i] = ~byte_array[i] & 0xFF
    return bytes(byte_array)

def process_file(content, part):
    """
    Processes the file content by performing specific replacements based on the part.

    This function takes a bytes object representing the file content and a string representing the part of the
    file to process. It first inverts the bytes of the content using the invert_bytes function. Then, it attempts
    to decode the inverted content as UTF-8 and searches for a specific pattern corresponding to the specified part.

    If the pattern is found, it performs replacements on the "count" values within that part based on the following
    rules:
    - For "characterShards_", if the count is between 100 and 9999, it is replaced with 9999 (14 stars).
    - For "characterPlentyShards_", if the count is between 0 and 7000, it is replaced with 7000 (Zenkai 7).
    - For other parts, the count is left unchanged.

    After the replacements, the processed content is encoded back to UTF-8, inverted again, and returned.

    Args:
        content (bytes): The content of the file.
        part (str): The part of the file to process.

    Returns:
        bytes: The processed file content.

    Raises:
        ValueError: If the specified part is not found in the file or if the file content is not valid UTF-8 format.
    """
    inverted_content = invert_bytes(content)

    try:
        file_str = inverted_content.decode("utf-8", errors="replace")
        match = re.search(fr'"{part}": \[.*?\],', file_str, re.DOTALL)
        if match:
            substring = match.group()

            def replace_count(match):
                value = int(match.group(1))
                if part == "characterShards_":
                    return f'{9999 if 100 <= value <= 9999 else value}'
                elif part == "characterPlentyShards_":
                    return f'{7000 if 0 <= value <= 7000 else value}'
                else:
                    return match.group()

            pattern = r'(?<="count":\s)(\d+)'
            processed_substring = re.sub(pattern, replace_count, substring)
            processed_content = file_str.replace(substring, processed_substring)
        else:
            raise ValueError(f"No '{part}' found in the file.")

        processed_content = processed_content.encode("utf-8", errors="replace")
        processed_content = invert_bytes(processed_content)

        return processed_content
    except UnicodeDecodeError:
        raise ValueError("File content is not valid UTF-8 format.")

# Example usage:
# generate_csv_table()
# processed_content = process_file(file_content, "characterShards_")
