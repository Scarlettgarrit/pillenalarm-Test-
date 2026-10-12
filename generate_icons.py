from PIL import Image, ImageDraw


def make_icon(size, output_path):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Background circle
    bg_color = (37, 99, 235, 255)  # blue
    margin = int(size * 0.12)
    draw.ellipse((margin, margin, size - margin, size - margin), fill=bg_color)

    # Inner white pill capsule
    capsule_w = int(size * 0.62)
    capsule_h = int(size * 0.28)
    capsule_x = (size - capsule_w) // 2
    capsule_y = (size - capsule_h) // 2
    draw.rounded_rectangle(
        (capsule_x, capsule_y, capsule_x + capsule_w, capsule_y + capsule_h),
        radius=int(capsule_h * 0.5),
        fill=(255, 255, 255, 255),
    )

    # Small plus sign / reminder indicator
    plus_size = int(size * 0.18)
    plus_x = size // 2
    plus_y = size // 2
    draw.rounded_rectangle(
        (plus_x - plus_size // 2, plus_y - plus_size * 2, plus_x + plus_size // 2, plus_y + plus_size * 2),
        radius=plus_size // 3,
        fill=bg_color,
    )
    draw.rounded_rectangle(
        (plus_x - plus_size * 2, plus_y - plus_size // 2, plus_x + plus_size * 2, plus_y + plus_size // 2),
        radius=plus_size // 3,
        fill=bg_color,
    )

    img.save(output_path)
    print(f"Created {output_path} ({size}x{size})")


if __name__ == "__main__":
    try:
        import PIL  # noqa: F401
    except ImportError:
        raise SystemExit(
            "Pillow is not installed. Run: pip install pillow"
        )

    make_icon(192, "icon-192.png")
    make_icon(512, "icon-512.png")
    print("Done.")
