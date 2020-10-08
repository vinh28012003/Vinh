def convertStringToList(text):
    result = text.split(", ")
    result.sort()
    return result

if __name__ == "__main__":
    convertStringToList()