# MobPo Asesmen 3 REST API - SIMLABFIT

REST API MobPro untuk aplikasi mobpro SimLabFit dengan setup database async yang siap ditambahkan model dan migration.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env-example .env
```

## Run

```powershell
fastapi dev app/main.py
```

Cek API Pada `http://127.0.0.1:8000`.

## Endpoints

- `GET /` - API information
- `GET /health` - health check
- `GET /health/db` - async database health check



Open `http://127.0.0.1:8000/docs` for interactive API documentation.

## Database

Project ini memakai SQLAlchemy async di folder `app/database/`.

- `app/database/base.py` berisi declarative `Base` untuk model nanti.
- `app/database/session.py` berisi async engine, session factory, dan dependency `get_db`.
- `DATABASE_URL` dibuat dari konfigurasi database di `.env`.

Default database memakai konfigurasi di `.env`. Untuk development cepat, ubah `DATABASE=sqlite`.
```
cp .env

## Migration

Project ini sudah memakai Alembic dan punya migration awal untuk table `users`.

Jalankan migration:

```powershell
alembic upgrade head
```

Buat migration baru setelah menambah atau mengubah model:

```powershell
alembic revision --autogenerate -m "create table name"
```
