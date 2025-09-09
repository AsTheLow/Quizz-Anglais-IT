# Script QCM interactif Python
import random
# Liste des questions
questions = [
    {"question": "1. Quelle est la traduction de 'Infrastructure de systèmes' en anglais ?",
     "options": ["a. System infrastructure", "b. Système infrastructure", "c. Systemes infrastructure", "d. Systems infrastructure"],
     "answer": "a", "full_answer": "System infrastructure"},

    {"question": "2. A quel mot anglais correspond cette définition : 'An extortion form imposed by malicious code on a user of the system.'",
     "options": ["a. Smurf attack", "b. XSS attack", "c. Ransomware", "d. Mailbot"],
     "answer": "c", "full_answer": "Ransomware"},

    {"question": "3. Quelle est la traduction de 'Bande passante' en anglais ?",
     "options": ["a. Passing band", "b. Wide band", "c. Taping band", "d. Bandwidth"],
     "answer": "d", "full_answer": "Bandwidth"},

    {"question": "4. Quelle est la traduction de 'Être l’expert des infrastructures techniques de son SI' en anglais ?",
     "options": ["a. Be the expert on the technics for IS infrastructure",
                 "b. Expertise the IS for technical infrastructure",
                 "c. Be the expert on the technical infrastructure of your IS",
                 "d. Expertise the technical infrastructure of your IS"],
     "answer": "c", "full_answer": "Be the expert on the technical infrastructure of your IS"},

    {"question": "5. A quel mot anglais correspond cette définition : 'Any program or set of programs used to hide activity, malicious or not, on a machine.'",
     "options": ["a. Encrypted program", "b. Program spoofing", "c. XSS attack", "d. Rootkit"],
     "answer": "d", "full_answer": "Rootkit"},

    {"question": "6. Quelle est la traduction de 'Système de messagerie collaborative' en anglais ?",
     "options": ["a. Collaboration mailing system", "b. Collaborative message system", "c. Collaborative messageries system", "d. Collaborative messaging system"],
     "answer": "d", "full_answer": "Collaborative messaging system"},

    {"question": "7. Quelle est la traduction de 'Mettre à niveau les logiciels et le matériel obsolètes' en anglais ?",
     "options": ["a. Get to the level obsolete software and hardware",
                 "b. Put to level obsolete software and hardware",
                 "c. Upgrade obsolete software and hardware",
                 "d. Level up obsolete software and hardware"],
     "answer": "c", "full_answer": "Upgrade obsolete software and hardware"},

    {"question": "8. Quelle est la traduction de 'Exécuter un programme' en anglais ?",
     "options": ["a. To run a program", "b. To drive a program", "c. To execute a programm", "d. To direct a programme"],
     "answer": "a", "full_answer": "To run a program"},

    {"question": "9. Quelle est la traduction de 'Animer une équipe' en anglais ?",
     "options": ["a. Host a team", "b. Moderate a team", "c. Lead a team", "d. Anime a team"],
     "answer": "c", "full_answer": "Lead a team"},

    {"question": "10. A quel mot anglais correspond cette définition : 'Program spreading from machine to machine, through network connections and IT systems.'",
     "options": ["a. Botnet", "b. Worm", "c. Trojan horse", "d. Ping of death"],
     "answer": "b", "full_answer": "Worm"},

    {"question": "11. Quelle est la traduction de 'Nettoyage des données' en anglais ?",
     "options": ["a. Data vaccuming", "b. Data sweeping", "c. Data trashing", "d. Data cleansing"],
     "answer": "d", "full_answer": "Data cleansing"},

    {"question": "12. Quelle est la traduction de 'Parc informatique' en anglais ?",
     "options": ["a. Informatics park", "b. Computerized equipment", "c. Informatics station", "d. IT stock"],
     "answer": "d", "full_answer": "IT stock"},

    {"question": "13. Quelle est la traduction de 'Surveiller l’efficacité des systèmes informatiques' en anglais ?",
     "options": ["a. Put under surveillance IT systems effectively",
                 "b. Monitor the effectiveness of IT systems",
                 "c. Check IT systems efficacity",
                 "d. Make a survey of IT systems effectiveness"],
     "answer": "b", "full_answer": "Monitor the effectiveness of IT systems"},

    {"question": "14. Quelle est la traduction de 'Assembler de nouveaux systèmes' en anglais ?",
     "options": ["a. New systems assembled", "b. Assemble new systems", "c. Assemblate new systems", "d. New assembling systems"],
     "answer": "b", "full_answer": "Assemble new systems"},

    {"question": "15. Quelle est la traduction de 'Microprocesseur' en anglais ?",
     "options": ["a. Microship", "b. Microprocess", "c. Microchip", "d. Microprocessings"],
     "answer": "c", "full_answer": "Microchip"},

    {"question": "16. Quelle est la traduction de 'Avoir de solides compétences pour le travail en équipe' en anglais ?",
     "options": ["a. Have strong team-working skills", "b. Have solid team-skills for working", "c. Have good working-skills in a team", "d. Have strong skills for team-working"],
     "answer": "a", "full_answer": "Have strong team-working skills"},

    {"question": "17. A quel mot anglais correspond cette définition : 'Set of software techniques which automatically complete forms protected by a captcha.'",
     "options": ["a. Captcha breaking", "b. Captcha bug", "c. Captcha failure", "d. Captcha injection"],
     "answer": "a", "full_answer": "Captcha breaking"},

    {"question": "18. Quelle est la traduction de 'Ecouter, analyser et rédiger les besoins' en anglais ?",
     "options": ["a. Monitor, analyze and write needs", "b. Listen, analyze and write needs", "c. Listen, consider and print needs", "d. Hear, observe and write needs"],
     "answer": "b", "full_answer": "Listen, analyze and write needs"},

    {"question": "19. A quel mot anglais correspond cette définition : 'Inspects each package to find a user-defined type of content, such as an IP address.'",
     "options": ["a. Tracker", "b. Packet filter", "c. Package filter", "d. IP Spoofing"],
     "answer": "b", "full_answer": "Packet filter"},

    {"question": "20. A quel mot anglais correspond cette définition : 'Software or hardware used to capture what a person is typing on the keyboard.'",
     "options": ["a. Key loggers", "b. XSS attack", "c. Dictionary attack", "d. Macro-virus"],
     "answer": "a", "full_answer": "Key loggers"},

    {"question": "21. Quelle est la traduction de 'Valider, concevoir et mettre en œuvre les infrastructures systèmes et réseaux' en anglais ?",
     "options": ["a. Value, conceive and ordain systems and networks architecture",
                 "b. Validate, design and implement systems and networks infrastructure",
                 "c. Validate, conceive and put in order systems and networks infrastructure",
                 "d. Verify, design and put together systems and networks architecture"],
     "answer": "b", "full_answer": "Validate, design and implement systems and networks infrastructure"},

    {"question": "22. Quelle est la traduction de 'Définir les étapes clés de cycle de vie du projet' en anglais ?",
     "options": ["a. Define key steps of project lifecycle", "b. Set the project life cycle steps", "c. Identify project key stages", "d. Determine project life cycle"],
     "answer": "a", "full_answer": "Define key steps of project lifecycle"},

    {"question": "23. Quelle est la traduction de 'Matériel informatique' en anglais ?",
     "options": ["a. Strongware", "b. Informatics material", "c. Work material", "d. Hardware"],
     "answer": "d", "full_answer": "Hardware"},

    {"question": "24. Quelle est la traduction de 'Mener à bien les différentes évolutions du SI' en anglais ?",
     "options": ["a. Drive in a good way the various developments in IS", "b. Take away the various developments in IS",
                 "c. Carry out the various developments in IS", "d. Remove the various developments in IS"],
     "answer": "c", "full_answer": "Carry out the various developments in IS"},

    {"question": "25. A quel mot anglais correspond cette définition : 'Network of zombie PCs remotely controlled by a hacker using bots to launch mass attacks.'",
     "options": ["a. Botnet", "b. Hackerbot", "c. Bot launcher", "d. Hacker attack"],
     "answer": "a", "full_answer": "Botnet"},

    {"question": "26. Quelle est la traduction de 'Imprimante' en anglais ?",
     "options": ["a. Imprints", "b. Printing", "c. Imprinter", "d. Printer"],
     "answer": "d", "full_answer": "Printer"},

    {"question": "27. Quelle est la traduction de 'Concevoir des solutions' en anglais ?",
     "options": ["a. Review solutions", "b. Consider solutions", "c. Concrete solutions", "d. Design solutions"],
     "answer": "d", "full_answer": "Design solutions"},

    {"question": "28. Quelle est la traduction de 'Surveiller les réseaux et les systèmes informatiques' en anglais ?",
     "options": ["a. Monitorize IT networks and systems", "b. Make a survey of computer networks and systems",
                 "c. Put under surveillance networks and systems for computer", "d. Monitor computer networks and systems"],
     "answer": "d", "full_answer": "Monitor computer networks and systems"},

    {"question": "29. Quelle est la traduction de 'Mettre en œuvre les solutions aux problématiques techniques' en anglais ?",
     "options": ["a. Put in order solutions to technical problems", "b. Ordain solutions to technical problems",
                 "c. Implement solutions to technical problems", "d. Put together solutions to technical problems"],
     "answer": "c", "full_answer": "Implement solutions to technical problems"},

    {"question": "30. Quelle est la traduction de 'Sécurité des données' en anglais ?",
     "options": ["a. Data safety", "b. Data savings", "c. Data safeguard", "d. Data safeguardings"],
     "answer": "a", "full_answer": "Data safety"},

    {"question": "31. Quelle est la traduction de 'Apprentissage automatique' en anglais ?",
     "options": ["a. Automatized learning", "b. Computing learning", "c. Machine learning", "d. Automatic learning"],
     "answer": "c", "full_answer": "Machine learning"},

    {"question": "32. Quelle est la traduction de 'Accroître la performance et la réactivité de l’entreprise' en anglais ?",
     "options": ["a. Decrease the company's performance and reactivity", "b. Push up the company's performance and reactivity",
                 "c. Increase the company's performance and responsiveness", "d. Ease the company's performance and responsiveness"],
     "answer": "c", "full_answer": "Increase the company's performance and responsiveness"},

    {"question": "33. Quelle est la traduction de 'Système informatique' en anglais ?",
     "options": ["a. Computer system", "b. Computerized system", "c. Informatics system", "d. Computing system"],
     "answer": "a", "full_answer": "Computer system"},

    {"question": "34. Quelle est la traduction de 'Carte mémoire' en anglais ?",
     "options": ["a. Memory card", "b. Mesmerize card", "c. Memories card", "d. Memoir card"],
     "answer": "a", "full_answer": "Memory card"},

    {"question": "35. Quelle est la traduction de 'Logiciel' en anglais ?",
     "options": ["a. Software", "b. Logware", "c. Logicial", "d. Skillware"],
     "answer": "a", "full_answer": "Software"},

    {"question": "36. Quelle est la traduction de 'Equipement téléphonique' en anglais ?",
     "options": ["a. Phone equipment", "b. Phoning equipment", "c. Phoning infrastructure", "d. Phone ware"],
     "answer": "a", "full_answer": "Phone equipment"},

    {"question": "37. A quel mot anglais correspond cette définition : 'Hacking tool used to decode encrypted passwords'",
     "options": ["a. Hacking tool", "b. Password stealer", "c. Decryption", "d. Crack"],
     "answer": "d", "full_answer": "Crack"},

    {"question": "38. A quel mot anglais correspond cette définition : 'Fraudulent technique used by hackers to solicit sensitive personal or confidential information from Internet users.'",
     "options": ["a. Ransomware", "b. File attack", "c. Phishing", "d. Eavesdropping attack"],
     "answer": "c", "full_answer": "Phishing"},

    {"question": "39. Quelle est la traduction de 'Réseaux et télécoms' en anglais ?",
     "options": ["a. Net infrastructure and telecoms", "b. Net architecture and telecoms",
                 "c. Networks and telecoms", "d. Net structure and telecoms"],
     "answer": "c", "full_answer": "Networks and telecoms"},

    {"question": "40. A quel mot anglais correspond cette définition : 'An exhaustive search method, which consists of testing all possible combinations to find a password or key.'",
     "options": ["a. Password research", "b. Bruteforce", "c. Hacker search method", "d. Encrypted attack"],
     "answer": "b", "full_answer": "Bruteforce"},

    {"question": "41. Quelle est la traduction de 'Fournir l’administration et le support du réseau' en anglais ?",
     "options": ["a. Forward network administration and support", "b. Forecast network administration and support",
                 "c. Provide network administration and support", "d. Furnish network administration and support"],
     "answer": "c", "full_answer": "Provide network administration and support"},

    {"question": "42. A quel mot anglais correspond cette définition : 'Attack that involves sending a large stream of data or packets to saturate a victim.'",
     "options": ["a. Flood", "b. Teardrop attack", "c. TCP SYN flood attack", "d. Spear phishing"],
     "answer": "a", "full_answer": "Flood"},

    {"question": "43. Quelle est la traduction de 'Aider à la mise en œuvre de systèmes informatiques' en anglais ?",
     "options": ["a. Help put together IT systems", "b. Help implement IT systems", "c. Help put in order IT systems", "d. Help ordain IT systems"],
     "answer": "b", "full_answer": "Help implement IT systems"},

    {"question": "44. Quelle est la traduction de 'Recueillir, analyser et formaliser les besoins systèmes et réseaux de l’entreprise' en anglais ?",
     "options": ["a. Recover, analyze and formalize the company's systems and networks needs",
                 "b. Collect, analyze and formalize the company's systems and networks needs",
                 "c. Review, analyze and formalize the company's needs in systems and networks",
                 "d. Classify, analyze and formalize the company's needs in systems and networks"],
     "answer": "b", "full_answer": "Collect, analyze and formalize the company's systems and networks needs"},

    {"question": "45. Quelle est la traduction de 'Identifier comment améliorer les performances' en anglais ?",
     "options": ["a. Identify improvements to perform", "b. Identify how the performances and improvements can be",
                 "c. Identify how performance can be improved", "d. Identify performant improvements"],
     "answer": "c", "full_answer": "Identify how performance can be improved"},

    {"question": "46. A quel mot anglais correspond cette définition : 'Creates a large number of processes, in order to saturate the available space within the list of processes kept by the operating system.'",
     "options": ["a. Code injection", "b. Fork bomb", "c. Man-in-the-middle attack - MITM", "d. Botnet"],
     "answer": "b", "full_answer": "Fork bomb"},

    {"question": "47. Quelle est la traduction de 'Consulter les clients' en anglais ?",
     "options": ["a. Make a consult for the clients", "b. Consultate clients", "c. Consult with clients", "d. Drive client consultations"],
     "answer": "c", "full_answer": "Consult with clients"},

    {"question": "48. A quel mot anglais correspond cette définition : 'a program that allows people to receive recognition and compensation after reporting bugs, anomalies, exploits and vulnerabilities on websites, applications or computer systems.'",
     "options": ["a. Bug bounty", "b. Reward system", "c. Failure detection", "d. Bug report"],
     "answer": "a", "full_answer": "Bug bounty"},

    {"question": "49. Quelle est la traduction de 'Processeur central' en anglais ?",
     "options": ["a. Center process", "b. Central processing unit", "c. Center processor", "d. Central processor"],
     "answer": "b", "full_answer": "Central processing unit"},

    {"question": "50. Quelle est la traduction de 'Pile de protocoles' en anglais ?",
     "options": ["a. Protocol stack", "b. Protocol pile", "c. Protocol layers", "d. Stack of protocols"],
     "answer": "a", "full_answer": "Protocol stack"},

    {"question": "51. A quel mot anglais correspond : Access management ?",
     "options": ["a. Admission management", "b. Access managing", "c. Access management", "d. Admittance management"],
     "answer": "c", "full_answer": "Access management"},

    {"question": "52. Quelle est la traduction de 'Manager le service informatique et ses projets' en anglais ?",
     "options": ["a. Lead IT into projects", "b. Drive IT projects in the service", "c. Manage IT and its projects", "d. Lead informatics service and their projects"],
     "answer": "c", "full_answer": "Manage IT and its projects"},

    {"question": "53. Quelle est la traduction de 'Rédiger et mettre à jour les procédures et les consignes d’exploitation et de documentation' en anglais ?",
     "options": ["a. Write and update operating and documentation procedures and instructions",
                 "b. Write and update operated documentation procedures and instructions",
                 "c. Write and update documentation procedures and instructions to operate",
                 "d. Write and update to operate documentation procedures and instructions"],
     "answer": "a", "full_answer": "Write and update operating and documentation procedures and instructions"},

    {"question": "54. Quelle est la traduction de 'Maintenir les logiciels et le matériel existants' en anglais ?",
     "options": ["a. Maintain into existence software and hardware", "b. Maintain software and hardware to existence",
                 "c. Maintain software and hardware that existed", "d. Maintain existing software and hardware"],
     "answer": "d", "full_answer": "Maintain existing software and hardware"},

    {"question": "55. Quelle est la traduction de 'Exploration de données' en anglais ?",
     "options": ["a. Data mining", "b. Data sampling", "c. Data scanner", "d. Data prospecting"],
     "answer": "a", "full_answer": "Data mining"},

    {"question": "56. Quelle est la traduction de 'Gestionnaire de périphérique' en anglais ?",
     "options": ["a. Device driver", "b. Peripherics driver", "c. Peripherics administrator", "d. Peripheral driver"],
     "answer": "a", "full_answer": "Device driver"},

    {"question": "57. A quel mot anglais correspond : Cryptographic transformation of data producing a cryptogram ?",
     "options": ["a. Cryptanalysis", "b. Cryptogram", "c. Encryption", "d. Cryptography"],
     "answer": "c", "full_answer": "Encryption"},

    {"question": "58. A quel mot anglais correspond : A method by which the data sender gives proof of shipment and the recipient is assured of the identity of the sender, so that no one can subsequently deny having processed that data ?",
     "options": ["a. Denial of proof", "b. Shipment fraud", "c. Data bug", "d. Non-repudiation"],
     "answer": "d", "full_answer": "Non-repudiation"},

    {"question": "59. Quelle est la traduction de 'Satisfaire les attentes du client' en anglais ?",
     "options": ["a. Satisfy the clients needs", "b. Take care of client satisfaction",
                 "c. Satisfy client waiting", "d. Meet client expectations"],
     "answer": "d", "full_answer": "Meet client expectations"},

    {"question": "60. Quelle est la traduction de 'Base de données' en anglais ?",
     "options": ["a. Database", "b. Databasis", "c. Databasics", "d. Figure base"],
     "answer": "a", "full_answer": "Database"},

    {"question": "61. Quelle est la traduction de 'Saisie des données' en anglais ?",
     "options": ["a. Data recording", "b. Data capturing", "c. Data show", "d. Data entering"],
     "answer": "a", "full_answer": "Data recording"},

    {"question": "62. A quel mot anglais correspond : Weakness in security procedures, administrative controls, internal controls, and others ?",
     "options": ["a. Spoofing", "b. Leak", "c. Vulnerability", "d. Failure"],
     "answer": "c", "full_answer": "Vulnerability"},

    {"question": "63. A quel mot anglais correspond : Computer crimes involving data modification in order to derive something of value from it ?",
     "options": ["a. Computer fraud", "b. Computer bug", "c. Computer spoofing", "d. Computer failure"],
     "answer": "a", "full_answer": "Computer fraud"},

    {"question": "64. Quelle est la traduction de 'Être garant de la pérennité et de l’évolution des solutions' en anglais ?",
     "options": ["a. Continue the solutions evolution", "b. Be the guarantor for sustained and evolved solutions",
                 "c. Ensure the perenity and evolution of solutions", "d. To guarantee the sustainability and evolution of solutions"],
     "answer": "d", "full_answer": "To guarantee the sustainability and evolution of solutions"},

    {"question": "65. Quelle est la traduction de 'Invite de commande' en anglais ?",
     "options": ["a. Command prompt", "b. Commande order", "c. Operation invite", "d. Purchase order"],
     "answer": "a", "full_answer": "Command prompt"},

    {"question": "66. A quel mot anglais correspond : Malicious software that massively sends e-mail automatically without human intervention ?",
     "options": ["a. Mailbot", "b. Drive-by download attack", "c. Phishing", "d. Ransomware"],
     "answer": "a", "full_answer": "Mailbot"},

    {"question": "67. A quel mot anglais correspond : Malicious action that involves deliberately using the address of another system instead of its own ?",
     "options": ["a. Automated address operator", "b. Address spoofing", "c. Address generator", "d. Address automation"],
     "answer": "b", "full_answer": "Address spoofing"},

    {"question": "68. Quelle est la traduction de 'Utilisateur' en anglais ?",
     "options": ["a. Uzer", "b. User", "c. Utilize", "d. Utilisator"],
     "answer": "b", "full_answer": "User"},

    {"question": "69. Quelle est la traduction de 'Sauvegarde' en anglais ?",
     "options": ["a. Backing", "b. Saving", "c. Backup", "d. Safegarde"],
     "answer": "c", "full_answer": "Backup"},

    {"question": "70. Quelle est la traduction de 'Choisir avec discernement des architectures performantes et sécurisées' en anglais ?",
     "options": ["a. Select performance to secure architectures", "b. Choose high-performance and secure architectures",
                 "c. Discern high-level performance and secured architectures", "d. Secure performance for chosen architectures"],
     "answer": "b", "full_answer": "Choose high-performance and secure architectures"},

    {"question": "71. Quelle est la traduction de 'Diriger des projets collaboratifs' en anglais ?",
     "options": ["a. Conduct project collaborations", "b. Direct collaborating projects",
                 "c. Collaborate on leading projects", "d. Lead collaborative projects"],
     "answer": "d", "full_answer": "Lead collaborative projects"},

    {"question": "72. Quelle est la traduction de 'Panneau de configuration' en anglais ?",
     "options": ["a. Monitoring panel", "b. Configuration panelling", "c. Controlling panels", "d. Control panel"],
     "answer": "d", "full_answer": "Control panel"},

    {"question": "73. Quelle est la traduction de 'Travailler avec le personnel de support informatique' en anglais ?",
     "options": ["a. Work in IT personnel staff", "b. Work between IT support and staff",
                 "c. Work with IT support staff", "d. Work among IT and support staff"],
     "answer": "c", "full_answer": "Work with IT support staff"},

    {"question": "74. Quelle est la traduction de 'Processeur graphique' en anglais ?",
     "options": ["a. Graph processing", "b. Graphics processor", "c. Graphical processor", "d. Graphics processing unit"],
     "answer": "d", "full_answer": "Graphics processing unit"},

    {"question": "75. Quelle est la traduction de 'Modéliser l’architecture systèmes et réseaux' en anglais ?",
     "options": ["a. Modelise an architecture from systems and networks", "b. Modeling systems and networks architecture",
                 "c. Model systems and networks in architecture", "d. Modelize the architecture for systems and networks"],
     "answer": "b", "full_answer": "Modeling systems and networks architecture"},

    {"question": "76. Quelle est la traduction de 'Se tenir informé des tendances en évolution rapide' en anglais ?",
     "options": ["a. Be informed about fast trends", "b. Track fast-moving trends", "c. Survey fast-evolving trends", "d. Keep up to date with fast-changing trends"],
     "answer": "d", "full_answer": "Keep up to date with fast-changing trends"},

    {"question": "77. Quelle est la traduction de 'Mémoire vive' en anglais ?",
     "options": ["a. Random access memory", "b. Life memory", "c. Alive memory", "d. Readable memory"],
     "answer": "a", "full_answer": "Random access memory"},

    {"question": "78. Quelle est la traduction de 'Effectuer un suivi des équipements' en anglais ?",
     "options": ["a. Follow equipment", "b. Track equipment", "c. Target equipment", "d. Keep up equipment"],
     "answer": "b", "full_answer": "Track equipment"},

    {"question": "79. Quelle est la traduction de 'Centre de données' en anglais ?",
     "options": ["a. Data core", "b. Data desk", "c. Data center", "d. Data office"],
     "answer": "c", "full_answer": "Data center"},

    {"question": "80. Quelle est la traduction de 'Accompagner la stratégie de l’entreprise' en anglais ?",
     "options": ["a. Submit the company's strategy", "b. Survey the company's strategy", "c. Supply the company's strategy", "d. Support the company’s strategy"],
     "answer": "d", "full_answer": "Support the company’s strategy"},

    {"question": "81. A quel mot anglais correspond : Occurs as a result of parallelization of a certain kind of attacks simultaneously carried out by multiple systems against a single victim system ?",
     "options": ["a. Man-in-the-middle attack - MITM", "b. Cyber attacks", "c. Hacking-wargames", "d. Denial of service attack -DDoS"],
     "answer": "d", "full_answer": "Denial of service attack -DDoS"},

    {"question": "82. Quelle est la traduction de 'Application client-serveur' en anglais ?",
     "options": ["a. Client-server application", "b. Client-IT application", "c. Client-computing application", "d. Client-serving application"],
     "answer": "a", "full_answer": "Client-server application"},

    {"question": "83. Quelle est la traduction de 'Serveur' en anglais ?",
     "options": ["a. Servering", "b. Hoster", "c. Host", "d. Servor"],
     "answer": "c", "full_answer": "Host"},

    {"question": "84. Quelle est la traduction de 'Assurer le maintien en condition opérationnelle du réseau et de l’architecture système de l’entreprise' en anglais ?",
     "options": ["a. Keep on operational conditions of the company's architecture network and system",
                 "b. Maintain in condition operational the network and system company's architecture",
                 "c. Maintain the operational condition of the company's network and system architecture",
                 "d. Pursue the company's systems and networks architecture operating conditions"],
     "answer": "c", "full_answer": "Maintain the operational condition of the company's network and system architecture"},

    {"question": "85. Quelle est la traduction de 'Garantir l’optimisation des ressources systèmes' en anglais ?",
     "options": ["a. Guarantee system optimized resources", "b. Ensure optimization for system resources",
                 "c. Structure optimized system resources", "d. Make sure optimization for system resources is set"],
     "answer": "b", "full_answer": "Ensure optimization for system resources"},

    {"question": "86. Quelle est la traduction de 'Communiquer et promouvoir un projet informatique' en anglais ?",
     "options": ["a. Computer project to commute and promote", "b. Communicate and promote a computer project",
                 "c. Communicate to promote a computer project", "d. Project computer to communicate and promove"],
     "answer": "b", "full_answer": "Communicate and promote a computer project"},

    {"question": "87. A quel mot anglais correspond : A seemingly useful and harmless program with additional hidden code to collect, exploit, falsify or destroy data illegally ?",
     "options": ["a. Spear phishing", "b. Teardrop attack", "c. Trojan horse", "d. Denial of service attack -DDoS"],
     "answer": "c", "full_answer": "Trojan horse"},

    {"question": "88. Quelle est la traduction de 'Construire un cahier des charges' en anglais ?",
     "options": ["a. Create a book of charges", "b. Specify the needs", "c. Construct a charge schedule", "d. Build specifications"],
     "answer": "d", "full_answer": "Build specifications"},

    {"question": "89. Quelle est la traduction de 'Rédiger les besoins pour les nouveaux systèmes informatiques' en anglais ?",
     "options": ["a. Write the new IT needs for the systems", "b. Write systems for IT needs", "c. Write requirements for new IT systems", "d. Write IT needs for new systems"],
     "answer": "c", "full_answer": "Write requirements for new IT systems"},

    {"question": "90. Quelle est la traduction de 'Maintenir et sécuriser les infrastructures informatiques' en anglais ?",
     "options": ["a. Maintain and make safe IT infrastructure", "b. Maintain and save IT infrastructure",
                 "c. Maintain and securize infrastructure informatics", "d. Maintain and secure IT infrastructure"],
     "answer": "d", "full_answer": "Maintain and secure IT infrastructure"},

    {"question": "91. Quelle est la traduction de 'Rechercher, diagnostiquer les bugs' en anglais ?",
     "options": ["a. Tremblespoting", "b. Troubleshooting", "c. Bugshooting", "d. Supportstanding"],
     "answer": "b", "full_answer": "Troubleshooting"},

    {"question": "92. Quelle est la traduction de 'Être en mesure de gérer une liste de problèmes ou d’améliorations' en anglais ?",
     "options": ["a. Be capable to deal with a list of problems and implementations",
                 "b. Be able to manage a list of issues or improvements",
                 "c. Be responsible for a list of issues and implantations",
                 "d. Be in measure to manage a list of problems or ameliorations"],
     "answer": "b", "full_answer": "Be able to manage a list of issues or improvements"},

    {"question": "93. Quelle est la traduction de 'Redémarrer' en anglais ?",
     "options": ["a. To reboot", "b. To reinitiate", "c. To reinstall", "d. To reinitialise"],
     "answer": "a", "full_answer": "To reboot"},

    {"question": "94. Quelle est la traduction de 'Répertoire racine' en anglais ?",
     "options": ["a. Root register", "b. Root directory", "c. Root repertory", "d. Rot repertoire"],
     "answer": "b", "full_answer": "Root directory"},

    {"question": "95. Quelle est la traduction de 'Sensibiliser les utilisateurs pour optimiser leur utilisation' en anglais ?",
     "options": ["a. Bring sensitivity among optimized utilisation by users", "b. Rise consciousness for utilizers to optimize their use",
                 "c. Raise awareness among users to optimize their use", "d. Sensibilize users for optimized use"],
     "answer": "c", "full_answer": "Raise awareness among users to optimize their use"},

    {"question": "96. Quelle est la traduction de 'Exploitation des réseaux' en anglais ?",
     "options": ["a. Network operation", "b. Network distribution", "c. Network exploit", "d. Network exploration"],
     "answer": "a", "full_answer": "Network operation"},

    {"question": "97. Quelle est la traduction de 'Paramètres' en anglais ?",
     "options": ["a. Sets", "b. Parametized", "c. Settings", "d. Parametering"],
     "answer": "c", "full_answer": "Settings"},

    {"question": "98. Quelle est la traduction de 'Piloter un projet d’infrastructure systèmes et réseaux' en anglais ?",
     "options": ["a. Conduct systems and networks project for better infrastructure",
                 "b. Drive an infrastructure project for systems and networks",
                 "c. Pilote a project on systems and networks infrastructure",
                 "d. Lead a systems and networks infrastructure project"],
     "answer": "d", "full_answer": "Lead a systems and networks infrastructure project"},

    {"question": "99. Quelle est la traduction de 'Routeur' en anglais ?",
     "options": ["a. Router", "b. Rooter", "c. Roter", "d. Routor"],
     "answer": "a", "full_answer": "Router"},

    {"question": "100. Quelle est la traduction de 'Désinstaller' en anglais ?",
     "options": ["a. To disinstall", "b. To uninstall", "c. To preinstall", "d. To desinstall"],
     "answer": "b", "full_answer": "To uninstall"},

    {"question": "101. Quelle est la traduction de 'Analyser et identifier tous les problèmes potentiels' en anglais ?",
     "options": ["a. Analyze and observe many potential problems", "b. Analyze and identify any potential problems",
                 "c. Analyze and identificate many potential problems", "d. Make analysis and identification of every potential problems"],
     "answer": "b", "full_answer": "Analyze and identify any potential problems"},

    {"question": "102. Quelle est la traduction de 'Virtualisation des serveurs' en anglais ?",
     "options": ["a. Hosting virtualization", "b. Server virtualization", "c. Servering virtualization", "d. Servor virtualizing"],
     "answer": "b", "full_answer": "Server virtualization"},

    {"question": "103. Quelle est la traduction de 'Analyser dans quelle mesure les logiciels, le matériel et le système informatique au sens plus large correspondent aux besoins de l’entreprise' en anglais ?",
     "options": ["a. Analyze how software, hardware and IT system match company needs", 
                 "b. Analyze if IT solutions correspond to business requirements",
                 "c. Review software, hardware and systems to fulfill company needs",
                 "d. Analyze to what extent software, hardware and IT system meet company requirements"],
     "answer": "d", "full_answer": "Analyze to what extent software, hardware and IT system meet company requirements"},

    {"question": "104. A quel mot anglais correspond : Data flow ?",
     "options": ["a. Data flux", "b. Figure flow", "c. Data flush", "d. Data flow"],
     "answer": "d", "full_answer": "Data flow"},

    {"question": "105. Quelle est la traduction de 'Poste de travail' en anglais ?",
     "options": ["a. Work office", "b. Work post", "c. Workstation", "d. Work desk"],
     "answer": "c", "full_answer": "Workstation"},

    {"question": "106. Quelle est la traduction de 'Stockage des données' en anglais ?",
     "options": ["a. Data stockage", "b. Data storing", "c. Data storage", "d. Data stores"],
     "answer": "c", "full_answer": "Data storage"},

    {"question": "107. Quelle est la traduction de 'Surveillance' en anglais ?",
     "options": ["a. Monitoring", "b. Telecontrolling", "c. Mentoring", "d. Motoring"],
     "answer": "a", "full_answer": "Monitoring"},

    {"question": "108. Quelle est la traduction de 'Réseau' en anglais ?",
     "options": ["a. Net web", "b. Web system", "c. Net architecture", "d. Network"],
     "answer": "d", "full_answer": "Network"},

    {"question": "109. Quelle est la traduction de 'Spécifier les besoins du système' en anglais ?",
     "options": ["a. Specify system requirements", "b. Specificate system needs",
                 "c. Specialize system needs", "d. Specify required systems"],
     "answer": "a", "full_answer": "Specify system requirements"},

    {"question": "110. Quelle est la traduction de 'Budgétiser l’équipement' en anglais ?",
     "options": ["a. Equip the budget", "b. Budget to equip", "c. Equipping the budget", "d. Budget for equipment"],
     "answer": "d", "full_answer": "Budget for equipment"},

    {"question": "111. Quelle est la traduction de 'Machine virtuelle' en anglais ?",
     "options": ["a. Virtuel machine", "b. Virtualized machine", "c. Virtual machine", "d. Virtualizing machine"],
     "answer": "c", "full_answer": "Virtual machine"},

    {"question": "112. Quelle est la traduction de 'Carte son' en anglais ?",
     "options": ["a. Sound board", "b. Sound chip", "c. Sound chart", "d. Sound card"],
     "answer": "d", "full_answer": "Sound card"},

    {"question": "113. Quelle est la traduction de 'Système d'exploitation' en anglais ?",
     "options": ["a. Operating system", "b. Exploitation système", "c. Exploitered system", "d. Monitor system"],
     "answer": "a", "full_answer": "Operating system"},

    {"question": "114. Quelle est la traduction de 'Carte mère' en anglais ?",
     "options": ["a. Motherchip", "b. Motherboard", "c. Motherchart", "d. Mothercard"],
     "answer": "b", "full_answer": "Motherboard"},

    {"question": "115. Quelle est la traduction de 'Assurer une veille technologique' en anglais ?",
     "options": ["a. Survey the technology", "b. Ensure a technological watch",
                 "c. Supply the technological survey", "d. Browse the internet"],
     "answer": "b", "full_answer": "Ensure a technological watch"},

    {"question": "116. Quelle est la traduction de 'Conseiller la DSI sur l’utilisation des ressources du système' en anglais ?",
     "options": ["a. Council the CIO in the purpose of system resources use", 
                 "b. Lead the CIO towards the use of system resources",
                 "c. Bring resources to the system to advise the CIO", 
                 "d. Advise the CIO on the use of system resources"],
     "answer": "d", "full_answer": "Advise the CIO on the use of system resources"},

    {"question": "117. A quel mot anglais correspond : Measures traffic or collects information about the user, under the appearance of an image placed on a web page ?",
     "options": ["a. Web bug", "b. User bug", "c. Information bug", "d. Traffic bug"],
     "answer": "a", "full_answer": "Web bug"},

    {"question": "118. Quelle est la traduction de 'Respecter les contraintes de qualité, de coûts et de délais' en anglais ?",
     "options": ["a. Review quality, cost and time constraints", "b. Schedule quality, expenses and delays constraints",
                 "c. Meet quality, cost and time constraints", "d. Repeal quality, money and time constraints"],
     "answer": "c", "full_answer": "Meet quality, cost and time constraints"},

    {"question": "119. Quelle est la traduction de 'Restauration des données' en anglais ?",
     "options": ["a. Data recovering", "b. Data recovery", "c. Data restauration", "d. Data recovers"],
     "answer": "b", "full_answer": "Data recovery"},

    {"question": "120. Quelle est la traduction de 'Service d'assistance' en anglais ?",
     "options": ["a. Aid office", "b. Assistance office", "c. Assistance desk", "d. Help desk"],
     "answer": "d", "full_answer": "Help desk"},

    {"question": "121. A quel mot anglais correspond : Electronic communication, including e-mail, unsolicited by recipients, massively shipped for advertising or dishonest purposes ?",
     "options": ["a. Botnet", "b. Spam", "c. Spear phishing", "d. Mailbot"],
     "answer": "b", "full_answer": "Spam"},

    {"question": "122. Quelle est la traduction de 'Installer et configurer des réseaux et des systèmes informatiques' en anglais ?",
     "options": ["a. Install and configurate networks and systems computer",
                 "b. Install networks and systems for configured computers",
                 "c. Install networks and systems computer to configure",
                 "d. Install and configure computer networks and systems"],
     "answer": "d", "full_answer": "Install and configure computer networks and systems"},

    {"question": "123. A quel mot anglais correspond : Attack which targets websites, changing parameters in their database through SQL queries ?",
     "options": ["a. Ping of death", "b. SQL injection", "c. IP Spoofing", "d. Smurf attack"],
     "answer": "b", "full_answer": "SQL injection"},

    {"question": "124. A quel mot anglais correspond : A technique for exploiting a vulnerability in a program's code that does not properly verify the size of certain data it manipulates ?",
     "options": ["a. Data hack", "b. Buffer overflow", "c. Vulnerability explorer", "d. Data manipulation"],
     "answer": "b", "full_answer": "Buffer overflow"},

    {"question": "125. Quelle est la traduction de 'Connecter différents appareils ensemble pour former des réseaux rapides et efficaces' en anglais ?",
     "options": ["a. Make a connection between different devices from fast and effective networks",
                 "b. Plug in different devices fast and effective networks",
                 "c. Put together fast and efficient networks to make different devices",
                 "d. Connect different devices together to form fast and efficient networks"],
     "answer": "d", "full_answer": "Connect different devices together to form fast and efficient networks"}

]

