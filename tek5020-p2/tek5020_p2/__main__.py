import cv2
from matplotlib import pyplot as plt
import numpy as np
from dataclasses import dataclass
import numpy as np
from PIL import Image
from tek5020_p1.classifiers import (
    MinimumErrorRateClassifier,
    LeastSquaresClassifier,
    NearestNeighborClassifier,
)
from tek5020_p2 import draw_regions
import os


def load_image(path):
    image = np.array(Image.open(path))
    if image.shape[-1] == 4:
        image = image[:, :, :3]
    return image


@dataclass
class Region:
    x1: int
    y1: int
    x2: int
    y2: int
    label: int


def extract_features(image, normalize=False):
    """Convert image to feature vectors"""
    # Reshape to (n_pixels, 3) array
    features = image.reshape(-1, 3)

    if normalize:
        # Apply RGB normalization
        rgb_sum = features.sum(axis=1, keepdims=True)
        features = features / (
            rgb_sum + 1e-10
        )  # Adding small number to avoid division by zero
        # Use only R and G components (B is redundant)
        features = features[:, :2]

    return features


def get_training_data(image, regions, normalize=False):
    """Extract training data from specified regions"""
    features_list = []
    labels_list = []

    for region in regions:
        roi = image[region.y1 : region.y2, region.x1 : region.x2]
        features = extract_features(roi, normalize)
        labels = np.full(len(features), region.label)

        features_list.append(features)
        labels_list.append(labels)

    return np.vstack(features_list), np.hstack(labels_list)


def segment_image(image, classifier, normalize=False):
    """Segment entire image using trained classifier"""
    features = extract_features(image, normalize)
    predictions = classifier.predict(features)
    return predictions.reshape(image.shape[0], image.shape[1])


def visualize_segmentation(segmented, n_classes):
    """Create colored visualization of segmentation"""
    colors = np.array([[0, 0, 1], [1, 0, 0], [0.6, 0.3, 0.1]])  # Red  # Blue  # Brown

    result = np.zeros((*segmented.shape, 3))
    for i in range(n_classes):
        mask = segmented == (i + 1)
        result[mask] = colors[i]
    for i in range(n_classes):
        mask = segmented == (i + 1)
        if np.any(mask):
            y_coords, x_coords = np.where(mask)
            center_y = int(np.mean(y_coords))
            center_x = int(np.mean(x_coords))
            right_part_x = x_coords[x_coords > center_x - 50]
            right_part_y = y_coords[y_coords > center_y - 50]
            center_right_x = int(np.mean(right_part_x))
            center_right_y = int(np.mean(right_part_y))

            cv2.putText(
                result,
                f"C{i+1}",
                (center_right_x, center_right_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                6,
                (0, 255, 0),
                12,
            )

    return (result * 255).astype(np.uint8)


if __name__ == "__main__":
    dir = os.path.dirname(__file__)
    data = os.path.join(dir, "..", "tests", "data")
    train_image_path = os.path.join(data, "Bilde2.png")
    test_image_path = os.path.join(data, "Bilde3.png")

    size = 200
    r1 = (950, 1200)
    r2 = (2500, 800)
    r3 = (400, 400)
    regions = [
        Region(r1[0] - size, r1[1] - size, r1[0] + size, r1[1] + size, 1),
        Region(r2[0] - size, r2[1] - size, r2[0] + size, r2[1] + size, 2),
        Region(r3[0] - size, r3[1] - size, r3[0] + size, r3[1] + size, 3),
    ]
    normalize = True
    train_image = load_image(train_image_path)
    X_train, y_train = get_training_data(train_image, regions, normalize)
    classifier = MinimumErrorRateClassifier()
    classifier.fit(X_train, y_train)
    # classifier.print_performance(X_train, y_train)

    train_result = segment_image(train_image, classifier, normalize)
    train_vis = visualize_segmentation(train_result, len(regions))

    test_image = load_image(test_image_path)
    test_result = segment_image(test_image, classifier, normalize)
    test_vis = visualize_segmentation(test_result, len(regions))

    plt.figure(figsize=(10, 8))

    plt.subplot(221)
    train_with_regions = draw_regions(train_image, regions)
    plt.imshow(train_with_regions)
    plt.title("Training Image with Regions")

    # plt.subplot(221)
    # plt.imshow(train_image)
    # plt.title("Training Image (Bilde2)")

    plt.subplot(222)
    plt.imshow(train_vis)
    plt.title("Segmented Training Image")

    plt.subplot(223)
    plt.imshow(test_image)
    plt.title("Test Image (Bilde3)")

    plt.subplot(224)
    plt.imshow(test_vis)
    plt.title("Segmented Test Image")

    plt.tight_layout()
    plt.show()
