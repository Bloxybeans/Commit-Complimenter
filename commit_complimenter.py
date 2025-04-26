import sys
import random
import os

# List of compliments the script can choose from
compliments = [
    "Nice job on this commit!",
    "Keep up the great work!",
    "You're a coding superstar!",
    "This commit looks awesome!",
    "Handling that like a pro!",
    "Simply brilliant!",
    "Another step towards greatness!",
    "Feeling proud of this one!",
    "You got this!",
    "Solving problems like a boss!"
]

# Keywords that might indicate a 'negative' or 'struggle' commit message
# Use lowercase for easier checking
negative_keywords = [
    "fix",
    "bug",
    "error",
    "failed",
    "broken",
    "hotfix",
    "struggling",
    "mess",
    "oops",
    "sigh",
    "ugh"
]

def main():
    # Git passes the path to the commit message file as the first argument
    if len(sys.argv) < 2:
        # Should not happen with standard Git commit process
        print("Error: No commit message file path provided.")
        sys.exit(1)

    message_filepath = sys.argv[1]

    try:
        # Read the current commit message content
        # Use 'r+' mode to read and write to the same file
        # Specify encoding for broader compatibility
        with open(message_filepath, 'r+', encoding='utf-8') as f:
            original_content = f.read()

            # Simple check for negative keywords (case-insensitive)
            should_add_compliment = any(keyword in original_content.lower() for keyword in negative_keywords)

            # Check if a compliment is already present (to avoid adding duplicates)
            # We'll use a simple marker
            if "✨ Commit Complimenter Says:" in original_content:
                 should_add_compliment = False # Already has a compliment

            if should_add_compliment:
                # Choose a random compliment
                compliment = random.choice(compliments)

                # Append the compliment with a separator
                # Use os.linesep for correct line endings on Windows
                new_content = original_content.strip() + os.linesep + os.linesep + "✨ Commit Complimenter Says: " + compliment

                # Go back to the start of the file to overwrite
                f.seek(0)
                # Write the new content
                f.write(new_content)
                # Truncate the file in case the new content is shorter than the original
                f.truncate()

    except Exception as e:
        # In case of any error, print it (it might show up in the console
        # when committing) but don't prevent the commit from happening.
        # The original message will be used.
        print(f"Commit Complimenter Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()