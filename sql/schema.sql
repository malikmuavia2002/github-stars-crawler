CREATE TABLE IF NOT EXISTS repositories (
    full_name TEXT PRIMARY KEY,
    stars INT NOT NULL,
    updated_at TIMESTAMP DEFAULT NOW()
);

