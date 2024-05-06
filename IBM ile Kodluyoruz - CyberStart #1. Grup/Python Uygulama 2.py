points = [(1, 5), (3, 4), (2, 10), (12, 12), (18,6)]  # Örnek olarak 5 nokta belirtildi.

# Öklid Mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # hiçbir kütüphane kullanmamak için Math.sqrt yerine üssü 1/2 kullanma

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)
print("Minimum mesafe: ", min_distance)