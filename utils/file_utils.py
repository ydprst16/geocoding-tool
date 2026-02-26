import os
# ===============================
# AUTO INCREMENT OUTPUT FILE
# ===============================
def get_next_output_filename(base_path):
    folder = os.path.dirname(base_path)
    os.makedirs(folder, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(base_path))[0]
    ext = os.path.splitext(base_path)[1]

    i = 1
    while True:
        new_name = f"{base_name}_{i:03d}{ext}"
        full_path = os.path.join(folder, new_name)

        if not os.path.exists(full_path):
            return full_path

        i += 1