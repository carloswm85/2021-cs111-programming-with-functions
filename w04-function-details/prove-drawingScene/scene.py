# sky, the ground, and clouds.
import tkinter as tk
from random import random, seed, randint

# MAIN PROGRAM


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame, bg='steelBlue1')
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()

# FUNCTION DEFINITION


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """

    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.


    # CLOUDS
    cloud_count = randint(10, 25)
    print(f'Cloud count: {cloud_count}')
    draw_random_clouds(canvas, scene_right, scene_bottom, cloud_count)
    
    # # GROUND
    draw_ground(canvas, scene_right, scene_bottom)

    # TREE
    tree_center = scene_right * 0.8
    tree_top = scene_bottom - scene_bottom * 0.5
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    # # RANDOM TREES
    tree_count = randint(500, 1200)
    tree_max_height = 150
    # """ Draw random pine trees at random locations."""
    draw_random_pine_trees(canvas, scene_right, scene_bottom, tree_max_height,tree_count)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.
def draw_ground(canvas, scene_right, scene_bottom):
    ground_left = 0
    ground_top = scene_bottom * 0.7
    ground_right = scene_right
    ground_bottom = scene_bottom
    canvas.create_rectangle(ground_left, ground_top,
                            ground_right, ground_bottom,
                            outline="black", width=1, fill="green")

def draw_random_clouds(canvas, scene_right, scene_bottom, cloud_count=1, cloud_size=30):
    limit_sky_bottom = int(scene_bottom * 0.7)
    for i in range(cloud_count):
        i = i + 1
        scene_right_random = randint(0, scene_right)
        scene_bottom_random = randint(0, limit_sky_bottom)
        cloud_size_random = randint(cloud_size, cloud_size * 3)
        
        scene_left_random = scene_right_random - cloud_size_random
        scene_top_random = scene_bottom_random - cloud_size_random
        cloud_random_width = random() + 1
        scene_right_random = scene_right_random * cloud_random_width

        canvas.create_oval(scene_left_random, scene_top_random, scene_right_random,
                           scene_bottom_random, width=0, fill="snow")

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
                            trunk_right, trunk_bottom,
                            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
                          skirt_right, skirt_bottom,
                          skirt_left, skirt_bottom,
                          outline="gray20", width=1, fill="dark green")

def draw_random_pine_trees(canvas, peak_x, peak_y, height, tree_count):
    print(canvas, peak_x, peak_y, height, tree_count)
    limit_sky_bottom = int(peak_y * 0.6)
    random_peak_y = limit_sky_bottom
    print(limit_sky_bottom)
    for i in range(tree_count):
        if limit_sky_bottom < peak_y:
            random_height = randint(50, height)
            trunk_width = random_height / 10
            trunk_height = random_height / 8

            # Random peak coordinates
            random_peak_x = randint(0, peak_x)
            # random_peak_y = randint(limit_sky_bottom, peak_y)
            random_peak_y = random_peak_y + 5

            # Trung                
            trunk_left = random_peak_x - trunk_width / 2
            trunk_right = random_peak_x + trunk_width / 2
            trunk_bottom = random_peak_y + random_height

            # Skirt
            skirt_width = random_height / 2
            skirt_height = random_height - trunk_height
            skirt_left = random_peak_x - skirt_width / 2
            skirt_right = random_peak_x + skirt_width / 2
            skirt_bottom = random_peak_y + skirt_height

            # Draw the trunk of the pine tree.
            canvas.create_rectangle(trunk_left, skirt_bottom,
                                    trunk_right, trunk_bottom,
                                    outline="gray20", width=1, fill="tan3")

            # Draw the crown (also called skirt) of the pine tree.
            canvas.create_polygon(random_peak_x, random_peak_y,
                                skirt_right, skirt_bottom,
                                skirt_left, skirt_bottom,
                                outline="gray20", width=1, fill="dark green")

# Call the main function so that
# this program will start executing.
if __name__ == '__main__':
    main()

""" W03 Assignment
During this lesson, you will write code that draws:
   - the sky,
   - the ground,
   - and clouds. 
During the next lesson, you will write code that completes the scene. The scene that your program draws may be very different from the example scene above. However, your scene must:
    - be outdoor,
    - the sky must have clouds,
    - and the scene must include repetitive elements such as blades of grass, trees, leaves on a tree, birds, flowers, insects, fish, pickets in a fence, dashed lines on a road, buildings, bales of hay, snowmen, snowflakes, or icicles. Be creative.
"""
