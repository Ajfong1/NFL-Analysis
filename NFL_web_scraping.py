from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # Run in background
options.add_argument("--disable-gpu")

# Start driver
driver = webdriver.Chrome()

# List to hold all years' data
early_all_offense_data = []





for i in range(1998, 2000):
    url = f'https://www.pro-football-reference.com/years/{i}/'
    print(f"Scraping {url} ...")
    driver.get(url)
    time.sleep(7)

    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "#team_stats tbody .left , #team_stats tbody .right")
        #elements = driver.find_elements(By.CSS_SELECTOR, "#team_stats")
        year_data = [el.text for el in elements]

        if year_data:
            early_all_offense_data.extend(year_data)
            early_all_offense_data.append()
            print("Data saved")
        else:
            print(f"No Data found for {i}")

    except Exception as e:
        print(f"Error scraping {i}: {e}")



# Save all collected data into one file
with open("early_combined_team_offense_stats.txt", "w", encoding="utf-8") as f:
    for section in early_all_offense_data:
        f.write(section + "\n")

print("✅ Scraping complete. Data saved to 'early_combined_team_offense_stats.txt'")

all_offense_data = []



for i in range(2000, 2025):
    url = f'https://www.pro-football-reference.com/years/{i}/'
    print(f"Scraping {url} ...")
    driver.get(url)
    time.sleep(7)

    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "#team_stats tbody .left , #team_stats tbody .right")
        #elements = driver.find_elements(By.CSS_SELECTOR, "#team_stats")
        year_data = [el.text for el in elements]

        if year_data:
            all_offense_data.extend(year_data)
            all_offense_data.append()
            print("Data saved")
        else:
            print(f"No Data found for {i}")

    except Exception as e:
        print(f"Error scraping {i}: {e}")



# Save all collected data into one file
with open("late_combined_team_offense_stats.txt", "w", encoding="utf-8") as f:
    for section in all_offense_data:
        f.write(section + "\n")

print("✅ Scraping complete. Data saved to 'late_combined_team_offense_stats.txt'")


all_defense_data_early = []

for i in range(1998, 2000):
    url = f'https://www.pro-football-reference.com/years/{i}/opp.htm'
    print(f"Scraping {url} ...")
    driver.get(url)
    time.sleep(7)

    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "#team_stats tbody .left , #team_stats tbody .right")
        #elements = driver.find_elements(By.CSS_SELECTOR, "#team_stats")
        year_data = [el.text for el in elements]

        if year_data:
            all_defense_data_early.extend(year_data)
            all_defense_data_early.append()
            print("Data saved")
        else:
            print(f"No Data found for {i}")

    except Exception as e:
        print(f"Error scraping {i}: {e}")



# Save all collected data into one file
with open("early_combined_team_defense_stats.txt", "w", encoding="utf-8") as f:
    for section in all_defense_data_early:
        f.write(section + "\n")

print("✅ Scraping complete. Data saved to 'combined_team_defense_stats.txt'")

all_defense_data = []


for i in range(2000, 2025):
    url = f'https://www.pro-football-reference.com/years/{i}/opp.htm'
    print(f"Scraping {url} ...")
    driver.get(url)
    time.sleep(7)

    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "#team_stats tbody .left , #team_stats tbody .right")
        year_data = [el.text for el in elements]

        if year_data:
            all_defense_data.extend(year_data)
            all_defense_data.append()
            print("Data saved")
        else:
            print(f"No Data found for {i}")

    except Exception as e:
        print(f"Error scraping {i}: {e}")

# Save all collected data into one file
with open("late_combined_team_defense_stats.txt", "w", encoding="utf-8") as f:
    for section in all_defense_data:
        f.write(section + "\n")

print("✅ Scraping complete. Data saved to 'late_combined_team_defense_stats.txt'")

wins_losses = []


for i in range(1998, 2025):
    url = f'https://www.pro-football-reference.com/years/{i}/'
    print(f"Scraping {url} ...")
    driver.get(url)
    time.sleep(7)

    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "#AFC .right:nth-child(4) , #NFC .right:nth-child(3) , #NFC tbody th , #NFC .left+ .right , #NFC .right:nth-child(4) , #AFC .right:nth-child(3) , #AFC .left+ .right , #AFC tbody th")
        year_data = [el.text for el in elements]

        if year_data:
            wins_losses.extend(year_data)
            wins_losses.append()
            print("Data saved")
        else:
            print(f"No Data found for {i}")

    except Exception as e:
        print(f"Error scraping {i}: {e}")

# Save all collected data into one file
with open("wins_losses.txt", "w", encoding="utf-8") as f:
    for section in wins_losses:
        f.write(section + "\n")

print("✅ Scraping complete. Data saved to 'wins_losses.txt'")

ancient_defense_stats = []


for i in range(1965, 1998):
    url = f'https://www.pro-football-reference.com/years/{i}/opp.htm'
    print(f"Scraping {url} ...")
    driver.get(url)
    time.sleep(7)

    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "#team_stats tbody .left , #team_stats tbody .right")
        year_data = [el.text for el in elements]

        if year_data:
            ancient_defense_stats.extend(year_data)
            ancient_defense_stats.append()
            print("Data saved")
        else:
            print(f"No Data found for {i}")

    except Exception as e:
        print(f"Error scraping {i}: {e}")

# Save all collected data into one file
with open("ancient_defense_stats.txt", "w", encoding="utf-8") as f:
    for section in ancient_defense_stats:
        f.write(section + "\n")

print("✅ Scraping complete. Data saved to 'ancient_defense_stats.txt'")


ancient_wins_losses = []


for i in range(1970, 1998):
    url = f'https://www.pro-football-reference.com/years/{i}/'
    print(f"Scraping {url} ...")
    driver.get(url)
    time.sleep(7)

    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "#AFC .right:nth-child(4) , #NFC .right:nth-child(3) , #NFC tbody th , #NFC .left+ .right , #NFC .right:nth-child(4) , #AFC .right:nth-child(3) , #AFC .left+ .right , #AFC tbody th")
        year_data = [el.text for el in elements]

        if year_data:
            ancient_wins_losses.extend(year_data)
            ancient_wins_losses.append()
            print("Data saved")
        else:
            print(f"No Data found for {i}")

    except Exception as e:
        print(f"Error scraping {i}: {e}")

# Save all collected data into one file
with open("ancient_wins_losses.txt", "w", encoding="utf-8") as f:
    for section in ancient_wins_losses:
        f.write(section + "\n")

print("✅ Scraping complete. Data saved to 'ancient_wins_losses.txt'")

extinct_wins_losses = []


for i in range(1965, 1970):
    url = f'https://www.pro-football-reference.com/years/{i}/'
    print(f"Scraping {url} ...")
    driver.get(url)
    time.sleep(7)

    try:
        elements = driver.find_elements(By.CSS_SELECTOR, "#NFL .right:nth-child(4) , #NFL .right:nth-child(3) , #NFL .left+ .right , #NFL tbody th")
        year_data = [el.text for el in elements]

        if year_data:
            extinct_wins_losses.extend(year_data)
            extinct_wins_losses.append()
            print("Data saved")
        else:
            print(f"No Data found for {i}")

    except Exception as e:
        print(f"Error scraping {i}: {e}")

# Save all collected data into one file
with open("extinct_wins_losses.txt", "w", encoding="utf-8") as f:
    for section in extinct_wins_losses:
        f.write(section + "\n")

print("✅ Scraping complete. Data saved to 'extinct_wins_losses.txt'")

driver.quit()
