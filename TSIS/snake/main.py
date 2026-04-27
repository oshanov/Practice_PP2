from __future__ import annotations
import json
import os
import sys
from typing import Callable
import pygame
import db
import game as gamemod
from config import (
    SCREEN_W, SCREEN_H, CELL, GRID_W, GRID_H, HUD_H,
    COLOR, SETTINGS_FILE,
)

DEFAULT_SETTINGS = {
    "snake_color": [100, 150, 115],
    "grid":  True,
}

#settings
def load_settings() -> dict:
    if not os.path.exists(SETTINGS_FILE):
        save_settings(DEFAULT_SETTINGS)
        return dict(DEFAULT_SETTINGS)
    try:
        with open(SETTINGS_FILE, encoding="utf-8") as f:
            return {**DEFAULT_SETTINGS, **json.load(f)}
    except (json.JSONDecodeError, OSError):
        return dict(DEFAULT_SETTINGS)

def save_settings(s: dict):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(s, f, indent=2)

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

font_title = pygame.font.SysFont("Arial", 32, bold=True)
font_med   = pygame.font.SysFont("Arial", 20)
font_small = pygame.font.SysFont("Arial", 14)

#ui
class Button:
    def __init__(self, rect, label, on_click: Callable[[], None],
                 colour=COLOR["accent"], fg=(20, 20, 20)):
        self.rect     = pygame.Rect(rect)
        self.label    = label
        self.on_click = on_click
        self.colour   = colour
        self.fg       = fg

    def text(self):
        return self.label() if callable(self.label) else self.label

    def draw(self, surf, font):
        hover = self.rect.collidepoint(pygame.mouse.get_pos())
        c = tuple(min(255, x + (15 if hover else 0)) for x in self.colour)
        pygame.draw.rect(surf, c, self.rect)
        t = font.render(self.text(), True, self.fg)
        surf.blit(t, t.get_rect(center=self.rect.center))

    def handle(self, ev):
        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and \
                self.rect.collidepoint(ev.pos):
            self.on_click()

