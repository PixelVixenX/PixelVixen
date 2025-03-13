import motif
import requests
import json

API_KEY = "YOUR_API_KEY"
API_URL = "https://api.x.ai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def generate_art_description(prompt):
    payload = {
        "model": "grok-2-1212",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "temperature": 0.7
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

def motif_map(width=12, height=6):
    """Generate a 2D text map of Pixel Vixen's motifs."""
    map = [[' ' for _ in range(width)] for _ in range(height)]
    for x in range(width):
        if random.random() < 0.15:
            map[0][x] = '✸'
    for x in range(0, width, 4):
        if random.random() < 0.6:
            map[height-2][x] = '▲'
            map[height-3][x] = '|'
    for x in range(width):
        if random.random() < 0.3:
            map[height-1][x] = '✧'
        elif random.random() < 0.2:
            map[height-1][x] = '⋏'
    return '\n'.join(''.join(row) for row in map)

def main():
    print("Pixel Vixen's Motif Map (Text Representation):")
    text_art = motif_map()
    print(text_art)

    prompt = "Describe a 2D artwork with shattered glass, neon holograms, skeletal spires, and a solitary figure in muted tones."
    description = generate_art_description(prompt)
    print("\nPixel Vixen's Artistic Vision (Grok API):")
    print(description)

if __name__ == "__main__":
    main()
