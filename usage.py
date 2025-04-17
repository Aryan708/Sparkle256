from sparkle256 import Sparkle256

def hash_message(message):
    state = [0] * 8  # 256-bit state initialization
    if message:
        # Message processing logic (add your absorption phase here)
        pass
    return Sparkle256.sparkle(state)

if __name__ == "__main__":
    print("SPARKLE-256 Empty Input Hash:")
    result = hash_message(bytes())
    print(''.join(f"{word:08x}" for word in result))