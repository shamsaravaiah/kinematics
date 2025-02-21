import numpy as np

# Rotation Matrices
def rotation_matrix_x(theta):
    """Rotation matrix for X-axis"""
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

def rotation_matrix_y(theta):
    """Rotation matrix for Y-axis"""
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def rotation_matrix_z(theta):
    """Rotation matrix for Z-axis"""
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])

# Translation Vector
def translation_vector(tx, ty, tz):
    """Translation vector"""
    return np.array([[tx], [ty], [tz]])

# Homogeneous Transformation Matrix
def homogeneous_transformation(R, P):
    """Creates a 4x4 homogeneous transformation matrix"""
    T = np.eye(4)  # Identity matrix (4x4)
    T[:3, :3] = R  # Insert rotation matrix
    T[:3, 3] = P.flatten()  # Insert translation vector
    return T

# Example Usage
if __name__ == "__main__":
    theta = np.radians(90)  # Convert degrees to radians
    R = rotation_matrix_z(theta)  # Rotate 30° around Z-axis
    P = translation_vector(4, -2, 5)  # Move by (5,3,2)

    T = homogeneous_transformation(R, P)  # Final transformation matrix

    # Apply transformation to a point (x, y, z, 1)
    point = np.array([[1], [2], [3], [1]])  # Homogeneous coordinates
    transformed_point = np.dot(T, point)  # Matrix multiplication

    print("Homogeneous Transformation Matrix:\n", T)
    print("\nTransformed Point:\n", transformed_point)
