import pygame
from random import randint


def update_screen(screen, rects):
    screen.fill((0, 0, 0))
    for rect in rects:
        pygame.draw.rect(screen, (255, 255, 255), rect)
    pygame.display.flip()


def heap_sort(arr, rects, screen):
    def heapify(arr, i, n):
        root = i
        left = 2*i+1
        right = 2*i+2

        if left < n and arr[left] > arr[i]:
            root = left

        if right < n and arr[right] > arr[root]:
            root = right

        if root != i:
            arr[i], arr[root] = arr[root], arr[i]
            rects[i].x, rects[root].x = rects[root].x, rects[i].x
            rects[i], rects[root] = rects[root], rects[i]
            update_screen(screen, rects)
            heapify(arr, root, n)

    n = len(arr)
    start = (n // 2) - 1
    for j in range(n, 0, -1):
        for parent in range(start, -1, -1):
            heapify(arr, parent, j)
        arr[0], arr[j-1] = arr[j-1], arr[0]
        rects[0].x, rects[j-1].x = rects[j-1].x, rects[0].x
        rects[0], rects[j - 1] = rects[j - 1], rects[0]
        update_screen(screen, rects)


def generate_array(n):
    return [randint(0, 100) for _ in range(n)]


def main():
    array = generate_array(300)

    pygame.init()

    win_size = win_width, win_height = 640, 320
    screen = pygame.display.set_mode(win_size)
    pygame.display.set_caption('heap sort visualization')

    shapes = []
    x = win_width / len(array)
    max_y = max(array)
    for i, value in enumerate(array):
        y = (value / max_y) * win_height
        shapes.append(pygame.Rect(i * x, win_height, x+1, -y))

    game_on = True
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

        heap_sort(array, shapes, screen)
        pygame.time.delay(10000)
        break


if __name__ == '__main__':
    main()


