"""
TSIS 4 — Snake | shared constants & DB credentials.
"""
import os

# ---- screen / grid -----------------------------------------------------
CELL          = 24
GRID_W        = 25
GRID_H        = 22
HUD_H         = 70
SCREEN_W      = CELL * GRID_W
SCREEN_H      = CELL * GRID_H + HUD_H

# ---- gameplay ----------------------------------------------------------
BASE_FPS          = 8
LEVEL_FOOD_STEP   = 5
SPEED_PER_LEVEL   = 1
OBSTACLE_LEVEL    = 3
OBSTACLES_PER_LV  = 6

POISON_PROBABILITY = 0.18

# ---- power-ups ---------------------------------------------------------
POWERUP_LIFETIME_MS = 8000
POWERUP_DURATION_MS = 5000
POWERUP_SPAWN_CHANCE_PER_FOOD = 0.35

# ---- DB ----------------------------------------------------------------
DB_CONFIG = {
    "host":     os.getenv("PGHOST",     "localhost"),
    "port":     os.getenv("PGPORT",     "5432"),
    "dbname":   os.getenv("PGDATABASE", "snakegame"),
    "user":     os.getenv("PGUSER",     "postgres"),
    "password": os.getenv("PGPASSWORD", "Zxcvbnm@210307"),
}

# ---- palette (muted / minimal) -----------------------------------------
COLOR = {
    "bg":           (18, 20, 24),
    "panel":        (28, 31, 38),
    "grid":         (32, 36, 44),
    "text":         (210, 210, 210),
    "dim":          (100, 108, 120),
    "accent":       (130, 170, 140),
    "danger":       (180, 75, 75),
    "food":         (190, 165, 70),
    "food_big":     (200, 120, 60),
    "poison":       (140, 50, 50),
    "obstacle":     (65, 70, 85),
    "shield_aura":  (100, 155, 200),
    "powerup_speed": (100, 155, 200),
    "powerup_slow":  (155, 110, 200),
    "powerup_shield":(200, 175, 85),
}

# ---- save file ---------------------------------------------------------
SETTINGS_FILE = "settings.json"