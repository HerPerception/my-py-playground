def print_file_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        split_content = content.split("\n")
        for idx in range(len(split_content)):
            line = split_content[idx]
            if line[:3] == "def":
                print(f"{idx+1:>3}: {line}")

print_file_content("./src/ailab/check_env.py")
