import pygame
import random
import json
import os

pygame.init()
pygame.mixer.init()

#Config
WIDTH, HEIGHT = 500, 700
FPS = 60
BASE_ROAD_SCROLL = 6   
FONT     = pygame.font.SysFont("Arial", 20)
FONT_SM  = pygame.font.SysFont("Arial", 16)
BIG      = pygame.font.SysFont("Arial", 44, bold=True)
MED      = pygame.font.SysFont("Arial", 28, bold=True)

#Colors
WHITE   = (255, 255, 255)
BLACK   = (0,   0,   0  )
RED     = (200, 0,   0  )
GREEN   = (0,   200, 0  )
BLUE    = (0,   120, 255)
ORANGE  = (255, 140, 0  )
GRAY    = (120, 120, 120)
DGRAY   = (60,  60,  60 )
YELLOW  = (255, 215, 0  )
SILVER  = (192, 192, 192)
BRONZE  = (205, 127, 50 )
PURPLE  = (140, 0,   200)

SHIELD_COLOR = (0,   120, 255)
NITRO_COLOR  = (255, 140, 0  )
REPAIR_COLOR = (200, 0,   0  )

#Files
LEADERBOARD_FILE = "leaderboard.json"
SETTINGS_FILE    = "settings.json"

#Def. settings
DEFAULT_SETTINGS = {
    "sound":      True,
    "car_color":  "default",
    "difficulty": "normal"
}

#Difficulty
DIFFICULTY_PARAMS = {
    "easy":   {"enemy_speed": 3, "spawn_chance": 0.03},
    "normal": {"enemy_speed": 4, "spawn_chance": 0.05},
    "hard":   {"enemy_speed": 6, "spawn_chance": 0.08},
}

CAR_COLORS = {
    "default": None,
    "red":     (220, 60,  60 ),
    "blue":    (60,  100, 220),
    "green":   (60,  200, 80 ),
    "purple":  (160, 60,  220),
}

#images
ROAD = pygame.transform.scale(
    pygame.image.load(r"C:\git_practice\TSIS\racer\assets\AnimatedStreet.png"),
    (WIDTH, HEIGHT))
PLAYER_IMG_BASE = pygame.transform.scale(
    pygame.image.load(r"C:\git_practice\TSIS\racer\assets\player.png"),
    (50, 90))
ENEMY_IMG = pygame.transform.scale(
    pygame.image.load(r"C:\git_practice\TSIS\racer\assets\enemy.png"),
    (50, 90))
COIN_IMG = pygame.transform.scale(
    pygame.image.load(r"C:\git_practice\TSIS\racer\assets\coin.png"),
    (24, 24))


def tinted_surface(base: pygame.Surface, color: tuple) -> pygame.Surface:
    tinted = base.copy().convert_alpha()
    overlay = pygame.Surface(tinted.get_size(), pygame.SRCALPHA)
    overlay.fill(color + (160,))
    tinted.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return tinted


def load_settings() -> dict:
    if os.path.exists(SETTINGS_FILE):
        try:
            data = json.load(open(SETTINGS_FILE))
            for k, v in DEFAULT_SETTINGS.items():
                data.setdefault(k, v)
            return data
        except Exception:
            pass
    return DEFAULT_SETTINGS.copy()


def save_settings(data: dict):
    json.dump(data, open(SETTINGS_FILE, "w"), indent=4)

def load_lb() -> list:
    if os.path.exists(LEADERBOARD_FILE):
        try:
            return json.load(open(LEADERBOARD_FILE))
        except Exception:
            pass
    return []

def save_lb(data: list):
    json.dump(data, open(LEADERBOARD_FILE, "w"), indent=4)

#Button
class Button:
    def __init__(self, x, y, w, h, text, color=GRAY, hover_color=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, s):
        pygame.draw.rect(s, GRAY, self.rect)
        s.blit(FONT.render(self.text, True, WHITE), (self.rect.x + 10, self.rect.y + 10))

    def click(self, pos) -> bool:
        return self.rect.collidepoint(pos)

class ToggleButton(Button):
    def __init__(self, x, y, w, h, label: str, state: bool):
        super().__init__(x, y, w, h, label)
        self.label = label
        self.state = state

    def draw(self, s):
        pygame.draw.rect(s, GRAY, self.rect)
        val = "ON" if self.state else "OFF"
        s.blit(FONT.render(f"{self.label}: {val}", True, WHITE),
               (self.rect.x + 10, self.rect.y + 10))

    def toggle(self):
        self.state = not self.state

