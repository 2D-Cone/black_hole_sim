import math
import pygame


def world_to_screen(x, y, center_x, center_y, scale):
    screen_x = int(center_x + x * scale)
    screen_y = int(center_y - y * scale)
    return screen_x, screen_y


def draw_glow_circle(surface, color, pos, radius, layers=4):
    x, y = pos

    for i in range(layers, 0, -1):
        alpha = max(20, 80 // i)
        glow_radius = radius * i

        temp = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(
            temp,
            (*color, alpha),
            (glow_radius, glow_radius),
            glow_radius
        )
        surface.blit(temp, (x - glow_radius, y - glow_radius))


def animate_pygame(data):
    pygame.init()
    pygame.font.init()

    width = 1000
    height = 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Black Hole Orbit Sim - Pygame Playback")

    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Menlo", 20)
    small_font = pygame.font.SysFont("Menlo", 16)

    x_history = data["x"]
    y_history = data["y"]
    time_history = data["time"]
    energy_history = data["energy"]
    L_history = data["L"]
    radius_history = data["radius"]
    speed_history = data["speed"]
    horizon_r = data["horizon_r"]
    captured = data["captured"]

    #compute bounds for scaling
    max_extent = max(
        max(abs(min(x_history)), abs(max(x_history))),
        max(abs(min(y_history)), abs(max(y_history))),
        horizon_r
    )

    #leave space for sidebar
    sim_width = width * 0.72
    center_x = int(sim_width / 2)
    center_y = height // 2

    scale = (min(sim_width, height) * 0.40) / max_extent

    #trail settings
    trail_length = 250
    frame = 0
    frame_skip = 8

    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    frame = 0
                    paused = False
                elif event.key == pygame.K_RIGHT:
                    frame = min(frame + 50, len(x_history) - 1)
                elif event.key == pygame.K_LEFT:
                    frame = max(frame - 50, 0)

        if not paused:
            frame += frame_skip
            if frame >= len(x_history):
                frame = len(x_history) - 1
                paused = True

        screen.fill((8, 8, 14))

        #sidebar panel
        sidebar_rect = pygame.Rect(int(width * 0.72), 0, int(width * 0.28), height)
        pygame.draw.rect(screen, (18, 18, 28), sidebar_rect)

        #draw faint full orbit path
        full_path_points = []
        for x, y in zip(x_history, y_history):
            sx, sy = world_to_screen(x, y, center_x, center_y, scale)
            full_path_points.append((sx, sy))

        if len(full_path_points) > 1:
            pygame.draw.lines(screen, (45, 45, 60), False, full_path_points, 1)

        #draw horizon/black hole
        bh_screen = world_to_screen(0, 0, center_x, center_y, scale)
        horizon_px = max(2, int(horizon_r * scale))

        draw_glow_circle(screen, (80, 80, 110), bh_screen, horizon_px, layers=3)
        pygame.draw.circle(screen, (0, 0, 0), bh_screen, horizon_px)
        pygame.draw.circle(screen, (110, 110, 130), bh_screen, horizon_px, 2)

        #trail
        start_idx = max(0, frame - trail_length)
        trail_points = []
        for i in range(start_idx, frame + 1):
            sx, sy = world_to_screen(x_history[i], y_history[i], center_x, center_y, scale)
            trail_points.append((sx, sy))

        if len(trail_points) > 1:
            #draw fading trail segments
            for i in range(1, len(trail_points)):
                fade = i / len(trail_points)
                color_value = int(80 + 150 * fade)
                pygame.draw.line(
                    screen,
                    (80, color_value, 255),
                    trail_points[i - 1],
                    trail_points[i],
                    2
                )

        #current particle
        x = x_history[frame]
        y = y_history[frame]
        sx, sy = world_to_screen(x, y, center_x, center_y, scale)

        draw_glow_circle(screen, (80, 160, 255), (sx, sy), 5, layers=2)
        pygame.draw.circle(screen, (160, 220, 255), (sx, sy), 5)

        #crosshair at center
        pygame.draw.line(screen, (30, 30, 40), (center_x - 10, center_y), (center_x + 10, center_y), 1)
        pygame.draw.line(screen, (30, 30, 40), (center_x, center_y - 10), (center_x, center_y + 10), 1)

        #live readout
        time_val = time_history[frame]
        r_val = radius_history[frame]
        speed_val = speed_history[frame]
        energy_val = energy_history[frame]
        L_val = L_history[frame]

        lines = [
            "BLACK HOLE ORBIT SIM",
            "",
            f"frame      : {frame}",
            f"time       : {time_val:.2f}",
            f"x          : {x:.4f}",
            f"y          : {y:.4f}",
            f"radius     : {r_val:.4f}",
            f"speed      : {speed_val:.4f}",
            f"energy     : {energy_val:.6f}",
            f"Lz         : {L_val:.6f}",
            f"captured   : {captured}",
            "",
            "Controls:",
            "SPACE  pause/resume",
            "R      restart",
            "LEFT   step back",
            "RIGHT  step forward",
            "ESC    quit",
        ]

        y_offset = 30
        for idx, line in enumerate(lines):
            active_font = font if idx == 0 else small_font
            color = (220, 220, 235) if idx == 0 else (180, 180, 200)
            text_surface = active_font.render(line, True, color)
            screen.blit(text_surface, (int(width * 0.75), y_offset))
            y_offset += 30 if idx == 0 else 24

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()