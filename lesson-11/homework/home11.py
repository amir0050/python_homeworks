# === 1) Create virtual environment and install packages ===
python -m venv myenv
source myenv/bin/activate   # Linux/Mac
myenv\Scripts\activate      # Windows
pip install requests numpy pandas

# === 2) Create math_operations.py ===
cat > math_operations.py << 'EOF'
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
EOF

# === 3) Create string_utils.py ===
cat > string_utils.py << 'EOF'
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
EOF

# === 4) Create geometry package ===
mkdir -p geometry
cat > geometry/__init__.py << 'EOF'
EOF

cat > geometry/circle.py << 'EOF'
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius
EOF

# === 5) Create file_operations package ===
mkdir -p file_operations
cat > file_operations/__init__.py << 'EOF'
EOF

cat > file_operations/file_reader.py << 'EOF'
def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read()
EOF

cat > file_operations/file_writer.py << 'EOF'
def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)
EOF
