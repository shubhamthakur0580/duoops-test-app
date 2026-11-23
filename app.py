# DuoOps Sample Backend Microservice - Breaking Change
import os
# BUG: Invalid internal database cluster endpoint
DB_HOST = os.getenv("DB_HOST", "cluster-db:9999")
print(f"Service starting... Attempting connection to {DB_HOST}")
raise ConnectionRefusedError(f"FATAL: dial tcp 10.96.0.1:9999: connect: database connection refused at {DB_HOST}")
