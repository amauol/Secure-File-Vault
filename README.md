🔐 Secure File Vault – TP Admin Linux & DevOps
📌 Présentation

Secure File Vault est un service de dépôt de fichiers sécurisé conçu pour être déployé sur un système Linux.
Ce TP permet de pratiquer :

Administration Linux (utilisateurs, permissions, services systemd)

Sécurisation d’un service web

Scripting Bash pour automatisation (backup, vérification d’intégrité)

Déploiement via Docker

Intégration CI/CD avec GitHub Actions

Organisation de projet professionnelle et versionnée sur GitHub

Le projet est facilement portable sur une VM, dans un homelab, ou sur un serveur cloud.

🎯 Objectifs pédagogiques

À la fin de ce TP, l’étudiant sera capable de :

Créer un utilisateur système dédié pour un service

Déployer une application web en Python (Flask)

Lancer et superviser le service avec systemd

Sécuriser le service (droits, firewall, isolation)

Automatiser la sauvegarde et la vérification d’intégrité

Conteneuriser le service avec Docker

Configurer un pipeline CI/CD simple pour linting Python

Structurer un projet pour GitHub

🧱 Architecture du projet
secure-file-vault/
│
├── app/
│   ├── app.py
│   └── uploads/
│
├── scripts/
│   ├── backup.sh
│   └── integrity_check.sh
│
├── systemd/
│   └── secure-vault.service
│
├── docker/
│   └── Dockerfile
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .gitignore
└── README.md

⚙️ Installation et déploiement
1️⃣ Création de l’utilisateur système
sudo useradd -r -s /usr/sbin/nologin vaultsvc
sudo mkdir -p /var/lib/secure-vault/uploads
sudo chown -R vaultsvc:vaultsvc /var/lib/secure-vault

2️⃣ Déploiement de l’application
sudo cp -r app /var/lib/secure-vault/
sudo chown -R vaultsvc:vaultsvc /var/lib/secure-vault


Test manuel :

python3 app/app.py
curl http://localhost:8080/health

3️⃣ Service systemd
sudo cp systemd/secure-vault.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl enable secure-vault
sudo systemctl start secure-vault
sudo systemctl status secure-vault

4️⃣ Sécurisation réseau
sudo ufw allow 8080/tcp
sudo ufw enable
sudo ufw status

5️⃣ Sauvegarde automatique

Script : scripts/backup.sh

Cron (toutes les 6 heures) :

0 */6 * * * /home/<user>/secure-file-vault/scripts/backup.sh

6️⃣ Vérification d’intégrité

Script : scripts/integrity_check.sh
Vérifie le SHA256 des fichiers uploadés.

7️⃣ Dockerisation
docker build -t secure-vault docker/
docker run -p 8080:8080 secure-vault

8️⃣ CI/CD (GitHub Actions)

Fichier : .github/workflows/ci.yml

Vérifie la syntaxe et le style du code Python avec flake8

Déclenché à chaque push ou pull request

🧪 Tests

Upload d’un fichier :

echo "test" > test.txt
curl -F "file=@test.txt" http://localhost:8080/upload


Réponse attendue :

{
  "filename": "test.txt",
  "sha256": "<hash>",
  "status": "uploaded"
}

🧠 Compétences validées

Administration Linux et services systemd

Scripting Bash et automatisation

Déploiement sécurisé de services web

Conteneurisation Docker

CI/CD et GitHub Actions

Organisation et documentation de projet

📌 Améliorations possibles

Authentification JWT pour l’API

HTTPS avec Nginx / Certbot

Monitoring Prometheus / Grafana

Reverse proxy et load balancing

Chiffrement des fichiers côté serveur

👤 Auteur

Projet personnel – Administration Système & DevOps – 2025

📜 Licence

Libre pour usage pédagogique.
