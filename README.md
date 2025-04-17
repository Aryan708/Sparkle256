# Sparkle256
Lightweight implementation of SPARKLE-256 permutation for IoT/constrained environments
## Features
- Pure Python implementation
- 256-bit security level
- Efficient ARX operations
## Usage
``
from sparkle256 import Sparkle256

# Initialize state
state = * 8  # 256-bit state

# Apply permutation
result = Sparkle256.sparkle(state)

# Generate hash
print(''.join(f"{word:08x}" for word in result))
