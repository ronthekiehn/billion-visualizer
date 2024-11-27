import argparse
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg
import os

BILLION = 1000000000

def language_visualization(language_data, playback_speed, fps=60, labels=False):
    # Calculate the maximum time based on the slowest language
    max_time = max(lang['time'] for lang in language_data)


    # Adjust animation length by playback speed
    total_duration = max_time / playback_speed
    frames = int(fps * total_duration)  # Determine frames based on playback speed and FPS
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(left=0.3, top=0.9)  # Adjusted top margin for title

    # Load and display logos - with debug information
    logo_size = 0.03  # Adjust this value to change logo size
    script_dir = os.path.dirname(os.path.abspath(__file__))
    logos_dir = os.path.join(script_dir, 'logos')
    
    
    for i, lang in enumerate(language_data):
        logo_path = os.path.join(logos_dir, f"{lang['name'].lower()}.png")
        try:
            if os.path.exists(logo_path):
                img = mpimg.imread(logo_path)
                # Adjusted vertical position to center with bars
                logo_ax = fig.add_axes([0.2, 0.06 + ((i + 1) / (len(language_data) + 1)) / 1.17, logo_size, logo_size])
                logo_ax.imshow(img)
                logo_ax.axis('off')
            else:
                print(f"No logo file found for {lang['name']}")
        except Exception as e:
            print(f"Error loading logo for {lang['name']}: {e}")

    ax.set_xlim(0, 1)
    ax.set_xticks([0, 1])
    ax.set_ylim(-0.5, len(language_data) - 0.5)
    ax.set_yticks(range(len(language_data)))
    
    ax.set_yticklabels([f"{lang['name']}\n{lang['time']:.2f}s" for lang in language_data], ha='right', x=-0.02)


    # Add background patches and conditional labels
    if labels:
        # Add background patches for counter text
        text_backgrounds = [plt.Rectangle((-0.25, i-0.25), 0.15, 0.5, 
                                        facecolor='white', edgecolor='none', 
                                        transform=ax.transData,
                                        zorder=2)
                           for i in range(len(language_data))]
        for patch in text_backgrounds:
            ax.add_patch(patch)
        
        counters = [ax.text(-0.15, i, "0", 
                           verticalalignment='center', 
                           horizontalalignment='right',
                           bbox=dict(facecolor='white', edgecolor='none', pad=1),
                           zorder=3)
                   for i in range(len(language_data))]
    else:
        text_backgrounds = []
        counters = []

        
    balls = [ax.plot([], [], 'o', markersize=20, label=lang['name'])[0] for lang in language_data]

    # Initialization function for animation
    def init():
        for ball in balls:
            ball.set_data([], [])
        if labels:
            for counter in counters:
                counter.set_text("0")
        return balls + counters + text_backgrounds

    # Update function for animation
    def update(frame):
        for idx, (lang, ball) in enumerate(zip(language_data, balls)):
            # Calculate progress for each language based on time taken and frame
            progress = (frame / frames) / (lang['time'] / max_time)
            #print(progress)
            progress = min(progress * BILLION, BILLION)
            # Simulate the "bouncing" motion
            x_pos = progress - int(progress) if int(progress) % 2 == 0 else (1 - (progress - int(progress)))
            ball.set_data([x_pos], [idx])  # x and y must be lists
            
            if labels:
                counters[idx].set_text(f"{int(progress):,}")
        
        return balls + counters + text_backgrounds

    # Create the animation
    anim = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=1000 / fps)
    plt.xlabel("One Loop")
    # Move title to be above the chart area
    ax.set_title("A Billion Loops in Different Langs", pad=20)
    plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--speed", type=float, default=1.0)
    parser.add_argument("--fps", type=int, default=60)
    parser.add_argument("--labels", action="store_true")
    
    args = parser.parse_args()

    # Sample language data: Name and time taken to complete a billion loops (in seconds)
    language_data = [
        {"name": "C", "time": 0.5},
        {"name": "Rust", "time": 0.5},
        {"name": "Java", "time": 0.54},
        {"name": "Kotlin", "time": 0.56},
        {"name": "Go", "time": 0.8},
        {"name": "Bun", "time": 0.8},
        {"name": "Node", "time": 1.03},
        {"name": "Deno", "time": 1.06},
        {"name": "Dart", "time": 1.34},
        {"name": "PyPy", "time": 1.53},
        {"name": "PHP", "time": 9.93},
        {"name": "Ruby", "time": 28.8},
        {"name": "R", "time": 73.16},
        {"name": "Python", "time": 74.42}
        ]

    language_visualization(language_data, args.speed, args.fps, args.labels)

if __name__ == "__main__":
    main()