#Entities
class Player:
    NITRO_MULT = 1.8  

    def __init__(self, car_img):
        self.img    = car_img
        self.x      = WIDTH // 2
        self.y      = HEIGHT - 120
        self.speed  = 6
        self.hp     = 3
        self.shield = 0
        self.nitro  = 0

    def reset(self, car_img=None):
        if car_img:
            self.img = car_img
        self.x      = WIDTH // 2
        self.y      = HEIGHT - 120
        self.hp     = 3
        self.shield = 0
        self.nitro  = 0

    def move(self, dx, dy, nitro_active=False):
        spd = self.speed * self.NITRO_MULT if nitro_active else self.speed
        self.x += dx * spd
        self.y += dy * spd
        self.x = max(0, min(WIDTH - 50, self.x))
        self.y = max(0, min(HEIGHT - 100, self.y))

    def update(self):
        if self.shield > 0: self.shield -= 1
        if self.nitro  > 0: self.nitro  -= 1

    def draw(self, s):
        s.blit(self.img, (self.x, self.y))
        if self.shield > 0:
            pygame.draw.circle(s, SHIELD_COLOR, (self.x + 25, self.y + 40), 50, 2)
        if self.nitro > 0:
            pygame.draw.circle(s, NITRO_COLOR, (self.x + 25, self.y + 40), 55, 3)

