import os

# Définition des versions du README
readme_fr = """# 👋 Bonjour, je suis Benjamin !

Bienvenue sur mon profil GitHub ! En tant qu'étudiant à l'école 42, je suis passionné par le développement logiciel et je m'efforce de créer des solutions innovantes et efficaces.

## 🚀 Technologies Utilisées

![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Shell](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

## 📌 Projets en Avant

- [**Libft**](https://github.com/youllbesorry/libft)  
  Une bibliothèque personnalisée en C recréant des fonctions standard de la libc, servant de base pour d'autres projets du cursus 42.

- [**ft_printf**](https://github.com/youllbesorry/ft_printf)  
  Réimplémentation de la fonction printf en C, démontrant des compétences en gestion de sorties formatées et en manipulation de fonctions variadiques.

- [**minishell**](https://github.com/youllbesorry/minishell)  
  Création d'un shell minimaliste capable d'exécuter des commandes simples, mettant en avant la gestion des processus et des signaux en C.

- [**Philosophers**](https://github.com/youllbesorry/Philo)  
  Implémentation du problème classique des philosophes mangeurs, illustrant la gestion des threads et des mutex en C.

- [**cub3D**](https://github.com/youllbesorry/XenoCube)  
  Un moteur de jeu 3D simple utilisant la bibliothèque MiniLibX, inspiré de Wolfenstein 3D, mettant en avant le raycasting et la gestion graphique en C.

- [**IRC Server**](https://github.com/youllbesorry/FT_IRCheat)  
  Implémentation d'un serveur IRC conforme au protocole RFC 1459. Ce projet met en avant la gestion des sockets, la communication réseau en C++ et la mise en place d'un serveur multi-clients capable de gérer les salons de discussion, les commandes utilisateur et l'authentification.

- [**ft_transcendence**](https://github.com/TheTerror-coder/ft_transcendance)  
  Développement d'une application web complète en utilisant NestJS, TypeScript et d'autres technologies modernes, démontrant des compétences en développement full-stack.

## 📊 Statistiques GitHub

![Statistiques GitHub](https://github-readme-stats.vercel.app/api?username=youllbesorry&show_icons=true&theme=tokyonight)

![Langages les Plus Utilisés](https://github-readme-stats.vercel.app/api/top-langs/?username=youllbesorry&layout=compact&theme=tokyonight)

---

💬 N'hésitez pas à explorer mes dépôts !

[🇬🇧 Read this in English](README_EN.md)
"""

readme_en = """# 👋 Hello, I'm Benjamin!

Welcome to my GitHub profile! As a student at 42 School, I'm passionate about software development and strive to create innovative and efficient solutions.

## 🚀 Technologies Used

![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Shell](https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

## 📌 Featured Projects

- [**Libft**](https://github.com/youllbesorry/libft)  
  A custom C library that recreates standard libc functions, serving as a foundation for other 42 projects.

- [**ft_printf**](https://github.com/youllbesorry/ft_printf)  
  Reimplementation of the `printf` function in C, showcasing skills in formatted output handling and variadic functions.

- [**minishell**](https://github.com/youllbesorry/minishell)  
  A minimalist shell capable of executing simple commands, highlighting process management and signal handling in C.

- [**Philosophers**](https://github.com/youllbesorry/Philo)  
  Implementation of the classic dining philosophers problem, demonstrating thread and mutex management in C.

- [**cub3D**](https://github.com/youllbesorry/XenoCube)  
  A simple 3D game engine using the MiniLibX library, inspired by Wolfenstein 3D, focusing on raycasting and graphics handling in C.

- [**IRC Server**](https://github.com/youllbesorry/FT_IRCheat)  
  Implementation of an IRC server following the RFC 1459 protocol. This project emphasizes socket management, network communication in C++, and setting up a multi-client server handling chat rooms, user commands, and authentication.

- [**ft_transcendence**](https://github.com/TheTerror-coder/ft_transcendance)  
  Development of a full-stack web application using NestJS, TypeScript, and modern technologies, showcasing full-stack development skills.

## 📊 GitHub Stats

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=youllbesorry&show_icons=true&theme=tokyonight)

![Most Used Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=youllbesorry&layout=compact&theme=tokyonight)

---

💬 Feel free to explore my repositories !

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
