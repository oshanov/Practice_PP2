from __future__ import annotations
import random
from collections import deque
import pygame

from config import (
    GRID_W, GRID_H, BASE_FPS, LEVEL_FOOD_STEP, SPEED_PER_LEVEL,
    OBSTACLE_LEVEL, OBSTACLES_PER_LV,
    POISON_PROBABILITY, POWERUP_LIFETIME_MS,
    POWERUP_DURATION_MS, POWERUP_SPAWN_CHANCE_PER_FOOD,
)

DIR_UP = (0, -1)
DIR_DOWN = (0, 1)
DIR_LEFT = (-1, 0)
DIR_RIGHT = (1, 0)


class Food:
    def __init__(self, pos, kind, value=1, points=10, expires_at=0):
        self.pos = pos
        self.kind = kind
        self.value = value
        self.points = points
        self.expires_at = expires_at


class PowerUp:
    def __init__(self, pos, kind, spawned_at):
        self.pos = pos
        self.kind = kind
        self.spawned_at = spawned_at


class Game:
    def __init__(self):
        self.snake = deque([
            (GRID_W // 2, GRID_H // 2),
            (GRID_W // 2 - 1, GRID_H // 2),
            (GRID_W // 2 - 2, GRID_H // 2)
        ])

        self.dir = DIR_RIGHT
        self.next_dir = DIR_RIGHT

        self.score = 0
        self.level = 1
        self.foods_eaten = 0
        self.over = False

        self.foods = []
        self.powerup = None
        self.obstacles = set()

        self.effect = None
        self.effect_until = 0
        self.shield_active = False

        self._regenerate_obstacles()
        self._spawn_food()

    # ───────── FPS (ВМЕСТО @property) ─────────
    def get_fps(self):
        base = BASE_FPS + (self.level - 1) * SPEED_PER_LEVEL

        if self.effect == "speed":
            base += 5
        elif self.effect == "slow":
            base = max(3, base - 4)

        return base

    # ───────── TURN ─────────
    def turn(self, d):
        if (d[0] + self.dir[0], d[1] + self.dir[1]) != (0, 0):
            self.next_dir = d

    # ───────── STEP ─────────
    def step(self):
        if self.over:
            return

        now = pygame.time.get_ticks()

        if self.effect and self.effect != "shield" and now > self.effect_until:
            self.effect = None

        if self.powerup and now - self.powerup.spawned_at > POWERUP_LIFETIME_MS:
            self.powerup = None

        self.foods = [
            f for f in self.foods
            if f.expires_at == 0 or f.expires_at > now
        ]

        self.dir = self.next_dir

        head = self.snake[0]
        new_head = (head[0] + self.dir[0], head[1] + self.dir[1])

        if not (0 <= new_head[0] < GRID_W and 0 <= new_head[1] < GRID_H):
            if self._consume_shield():
                return
            self.over = True
            return

        if new_head in self.obstacles:
            if self._consume_shield():
                return
            self.over = True
            return

        if new_head in list(self.snake)[:-1]:
            if self._consume_shield():
                return
            self.over = True
            return

        self.snake.appendleft(new_head)

        ate = self._food_at(new_head)

        if ate:
            if ate.kind == "poison":
                for _ in range(3):
                    if self.snake:
                        self.snake.pop()

                if len(self.snake) <= 1:
                    self.over = True
                    return

            else:
                for _ in range(ate.value - 1):
                    self.snake.append(self.snake[-1])

                self.score += ate.points
                self.foods_eaten += 1
                self._maybe_level_up()

                if random.random() < POWERUP_SPAWN_CHANCE_PER_FOOD and not self.powerup:
                    self._spawn_powerup()

            self.foods.remove(ate)
            self._spawn_food()
        else:
            self.snake.pop()

        if self.powerup and new_head == self.powerup.pos:
            self._activate_powerup(self.powerup.kind)
            self.powerup = None

    # ───────── HELPERS ─────────
    def _food_at(self, pos):
        for f in self.foods:
            if f.pos == pos:
                return f
        return None

    def _consume_shield(self):
        if self.shield_active:
            self.shield_active = False
            self.effect = None
            return True
        return False

    def _maybe_level_up(self):
        new_level = 1 + self.foods_eaten // LEVEL_FOOD_STEP
        if new_level > self.level:
            self.level = new_level
            self._regenerate_obstacles()

    # ───────── SPAWN ─────────
    def _free_cells(self):
        used = set(self.snake) | self.obstacles | {f.pos for f in self.foods}
        if self.powerup:
            used.add(self.powerup.pos)

        all_cells = {
            (x, y)
            for x in range(GRID_W)
            for y in range(GRID_H)
        }
        return all_cells - used

    def _spawn_food(self):
        free = self._free_cells()
        if not free:
            return

        has_regular = any(f.kind != "poison" for f in self.foods)
        kind_roll = random.random()
        now = pygame.time.get_ticks()

        if not has_regular or kind_roll < 0.55:
            kind, value, points, expires = "small", 1, 10, 0
        elif kind_roll < 0.75:
            kind, value, points, expires = "big", 2, 25, now + 6000
        elif kind_roll < 0.75 + POISON_PROBABILITY:
            kind, value, points, expires = "poison", 0, 0, 0
        else:
            kind, value, points, expires = "small", 1, 10, 0

        self.foods.append(
            Food(random.choice(list(free)), kind, value, points, expires)
        )

    def _spawn_powerup(self):
        free = self._free_cells()
        if not free:
            return

        kind = random.choice(["speed", "slow", "shield"])
        self.powerup = PowerUp(
            random.choice(list(free)),
            kind,
            pygame.time.get_ticks()
        )

    def _activate_powerup(self, kind):
        self.effect = kind

        if kind == "shield":
            self.shield_active = True
            self.effect_until = 0
        else:
            self.effect_until = pygame.time.get_ticks() + POWERUP_DURATION_MS

    # ───────── OBSTACLES ─────────
    def _regenerate_obstacles(self):
        self.obstacles.clear()

        if self.level < OBSTACLE_LEVEL:
            return

        count = OBSTACLES_PER_LV + (self.level - OBSTACLE_LEVEL) * 2

        forbidden = set(self.snake)
        head = self.snake[0]

        for dx in range(-3, 4):
            for dy in range(-3, 4):
                forbidden.add((head[0] + dx, head[1] + dy))

        all_cells = {
            (x, y)
            for x in range(GRID_W)
            for y in range(GRID_H)
        }

        candidates = list(all_cells - forbidden)
        random.shuffle(candidates)

        self.obstacles = set(candidates[:count])

        self.foods = [
            f for f in self.foods
            if f.pos not in self.obstacles
        ]