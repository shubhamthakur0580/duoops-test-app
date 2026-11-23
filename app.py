# DuoOps Sample Backend Microservice v1.0.0
import os
DB_HOST = os.getenv("DB_HOST", "sample-db.demo.svc.cluster.local:5432")
print(f"Service running, connected to DB at {DB_HOST}")