def centered(surf, font, text, y, color=COLOR["text"]):
    s = font.render(text, True, color)
    surf.blit(s, s.get_rect(center=(SCREEN_W // 2, y)))

def offline_notice():
    if not db.is_online():
        centered(screen, font_small, "offline", SCREEN_H - 20, COLOR["danger"])

# username prompt
def prompt_username(default="player") -> str:
    name = default
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN and name.strip():
                    return name.strip()
                elif ev.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif ev.key == pygame.K_ESCAPE:
                    return name.strip() or default
                elif ev.unicode.isprintable() and len(name) < 14:
                    name += ev.unicode

        screen.fill(COLOR["bg"])
        centered(screen, font_title, "enter name", SCREEN_H // 2 - 60, COLOR["accent"])
        box = pygame.Rect(0, 0, 380, 50)
        box.center = (SCREEN_W // 2, SCREEN_H // 2)
        pygame.draw.rect(screen, COLOR["panel"], box)
        pygame.draw.rect(screen, COLOR["dim"], box, 1)
        centered(screen, font_med, name + "▌", box.centery)
        centered(screen, font_small, "enter to confirm", SCREEN_H // 2 + 55, COLOR["dim"])
        offline_notice()
        pygame.display.flip()
        clock.tick(60)

# draw board
def draw_board(g: gamemod.Game, settings: dict, name: str, pb: int):
    screen.fill(COLOR["bg"])

    # HUD
    pygame.draw.rect(screen, COLOR["panel"], (0, 0, SCREEN_W, HUD_H))
    screen.blit(font_med.render(f"score {g.score}", True, COLOR["text"]), (10, 8))
    screen.blit(font_med.render(f"level {g.level}", True, COLOR["text"]), (10, 34))
    screen.blit(font_small.render(name,       True, COLOR["dim"]), (200, 10))
    screen.blit(font_small.render(f"best {pb}", True, COLOR["dim"]), (200, 28))
    screen.blit(font_small.render(f"len {len(g.snake)}", True, COLOR["dim"]), (200, 46))

    if g.effect:
        remain = "" if g.effect == "shield" \
            else f" {max(0, g.effect_until - pygame.time.get_ticks())//1000+1}s"
        screen.blit(font_small.render(f"{g.effect}{remain}", True, COLOR["accent"]), (340, 10))
    if g.shield_active:
        screen.blit(font_small.render("shield", True, COLOR["accent"]), (340, 28))
    if not db.is_online():
        screen.blit(font_small.render("offline", True, COLOR["danger"]), (SCREEN_W - 68, 10))

    #grid
    if settings.get("grid", True):
        for x in range(GRID_W + 1):
            pygame.draw.line(screen, COLOR["grid"], (x*CELL, HUD_H), (x*CELL, SCREEN_H), 1)
        for y in range(GRID_H + 1):
            pygame.draw.line(screen, COLOR["grid"], (0, HUD_H + y*CELL), (SCREEN_W, HUD_H + y*CELL), 1)

    #obstacles
    for ox, oy in g.obstacles:
        pygame.draw.rect(screen, COLOR["obstacle"],
                         (ox*CELL+1, HUD_H + oy*CELL+1, CELL-2, CELL-2))

    #foods
    for f in g.foods:
        cx = f.pos[0]*CELL + CELL//2
        cy = HUD_H + f.pos[1]*CELL + CELL//2
        if f.kind == "poison":
            pygame.draw.rect(screen, COLOR["poison"],
                             (f.pos[0]*CELL+3, HUD_H + f.pos[1]*CELL+3, CELL-6, CELL-6))
        elif f.kind == "big":
            pygame.draw.circle(screen, COLOR["food_big"], (cx, cy), CELL//2 - 2)
        else:
            pygame.draw.circle(screen, COLOR["food"], (cx, cy), CELL//2 - 4)

    #power-up
    if g.powerup:
        cx = g.powerup.pos[0]*CELL + CELL//2
        cy = HUD_H + g.powerup.pos[1]*CELL + CELL//2
        col = COLOR[f"powerup_{g.powerup.kind}"]
        pygame.draw.rect(screen, col,
                         (cx - CELL//2 + 2, cy - CELL//2 + 2, CELL-4, CELL-4))
        letter = {"speed": "S", "slow": "L", "shield": "*"}[g.powerup.kind]
        s = font_small.render(letter, True, COLOR["bg"])
        screen.blit(s, s.get_rect(center=(cx, cy)))

    #snake 
    snake_color = tuple(settings.get("snake_color", [100, 150, 115]))
    head_color  = tuple(min(255, c + 20) for c in snake_color)
    for i, (sx, sy) in enumerate(g.snake):
        c = head_color if i == 0 else snake_color
        pygame.draw.rect(screen, c, (sx*CELL+1, HUD_H + sy*CELL+1, CELL-2, CELL-2))

    # shield outline
    if g.shield_active:
        hx, hy = g.snake[0]
        pygame.draw.rect(screen, COLOR["shield_aura"],
                         (hx*CELL, HUD_H + hy*CELL, CELL, CELL), 1)

#screens
def main_menu():
    state = {"a": None}
    bw, bh, bx = 200, 44, SCREEN_W//2 - 100
    btns = [
        Button((bx, 200, bw, bh), "Play",        lambda: state.update(a="play")),
        Button((bx, 258, bw, bh), "Leaderboard", lambda: state.update(a="board"),
               colour=COLOR["panel"], fg=COLOR["text"]),
        Button((bx, 316, bw, bh), "Settings",    lambda: state.update(a="settings"),
               colour=COLOR["panel"], fg=COLOR["text"]),
        Button((bx, 374, bw, bh), "Quit",        lambda: state.update(a="quit"),
               colour=COLOR["danger"], fg=(220, 220, 220)),
    ]
    while state["a"] is None:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                state["a"] = "quit"
            for b in btns: b.handle(ev)
        screen.fill(COLOR["bg"])
        centered(screen, font_title, "SNAKE", 130, COLOR["accent"])
        for b in btns: b.draw(screen, font_med)
        offline_notice()
        pygame.display.flip()
        clock.tick(60)
    return state["a"]

def settings_screen(s: dict):
    palette = [
        ("green",  [100, 150, 115]),
        ("blue",   [80, 130, 190]),
        ("red",    [180, 85, 85]),
        ("yellow", [190, 175, 80]),
        ("white",  [180, 180, 180]),
    ]

    def cycle_color():
        cur = s.get("snake_color", palette[0][1])
        idx = next((i for i, (_, c) in enumerate(palette) if c == cur), -1)
        s["snake_color"] = palette[(idx + 1) % len(palette)][1]

    def color_label():
        for n, c in palette:
            if c == s["snake_color"]: return f"color: {n}"
        return "color: custom"

    state = {"done": False}
    bw, bh, bx = 260, 44, SCREEN_W//2 - 130
    btns = [
        Button((bx, 160, bw, bh),
               lambda: f"grid: {'on' if s['grid'] else 'off'}",
               lambda: s.update(grid=not s["grid"]),
               colour=COLOR["panel"], fg=COLOR["text"]),
        Button((bx, 276, bw, bh), color_label, cycle_color,
               colour=COLOR["panel"], fg=COLOR["text"]),
        Button((bx, 360, bw, bh), "save & back",
               lambda: state.update(done=True), colour=COLOR["accent"]),
    ]
    while not state["done"]:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                state["done"] = True
            for b in btns: b.handle(ev)
        screen.fill(COLOR["bg"])
        centered(screen, font_title, "settings", 100, COLOR["text"])
        for b in btns: b.draw(screen, font_med)
        pygame.display.flip()
        clock.tick(60)
    save_settings(s)

def leaderboard_screen():
    rows = db.top10()
    state = {"done": False}
    back = Button((SCREEN_W//2 - 70, SCREEN_H - 60, 140, 40), "back",
                  lambda: state.update(done=True), colour=COLOR["panel"], fg=COLOR["text"])
    while not state["done"]:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                state["done"] = True
            back.handle(ev)
        screen.fill(COLOR["bg"])
        centered(screen, font_title, "top 10", 55, COLOR["text"])
        if not rows:
            centered(screen, font_med,
                     "no scores" if db.is_online() else "offline", 220, COLOR["dim"])
        else:
            y = 110
            for i, r in enumerate(rows, 1):
                d = r["played_at"].strftime("%m-%d %H:%M")
                line = f"{i:<2}  {r['username']:<13} {r['score']:>5}  lv{r['level_reached']}  {d}"
                screen.blit(font_small.render(line, True, COLOR["text"]), (30, y))
                y += 24
        back.draw(screen, font_med)
        pygame.display.flip()
        clock.tick(60)

#game loop
def play(name: str, settings: dict):
    g  = gamemod.Game()
    pb = db.personal_best(name)

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key in (pygame.K_UP,    pygame.K_w): g.turn(gamemod.DIR_UP)
                if ev.key in (pygame.K_DOWN,  pygame.K_s): g.turn(gamemod.DIR_DOWN)
                if ev.key in (pygame.K_LEFT,  pygame.K_a): g.turn(gamemod.DIR_LEFT)
                if ev.key in (pygame.K_RIGHT, pygame.K_d): g.turn(gamemod.DIR_RIGHT)
                if ev.key == pygame.K_ESCAPE:
                    return "menu"

        prev = g.score
        g.step()
        draw_board(g, settings, name, pb)
        pygame.display.flip()
        clock.tick(g.get_fps())

        if g.over:
            return game_over_screen(g, name, pb)

def game_over_screen(g: gamemod.Game, name: str, pb: int):
    saved  = db.save_session(name, g.score, g.level)
    new_pb = max(pb, g.score)
    state  = {"a": None}
    bw, bh = 130, 44
    btns = [
        Button((SCREEN_W//2 - 140, SCREEN_H - 110, bw, bh), "retry",
               lambda: state.update(a="retry")),
        Button((SCREEN_W//2 + 10,  SCREEN_H - 110, bw, bh), "menu",
               lambda: state.update(a="menu"), colour=COLOR["panel"], fg=COLOR["text"]),
    ]
    while state["a"] is None:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
            for b in btns: b.handle(ev)
        screen.fill(COLOR["bg"])
        centered(screen, font_title, "game over", 120, COLOR["danger"])
        centered(screen, font_med, f"score  {g.score}",   200, COLOR["text"])
        centered(screen, font_med, f"level  {g.level}",   232, COLOR["text"])
        centered(screen, font_med, f"best   {new_pb}",    264, COLOR["accent"])
        if not saved:
            centered(screen, font_small, "score not saved (offline)", 300, COLOR["dim"])
        for b in btns: b.draw(screen, font_med)
        pygame.display.flip()
        clock.tick(60)
    return state["a"]

#entry point
def run():
    db.init_schema()
    settings = load_settings()
    name = None

    while True:
        action = main_menu()
        if action == "play":
            if not name:
                name = prompt_username()
            while True:
                result = play(name, settings)
                if result != "retry":
                    break
        elif action == "board":
            leaderboard_screen()
        elif action == "settings":
            settings_screen(settings)
        else:
            pygame.quit()
            return

if __name__ == "__main__":
    run()