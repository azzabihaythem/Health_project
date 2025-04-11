from cryptography.fernet import Fernet

# Générer une clé de chiffrement
key = Fernet.generate_key()
print(f"Clé de chiffrement : {key.decode()}")

# Sauvegardez cette clé dans un endroit sécurisé
with open("encryption_key.key", "wb") as key_file:
    key_file.write(key)

# Charger la clé de chiffrement
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Mots de passe à chiffrer
admin_password = "******"
readonly_password = "*****"

# Chiffrer les mots de passe
encrypted_admin_password = cipher_suite.encrypt(admin_password.encode()).decode()
encrypted_readonly_password = cipher_suite.encrypt(readonly_password.encode()).decode()

print(f"MONGO_ADMIN_PASSWORD={encrypted_admin_password}")
print(f"MONGO_READ_ONLY_USERNAME_PASSWORD={encrypted_readonly_password}")