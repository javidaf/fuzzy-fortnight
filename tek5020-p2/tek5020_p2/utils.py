import cv2


def draw_regions(image, regions):
    """Draw rectangular regions on the image with labels"""
    vis_image = image.copy()

    colors = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]  # Green

    for region, color in zip(regions, colors):
        cv2.rectangle(
            vis_image,
            (region.x1, region.y1),
            (region.x2, region.y2),
            color,
            4,
        )
        label = str(region.label) if hasattr(region, "label") else "Region"
        cv2.putText(
            vis_image,
            label,
            (region.x2, region.y2),
            cv2.FONT_HERSHEY_SIMPLEX,
            4,
            color,
            4,
            cv2.LINE_AA,
        )

    return vis_image
