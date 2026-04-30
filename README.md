# 📬 contact-me

Serveur de contact léger pour portfolio personnel. Reçoit les messages du formulaire de contact et les transmet instantanément via un bot Telegram.

---

## ✨ Fonctionnalités

- **API REST** — endpoint `POST /contact` en JSON
- **Notification Telegram** — message formaté envoyé en temps réel
- **CORS configuré** — accepte uniquement les requêtes depuis ton domaine
- **Validation automatique** — champs vérifiés via Pydantic

---

## 🛠️ Stack

| Outil | Rôle |
|---|---|
| [FastAPI](https://fastapi.tiangolo.com/) | Framework API |
| [Uvicorn](https://www.uvicorn.org/) | Serveur ASGI |
| [httpx](https://www.python-httpx.org/) | Requêtes HTTP async |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Variables d'environnement |
| Telegram Bot API | Notifications |

---

## 🚀 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/RayanBO/contact-me.git
cd contact-me
```

### 2. Installer les dépendances

```bash
pip install fastapi uvicorn httpx python-dotenv
```

### 3. Configurer les variables d'environnement

Crée un fichier `.env` à la racine :

```env
TELEGRAM_TOKEN=7xxxxxxxxx:AAFxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TELEGRAM_CHAT_ID=123456789
```

> **Comment obtenir ces valeurs ?**
> - `TELEGRAM_TOKEN` → crée un bot via [@BotFather](https://t.me/BotFather) sur Telegram
> - `TELEGRAM_CHAT_ID` → envoie un message à ton bot puis visite `https://api.telegram.org/bot<TOKEN>/getUpdates`

### 4. Lancer le serveur

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

---

## 📡 API

### `POST /contact`

**Corps de la requête (JSON) :**

```json
{
  "name": "Jean Dupont",
  "email": "jean@example.com",
  "message": "Bonjour, je souhaite vous contacter..."
}
```

**Réponse :**

```json
{ "ok": true }
```

**Notification reçue sur Telegram :**

```
📬 Nouveau message portfolio

👤 Nom : Jean Dupont
📧 Email : jean@example.com
💬 Message :
Bonjour, je souhaite vous contacter...
```

---

## 🌐 Déploiement VPS

### Nginx (reverse proxy)

```nginx
server {
    listen 80;
    server_name api.ton-domaine.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### systemd (service persistant)

Crée `/etc/systemd/system/contact-me.service` :

```ini
[Unit]
Description=Contact Me FastAPI Server
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/contact-me
EnvironmentFile=/var/www/contact-me/.env
ExecStart=uvicorn main:app --host 127.0.0.1 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable contact-me
sudo systemctl start contact-me
```

---

## 🔒 Sécurité

- Le fichier `.env` est ignoré par Git (voir `.gitignore`)
- Ne jamais committer `TELEGRAM_TOKEN` ou `TELEGRAM_CHAT_ID` en dur dans le code
- Restreindre le CORS à ton domaine uniquement

---

## 📄 Licence

MIT © [RayanBO](https://github.com/RayanBO)