# Liste globale pour stocker les questions ratées
questions_fausses = []

def run_quiz(selected_questions, memorize_mistakes=True):
    score = 0
    global questions_fausses
    for q in selected_questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        
        user_answer = input("Votre réponse (a/b/c/d) : ").lower()
        
        if user_answer == q["answer"]:
            print("✅ Correct ! +1 point\n")
            score += 1
        else:
            print(f"❌ Faux. La bonne réponse est {q['answer']} ***{q['full_answer']}***\n")
            if memorize_mistakes and q not in questions_fausses:
                questions_fausses.append(q)
                
    print(f"Votre score final est {score} / {len(selected_questions)}\n")

def quiz_entier():
    run_quiz(questions)

def quiz_aleatoire(n):
    if n > len(questions):
        n = len(questions)
    selected_questions = random.sample(questions, n)
    run_quiz(selected_questions)

def quiz_faux():
    if questions_fausses:
        print("Vous allez refaire uniquement les questions que vous avez ratées précédemment !")
        run_quiz(questions_fausses, memorize_mistakes=False)
        # On vide la liste après le passage pour ne pas répéter les mêmes
        questions_fausses.clear()
    else:
        print("Bravo ! Vous n'avez aucune question incorrecte à réviser.\n")

# Menu interactif
def menu():
    while True:
        print("Bienvenue au QCM interactif !")
        print("1. Faire le test complet")
        print("2. Faire un quiz aléatoire")
        print("3. Refaire uniquement les questions ratées")
        print("4. Quitter")
        
        choix = input("Votre choix (1/2/3/4) : ")
        
        if choix == "1":
            quiz_entier()
        elif choix == "2":
            nb = int(input(f"Combien de questions voulez-vous ? (max {len(questions)}) : "))
            quiz_aleatoire(nb)
        elif choix == "3":
            quiz_faux()
        elif choix == "4":
            print("Merci d'avoir utilisé le QCM interactif !")
            break
        else:
            print("Choix invalide.\n")

# Lancer le menu
menu()