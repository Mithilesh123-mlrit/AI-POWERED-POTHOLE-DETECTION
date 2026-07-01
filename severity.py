def classify_severity(width, height):

    area = width * height

    if area < 5000:
        return "Low"

    elif area < 15000:
        return "Medium"

    else:
        return "High"