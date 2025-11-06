import csv
import random

# --- Configuration ---
FILENAME = 'dragonball_characters.csv'
NUM_ROWS = 2000  # <--- Make this as big as you want!
# ---------------------

print(f"Generating {FILENAME} with {NUM_ROWS} characters...")

# Data pools for plausible-looking data
names = ['Goku', 'Vegeta', 'Gohan', 'Piccolo', 'Trunks', 'Krillin', 'Bulma', 'Frieza', 'Cell', 'Majin Buu', 'Tien', 'Yamcha', 'Android 18', 'Android 17', 'Goten', 'Jiren', 'Beerus', 'Whis', 'Broly', 'Raditz', 'Nappa', 'Bardock']
races = ['Saiyan', 'Human', 'Namekian', 'Frieza Race', 'Android', 'Majin', 'God', 'Angel', 'Hybrid']
sagas = ['Saiyan Saga', 'Frieza Saga', 'Cell Saga', 'Buu Saga', 'Battle of Gods', 'Tournament of Power', 'Broly Movie']
alignments = ['Hero', 'Villain', 'Neutral', 'Anti-Hero']

# Define the headers
headers = ['CharacterID', 'Name', 'Race', 'Saga', 'BasePowerLevel', 'MaxPowerLevel', 'Age', 'Alignment', 'HasKiControl']

# Function to get saga-appropriate power levels
def get_power_levels(saga):
    if saga == 'Saiyan Saga':
        base = random.randint(100, 18000)
    elif saga == 'Frieza Saga':
        base = random.randint(5000, 530000)
    elif saga == 'Cell Saga':
        base = random.randint(100000, 5000000)
    elif saga == 'Buu Saga':
        base = random.randint(5000000, 90000000)
    else:
        base = random.randint(10000000, 1000000000)
    
    # Max power is some multiplier of base
    max_power = base * random.uniform(1.5, 50) # Transformations
    
    # Add some "scouter-breaking" numbers for fun
    if random.random() < 0.02: # 2% chance
        max_power = 9001
        
    return int(base), int(max_power)

# Open the file and write the data
with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Write the header row
    writer.writerow(headers)
    
    # Generate and write the rows
    for i in range(1, NUM_ROWS + 1):
        char_id = 20000 + i
        name = random.choice(names)
        race = random.choice(races)
        saga = random.choice(sagas)
        alignment = random.choice(alignments)
        
        # Make data slightly more realistic
        if name in ['Goku', 'Vegeta', 'Gohan', 'Trunks', 'Goten', 'Broly', 'Raditz', 'Nappa', 'Bardock']:
            race = random.choice(['Saiyan', 'Hybrid'])
        if name == 'Piccolo':
            race = 'Namekian'
        if name == 'Frieza':
            race = 'Frieza Race'
        if name in ['Krillin', 'Bulma', 'Tien', 'Yamcha']:
            race = 'Human'
            
        base_power, max_power = get_power_levels(saga)
        
        # Age is very inconsistent in DB, so just a random number
        age = random.randint(5, 1000) 
        
        # Create a boolean feature for ML practice
        has_ki_control = random.choice([True, False])
        
        writer.writerow([char_id, name, race, saga, base_power, max_power, age, alignment, has_ki_control])

print(f"Successfully created {FILENAME}!")