import os

# Définition des versions du README
readme_fr = """# 👋 Bonjour, je suis Benjamin ! 🇫🇷  

Bienvenue sur mon profil GitHub ! En tant qu'étudiant à l'école 42, je suis passionné par le développement logiciel et je m'efforce de créer des solutions innovantes et efficaces.  

## 🚀 Technologies Utilisées  
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=white)  
...

[🇬🇧 Voir en anglais](README_EN.md)
"""

readme_en = """# 👋 Hello, I'm Benjamin! 🇬🇧  

Welcome to my GitHub profile! As a student at 42 School, I'm passionate about software development and strive to create innovative and efficient solutions.  

## 🚀 Technologies Used  
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=white)  
...

[🇫🇷 Voir en français](README.md)
"""

# Vérifier la langue choisie
lang = os.getenv("README_LANG", "fr")  # Par défaut, français
if lang == "en":
    content = readme_en
    filename = "README_EN.md"
else:
    content = readme_fr
    filename = "README.md"

# Écrire dans le fichier correspondant
with open(filename, "w", encoding="utf-8") as f:
    f.write(content)
