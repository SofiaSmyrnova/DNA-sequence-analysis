def load_file_safely(filename: str, file_type: str) -> list:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        print(f"Loaded {filename}: {len(lines)} lines")
        return lines
    except FileNotFoundError:
        print(f"Warning: {filename} was not found. {file_type} will be empty.")
        return []
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []
