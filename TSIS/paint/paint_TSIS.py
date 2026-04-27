import pygame
import datetime
import math

#Constants
SCREEN_W, SCREEN_H = 640, 480
TOOLBAR_H = 40           
CANVAS_H  = SCREEN_H - TOOLBAR_H   #Canvas` height

#Colors
COLORS = [
    (255, 255, 255),   #White
    (255,   0,   0),   #Red
    (  0, 255,   0),   #Green
    (100, 100, 255),   #Blue
    (255, 255,   0),   #Yellow
    (255, 165,   0),   #Orange
]
COLOR_NAMES = ['white', 'red', 'green', 'blue', 'yellow', 'orange']

SIZES     = [2, 5, 10]
SIZE_NAMES = ['S', 'M', 'L']


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption('Paint')
    clock = pygame.time.Clock()

    size_idx  = 1
    radius    = SIZES[size_idx]
    color_idx = 3
    color     = COLORS[color_idx]

    mode = 'pen'

    points      = []
    shape_start = None
    line_preview_start = None

    text_active = False
    text_pos    = (0, 0)
    text_buffer = ''

    #Need canvas for rendering. Not full screen
    canvas = pygame.Surface((SCREEN_W, CANVAS_H))
    canvas.fill((0, 0, 0))

    font      = pygame.font.SysFont('Arial', 13)
    text_font = pygame.font.SysFont('Arial', 20)

    while True:
        pressed   = pygame.key.get_pressed()
        alt_held  = pressed[pygame.K_LALT]  or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); quit()

            #KEYBOARD-------------------------------------------------------
            if event.type == pygame.KEYDOWN:

                if text_active:
                    if event.key == pygame.K_RETURN:
                        surf = text_font.render(text_buffer, True, color)
                        canvas.blit(surf, text_pos)
                        text_active = False 
                        text_buffer = ''
                    elif event.key == pygame.K_ESCAPE:
                        text_active = False
                        text_buffer = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text_buffer = text_buffer[:-1]
                    else:
                        if event.unicode and event.unicode.isprintable():
                            text_buffer += event.unicode
                    continue

                if event.key == pygame.K_w and ctrl_held: return
                if event.key == pygame.K_F4 and alt_held: return
                if event.key == pygame.K_ESCAPE:          return

                #Saving
                if event.key == pygame.K_s and ctrl_held:
                    ts    = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                    fname = f'canvas_{ts}.png'
                    pygame.image.save(canvas, fname)
                    pygame.display.set_caption(f'Paint - saved: {fname}')

                #Instruments
                if event.key == pygame.K_p: mode = 'pen'
                if event.key == pygame.K_l: mode = 'line'
                if event.key == pygame.K_r: mode = 'rect'
                if event.key == pygame.K_c: mode = 'circle'
                if event.key == pygame.K_e: mode = 'eraser'
                if event.key == pygame.K_f: mode = 'fill'
                if event.key == pygame.K_t: mode = 'text'
                if event.key == pygame.K_q: mode = 'square'
                if event.key == pygame.K_i: mode = 'rtriangle'
                if event.key == pygame.K_u: mode = 'etriangle'
                if event.key == pygame.K_h: mode = 'rhombus'
                if event.key == pygame.K_k: mode = 'colorpick'

                #Sizes by 1-2-3
                if event.key == pygame.K_1: size_idx = 0; radius = SIZES[0]
                if event.key == pygame.K_2: size_idx = 1; radius = SIZES[1]
                if event.key == pygame.K_3: size_idx = 2; radius = SIZES[2]

                if event.key == pygame.K_DELETE:
                    canvas.fill((0, 0, 0))

            #MOUSE----------------------------------------------------
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos #Mouse click position

                #Click on toolbar
                if my >= CANVAS_H:
                    hit = toolbar_hit(mx, my)
                    if hit == 'color':
                        #Which color?
                        color_idx = toolbar_color_index(mx)
                        if color_idx is not None:
                            color = COLORS[color_idx]
                    elif hit == 'size':
                        idx = toolbar_size_index(mx)
                        if idx is not None:
                            size_idx = idx
                            radius   = SIZES[size_idx]
                    continue

                #Canvas click
                canvas_pos = (mx, my)
                if mode == 'fill':
                    flood_fill_scanline(canvas, canvas_pos, color)
                elif mode == 'text':
                    text_pos = canvas_pos
                    text_active = True 
                    text_buffer = ''
                elif mode == 'line':
                    line_preview_start = canvas_pos
                elif mode == 'colorpick':
                    if 0 <= my < CANVAS_H:#Checking click on canvas
                        picked    = canvas.get_at(canvas_pos)[:3]#(R,G,B,A) we dont need A
                        color     = picked
                        if picked in COLORS:
                            color_idx = COLORS.index(picked)
                    mode = 'pen'
                else:
                    shape_start = canvas_pos
                    points      = [canvas_pos]

            #Mouse unclick
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mx, my = event.pos
                if my >= CANVAS_H:
                    shape_start = None
                    line_preview_start = None
                    points = []
                    continue

                canvas_pos = (mx, my)#Unclick

                if mode == 'line' and line_preview_start:
                    pygame.draw.line(canvas, color, line_preview_start, canvas_pos, radius)
                    line_preview_start = None
                elif shape_start:
                    sx, sy = shape_start
                    ex, ey = canvas_pos
                    draw_shape(canvas, mode, sx, sy, ex, ey, color, radius)
                    shape_start = None; points = []

            #Mouse motion
            if event.type == pygame.MOUSEMOTION:
                mx, my = event.pos
                if event.buttons[0] and my < CANVAS_H:
                    canvas_pos = (mx, my)
                    points.append(canvas_pos)
                    if mode == 'pen' and len(points) >= 2:
                        pygame.draw.line(canvas, color, points[-2], points[-1], radius)
                    elif mode == 'eraser':
                        pygame.draw.circle(canvas, (0,0,0), canvas_pos, radius * 2)

        #Render--------------------------------------
        screen.blit(canvas, (0, 0))

        #Prelook line
        if mode == 'line' and line_preview_start:
            mx, my = pygame.mouse.get_pos()
            if my < CANVAS_H:
                pygame.draw.line(screen, color, line_preview_start, (mx, my), radius)

        #Prelook figure
        if shape_start and pygame.mouse.get_pressed()[0]:
            sx, sy = shape_start
            mx, my = pygame.mouse.get_pos()
            if my < CANVAS_H:
                draw_shape(screen, mode, sx, sy, mx, my, color, radius)

        #Prelook text
        if text_active:
            preview_surf = text_font.render(text_buffer + '|', True, color)
            screen.blit(preview_surf, text_pos)

        #For toolbar
        draw_toolbar(screen, font, color_idx, size_idx, mode, color, COLORS, COLOR_NAMES, SIZE_NAMES, SIZES)

        pygame.display.flip()
        clock.tick(60)

COLOR_START_X = 8   #First square`s x-coord(from left side)
COLOR_BOX_W   = 28  #Every square`s width,height
COLOR_BOX_H   = 28
COLOR_BOX_GAP = 4

SIZE_START_X  = 8 + 6 * (COLOR_BOX_W + COLOR_BOX_GAP) + 12   #Size squares x-coord (8 + 6sq + 12)

def draw_toolbar(screen, font, color_idx, size_idx, mode, color, COLORS, COLOR_NAMES, SIZE_NAMES, SIZES):
    tb_y = CANVAS_H   #Y-coord of toolbar - end of canvas
    #Toolbar`s BG:very dark grey, border:dark-grey
    pygame.draw.rect(screen, (30, 30, 30), (0, tb_y, SCREEN_W, TOOLBAR_H))
    pygame.draw.line(screen, (80, 80, 80), (0, tb_y), (SCREEN_W, tb_y), 1)

    box_y = tb_y + (TOOLBAR_H - COLOR_BOX_H) // 2 #Toolbars center

    #Colors
    for i, c in enumerate(COLORS):
        x = COLOR_START_X + i * (COLOR_BOX_W + COLOR_BOX_GAP)
        pygame.draw.rect(screen, c, (x, box_y, COLOR_BOX_W, COLOR_BOX_H))
        #If color is chosen
        border_color = (255, 255, 255) if i == color_idx else (80, 80, 80)
        border_w     = 3               if i == color_idx else 1
        pygame.draw.rect(screen, border_color, (x, box_y, COLOR_BOX_W, COLOR_BOX_H), border_w)

    #Sizes
    for i, name in enumerate(SIZE_NAMES):
        x = SIZE_START_X + i * 28
        bg = (70, 70, 120) if i == size_idx else (50, 50, 50)
        pygame.draw.rect(screen, bg, (x, box_y, 24, COLOR_BOX_H))
        pygame.draw.rect(screen, (100, 100, 100), (x, box_y, 24, COLOR_BOX_H), 1)
        lbl = font.render(name, True, (220, 220, 220))
        screen.blit(lbl, (x + 24//2 - lbl.get_width()//2, box_y + COLOR_BOX_H//2 - lbl.get_height()//2))

    #Hints and mode
    info_x = SIZE_START_X + 3 * 28 + 14
    mode_surf = font.render(f'Mode: {mode}', True, (200, 200, 200))
    screen.blit(mode_surf, (info_x, tb_y + 4))
    hint_surf = font.render('P/L/R/C/E/F/T/Q/I/U/H/K  |  1-3 size  |  DEL clear  |  Ctrl+S save', True, (120, 120, 120))
    screen.blit(hint_surf, (info_x, tb_y + 22))

#Returns color, size or None by checking boundaries
def toolbar_hit(mx, my):
    box_y = CANVAS_H + (TOOLBAR_H - COLOR_BOX_H) // 2 #Toolbars center
    if box_y <= my <= box_y + COLOR_BOX_H:
        if COLOR_START_X <= mx <= COLOR_START_X + 6 * (COLOR_BOX_W + COLOR_BOX_GAP):
            return 'color'
        if SIZE_START_X <= mx <= SIZE_START_X + 3 * 28:
            return 'size'
    return None
#Check if mouse pressed between lef-right sides of color or size
#If didnt - None
def toolbar_color_index(mx):
    for i in range(6):
        x = COLOR_START_X + i * (COLOR_BOX_W + COLOR_BOX_GAP)
        if x <= mx <= x + COLOR_BOX_W:
            return i
    return None
def toolbar_size_index(mx):
    for i in range(3):
        x = SIZE_START_X + i * 28
        if x <= mx <= x + 24:
            return i
    return None


#Figures` draw 
def draw_shape(surface, mode, sx, sy, ex, ey, color, radius):
    if mode == 'rect':
        x, y = min(sx,ex), min(sy,ey)
        pygame.draw.rect(surface, color, (x, y, abs(ex-sx), abs(ey-sy)), radius)

    elif mode == 'circle':
        cx = (sx+ex)//2; cy = (sy+ey)//2
        r  = max(abs(ex-sx), abs(ey-sy)) // 2
        if r > 0:
            pygame.draw.circle(surface, color, (cx,cy), r, radius)

    elif mode == 'square':
        side = min(abs(ex-sx), abs(ey-sy))
        x = sx if ex >= sx else sx - side
        y = sy if ey >= sy else sy - side
        pygame.draw.rect(surface, color, (x, y, side, side), radius)

    elif mode == 'rtriangle':
        pts = [(sx, ey), (sx, sy), (ex, ey)]
        pygame.draw.polygon(surface, color, pts, radius)

    elif mode == 'etriangle':
        base   = abs(ex - sx)
        height = int(base * math.sqrt(3) / 2)
        mid_x  = (sx + ex) // 2
        pts = [(sx, ey), (ex, ey), (mid_x, ey - height)]
        pygame.draw.polygon(surface, color, pts, radius)

    elif mode == 'rhombus':
        cx = (sx+ex)//2
        cy = (sy+ey)//2
        pts = [(cx,sy), (ex,cy), (cx,ey), (sx,cy)]
        pygame.draw.polygon(surface, color, pts, radius)


#Flood fill
def flood_fill_scanline(surface, start_pos, fill_color):
    x0, y0 = start_pos
    W, H   = surface.get_size()
    target = surface.get_at((x0, y0))[:3]

    if target == tuple(fill_color[:3]):
        return

    stack = [(x0, y0)]

    while stack:
        x, y = stack.pop()
        if not (0 <= y < H):
            continue
        if surface.get_at((x, y))[:3] != target:
            continue

        #Going left until different color or boudary
        x_left = x
        while x_left > 0 and surface.get_at((x_left - 1, y))[:3] == target:
            x_left -= 1
        #Going right until different color or boudary
        x_right = x
        while x_right < W - 1 and surface.get_at((x_right + 1, y))[:3] == target:
            x_right += 1
        #Draw full line
        pygame.draw.line(surface, fill_color, (x_left, y), (x_right, y))

        for nx in range(x_left, x_right + 1):
            if y > 0     and surface.get_at((nx, y - 1))[:3] == target:
                stack.append((nx, y - 1))
            if y < H - 1 and surface.get_at((nx, y + 1))[:3] == target:
                stack.append((nx, y + 1))


main()