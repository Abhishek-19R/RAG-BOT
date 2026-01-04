import requests
from bs4 import BeautifulSoup

URLS = {
    "CSE": "https://pragati.ac.in/computer-science-engineering/about-cse-department/staff/",
    "ECE": "https://pragati.ac.in/electronics-communication-engineering/staff/",
    "EEE": "https://pragati.ac.in/electrical-electronics-engineering/about-eee-department/staff/",
    "MECH": "https://pragati.ac.in/mechanical-engineering/staff/",
    "CIVIL": "https://pragati.ac.in/civil-engineering/staff/",
    "AIML": "https://pragati.ac.in/cse-artificial-intelligence-machine-learning/staff/",
   "DS":  "https://pragati.ac.in/cse-data-science/staff/",
   "AI":  "https://pragati.ac.in/cse-artificial-intelligence/staff/",
   "CS":  "https://pragati.ac.in/cse-cyber-security/staff/",

}

output = []

for dept, url in URLS.items():
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    output.append(f"\n==============================")
    output.append(f"Department of {dept}")
    output.append(f"==============================\n")

    # for tag in soup.find_all(["h3", "h4", "p", "li"]):
    #     text = tag.get_text(strip=True)
    #     if any(x in text.lower() for x in ["professor", "hod", "assistant", "associate", "dr."]):
    #         output.append(text)
    tables = soup.find_all("table")
    for table in tables:
        for row in table.find_all("tr"):
            cells = row.find_all(["td", "th"])
            text = " ".join(c.get_text(strip=True) for c in cells)
            if any(x in text.lower() for x in ["professor", "hod", "assistant", "associate", "dr"]):
                output.append(text)
    # 2️⃣ Extract strong / bold names (backup)
    for tag in soup.find_all(["strong", "b"]):
        text = tag.get_text(strip=True)
        if "dr" in text.lower():
            output.append(text) 

with open("data/faculty.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print("✅ faculty.txt generated with REAL website data")