class Coin:
    VALUE = 5
    SIZE  = 24

    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -self.SIZE

    def update(self, scroll): self.y += scroll

    def draw(self, s):
        s.blit(COIN_IMG, (self.x - self.SIZE // 2, int(self.y) - self.SIZE // 2))

class Enemy:
    def __init__(self, speed):
        self.x     = random.randint(50, WIDTH - 100)
        self.y     = -100
        self.speed = speed


    def update(self, extra=0): self.y += self.speed + extra
    def draw(self, s): s.blit(ENEMY_IMG, (self.x, self.y))

class Obstacle:
    def __init__(self, t):
        self.x = random.randint(50, WIDTH - 100)
        self.y = -50
        self.t = t

    def update(self, scroll): self.y += scroll

    def draw(self, s):
        if   self.t == "barrier":    pygame.draw.rect(s, BLACK,  (self.x, self.y, 50, 20))
        elif self.t == "speed_bump": pygame.draw.rect(s, GRAY,   (self.x, self.y, 50, 20))
        elif self.t == "boost":      pygame.draw.rect(s, GREEN,  (self.x, self.y, 50, 20))

class PowerUp:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = -40
        self.t = random.choice(["shield", "nitro", "repair"])

    def update(self, scroll): self.y += scroll

    def draw(self, s):
        c = SHIELD_COLOR if self.t == "shield" else NITRO_COLOR if self.t == "nitro" else REPAIR_COLOR
        pygame.draw.circle(s, c, (self.x, int(self.y)), 12)

#Game
class Game:
    SPAWN_MIN_DIST = 80
    NITRO_SCROLL   = 11   
    BASE_SCROLL    = 6    

    def __init__(self):
        self.s = pygame.display.set_mode((WIDTH, HEIGHT))
        self.c = pygame.time.Clock()
        pygame.display.set_caption("RACER")

        self.settings    = load_settings()
        self.player_img  = self._build_car_img()
        self.player      = Player(self.player_img)
        self.state       = "menu"
        self.coins_total = 0

        self.reset_game()
        self._build_buttons()

    def _build_car_img(self) -> pygame.Surface:
        color = CAR_COLORS[self.settings.get("car_color", "default")]
        if color is None:
            return PLAYER_IMG_BASE.copy()
        return tinted_surface(PLAYER_IMG_BASE, color)

    def _build_buttons(self):
        cx = WIDTH // 2
        BW, BH = 160, 42

        def btn(y, text, color=GRAY):
            return Button(cx - BW // 2, y, BW, BH, text, color)

        self.buttons = {
            "play":        btn(200, "PLAY"),
            "lb":          btn(255, "LEADERBOARD"),
            "settings":    btn(310, "SETTINGS"),
            "quit":        btn(365, "QUIT"),
            "retry":       btn(430, "RESTART"),
            "back":        btn(485, "MENU"),
            "back2":       Button(cx - BW // 2, 620, BW, BH, "BACK"),
            "diff_easy":   Button(cx - 200, 300, 110, 38, "EASY"),
            "diff_normal": Button(cx -  55, 300, 110, 38, "NORMAL"),
            "diff_hard":   Button(cx +  90, 300, 110, 38, "HARD"),
            "col_default": Button(cx - 210, 410, 70, 34, "DEF"),
            "col_red":     Button(cx - 130, 410, 70, 34, "RED"),
            "col_blue":    Button(cx -  50, 410, 70, 34, "BLUE"),
            "col_green":   Button(cx +  30, 410, 70, 34, "GREEN"),
            "col_purple":  Button(cx + 110, 410, 70, 34, "PURPLE"),
        }

        self.snd_btn = ToggleButton(cx - BW // 2, 220, BW, BH,
                                    "SOUND", self.settings["sound"])

    def reset_game(self):
        self.coins        = []
        self.enemies      = []
        self.obs          = []
        self.pups         = []
        self.score        = 0
        self.dist         = 0
        self.coins_total  = 0
        diff = self.settings.get("difficulty", "normal")
        self.enemy_speed  = DIFFICULTY_PARAMS[diff]["enemy_speed"]
        self.spawn_chance = DIFFICULTY_PARAMS[diff]["spawn_chance"]
        self.road_scroll  = self.BASE_SCROLL
        self.nitro_active = False

    def _all_objects(self):
        return self.coins + self.enemies + self.obs + self.pups

    def safe_pos(self, y_spawn=-20, max_tries=20):
        for _ in range(max_tries):
            x = random.randint(50, WIDTH - 100)
            if abs(x - self.player.x) < 100:
                continue
            ok = all(
                not (abs(x - o.x) < self.SPAWN_MIN_DIST
                     and abs(y_spawn - o.y) < self.SPAWN_MIN_DIST)
                for o in self._all_objects()
            )
            if ok:
                return x
        return None

    def spawn(self):
        if random.random() < 0.5:
            x = self.safe_pos(-20)
            if x is not None:
                c = Coin(); c.x = x; self.coins.append(c)

        if random.random() < 0.3:
            x = self.safe_pos(-100)
            if x is not None:
                e = Enemy(self.enemy_speed); e.x = x; self.enemies.append(e)

        if random.random() < 0.3:
            x = self.safe_pos(-50)
            if x is not None:
                o = Obstacle(random.choice(["barrier", "speed_bump", "boost"]))
                o.x = x; self.obs.append(o)

        if random.random() < 0.25:
            x = self.safe_pos(-40)
            if x is not None:
                p = PowerUp(); p.x = x; self.pups.append(p)

    def hit(self, a, b):
        return abs(a.x - b.x) < 40 and abs(a.y - b.y) < 60

    def check(self):
        for c in self.coins[:]:
            if self.hit(c, self.player):
                self.score += Coin.VALUE * 10
                self.coins_total += 1
                self.coins.remove(c)

        for e in self.enemies[:]:
            if self.hit(e, self.player):
                if self.player.shield <= 0: self.player.hp -= 1
                self.enemies.remove(e)

        for o in self.obs[:]:
            if self.hit(o, self.player):
                if   o.t == "boost"  : self.enemy_speed += 1
                elif o.t == "barrier" and self.player.shield <= 0: self.player.hp -= 1
                self.obs.remove(o)

        for p in self.pups[:]:
            if self.hit(p, self.player):
                if   p.t == "shield": self.player.shield = 300
                elif p.t == "nitro" : self.player.nitro  = 200; self.enemy_speed += 1
                elif p.t == "repair": self.player.hp = min(3, self.player.hp + 1)
                self.pups.remove(p)

        if self.player.hp <= 0:
            self._save_score()
            self.state = "gameover"

    def _save_score(self):
        data = load_lb()
        data.append({"name": "Player", "score": self.score,
                     "dist": self.dist, "coins": self.coins_total})
        data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]
        save_lb(data)

    def update(self):
        self.dist  += 1
        self.score += 1

        self.nitro_active = self.player.nitro > 0
        self.road_scroll  = self.NITRO_SCROLL if self.nitro_active else self.BASE_SCROLL

        self.player.update()

        for obj in self.coins: obj.update(self.road_scroll)
        for obj in self.obs:   obj.update(self.road_scroll)
        for obj in self.pups:  obj.update(self.road_scroll)

        nitro_extra = (self.NITRO_SCROLL - self.BASE_SCROLL) if self.nitro_active else 0
        for obj in self.enemies: obj.update(nitro_extra)

        self.coins   = [c for c in self.coins   if c.y < HEIGHT]
        self.enemies = [e for e in self.enemies  if e.y < HEIGHT]
        self.obs     = [o for o in self.obs      if o.y < HEIGHT]
        self.pups    = [p for p in self.pups     if p.y < HEIGHT]
        self.check()
        if random.random() < self.spawn_chance:
            self.spawn()

    def draw(self):
        self.s.blit(ROAD, (0, 0))
        self.player.draw(self.s)
        for lst in [self.coins, self.enemies, self.obs, self.pups]:
            for obj in lst: obj.draw(self.s)

        nitro_str = f" NITRO:{self.player.nitro}" if self.nitro_active else ""
        self.s.blit(FONT.render(
            f"Score:{self.score} HP:{self.player.hp} Coins:{self.coins_total} Dist:{self.dist}{nitro_str}",
            True, NITRO_COLOR if self.nitro_active else WHITE), (10, 10))

    def screen_menu(self):
        self.s.fill(BLACK)
        self.s.blit(BIG.render("RACER", True, WHITE), (180, 100))
        for key in ["play", "lb", "settings", "quit"]:
            self.buttons[key].draw(self.s)

    def screen_settings(self):
        self.s.fill(BLACK)
        self.s.blit(BIG.render("SETTINGS", True, WHITE), (150, 40))

        self.s.blit(FONT.render("Sound:", True, WHITE), (30, 160))
        self.snd_btn.draw(self.s)

        self.s.blit(FONT.render("Difficulty:", True, WHITE), (30, 260))
        cur_diff = self.settings["difficulty"]
        for key, val in [("diff_easy","easy"),("diff_normal","normal"),("diff_hard","hard")]:
            self.buttons[key].text = ("*" if cur_diff == val else "") + val.upper()
            self.buttons[key].draw(self.s)

        self.s.blit(FONT.render("Car Color:", True, WHITE), (30, 370))
        cur_col = self.settings["car_color"]
        for key, val in [("col_default","default"),("col_red","red"),
                         ("col_blue","blue"),("col_green","green"),("col_purple","purple")]:
            self.buttons[key].text = ("*" if cur_col == val else "") + val[:3].upper()
            self.buttons[key].draw(self.s)

        self.buttons["back2"].draw(self.s)

    def screen_leaderboard(self):
        self.s.fill(BLACK)
        self.s.blit(BIG.render("LEADERBOARD", True, WHITE), (100, 30))

        self.s.blit(FONT.render("#   Score    Dist  Coins", True, WHITE), (60, 100))
        y = 130
        for i, d in enumerate(load_lb()):
            self.s.blit(FONT.render(
                f"{i+1}.  {d['score']}    {d.get('dist',0)}    {d.get('coins',0)}",
                True, WHITE), (60, y))
            y += 30

        self.buttons["back2"].draw(self.s)

    def screen_gameover(self):
        self.s.fill(BLACK)
        self.s.blit(BIG.render("GAME OVER", True, RED), (120, 180))
        self.s.blit(FONT.render(f"Score:    {self.score}",        True, WHITE), (180, 280))
        self.s.blit(FONT.render(f"Distance: {self.dist}",         True, WHITE), (180, 310))
        self.s.blit(FONT.render(f"Coins:    {self.coins_total}",  True, WHITE), (180, 340))

        lb = load_lb()
        rank = next((i + 1 for i, d in enumerate(lb) if d["score"] == self.score), None)
        if rank:
            self.s.blit(FONT.render(f"Rank: #{rank}", True, WHITE), (180, 380))

        self.buttons["retry"].draw(self.s)
        self.buttons["back"].draw(self.s)

    def run(self):
        running = True
        while running:
            self.c.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos

                    if self.state == "menu":
                        if self.buttons["play"].click(pos):
                            self.player.reset(self._build_car_img())
                            self.reset_game()
                            self.state = "play"
                        elif self.buttons["lb"].click(pos):
                            self.state = "leaderboard"
                        elif self.buttons["settings"].click(pos):
                            self.state = "settings"
                        elif self.buttons["quit"].click(pos):
                            running = False

                    elif self.state == "settings":
                        if self.snd_btn.click(pos):
                            self.snd_btn.toggle()
                            self.settings["sound"] = self.snd_btn.state
                            save_settings(self.settings)
                        for key, val in [("diff_easy","easy"),
                                         ("diff_normal","normal"),
                                         ("diff_hard","hard")]:
                            if self.buttons[key].click(pos):
                                self.settings["difficulty"] = val
                                save_settings(self.settings)
                        for key, val in [("col_default","default"),("col_red","red"),
                                         ("col_blue","blue"),("col_green","green"),
                                         ("col_purple","purple")]:
                            if self.buttons[key].click(pos):
                                self.settings["car_color"] = val
                                save_settings(self.settings)
                        if self.buttons["back2"].click(pos):
                            self.state = "menu"

                    elif self.state == "gameover":
                        if self.buttons["retry"].click(pos):
                            self.player.reset(self._build_car_img())
                            self.reset_game()
                            self.state = "play"
                        elif self.buttons["back"].click(pos):
                            self.state = "menu"

                    elif self.state == "leaderboard":
                        if self.buttons["back2"].click(pos):
                            self.state = "menu"

            if self.state == "play":
                keys = pygame.key.get_pressed()
                dx = dy = 0
                if keys[pygame.K_LEFT]:  dx = -1
                if keys[pygame.K_RIGHT]: dx =  1
                if keys[pygame.K_UP]:    dy = -1
                if keys[pygame.K_DOWN]:  dy =  1
                self.player.move(dx, dy, nitro_active=self.nitro_active)

            if   self.state == "menu":        self.screen_menu()
            elif self.state == "play":        self.update(); self.draw()
            elif self.state == "settings":    self.screen_settings()
            elif self.state == "leaderboard": self.screen_leaderboard()
            elif self.state == "gameover":    self.screen_gameover()

            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    Game().run()