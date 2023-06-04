from PIL import Image
import imagehash
import distance

def hamming_dis():
    """function which prints the hamming distance between tow images (calculate similarity)"""

    hash1 = imagehash.phash(Image.open("car1.png"))
    hash2 = imagehash.phash(Image.open("car2.png"))

    hash1 = str(hash1)
    hash2 = str(hash2)

    return (distance.hamming(hash1,hash2))

if __name__ == "__main__":
    result = hamming_dis()
    # print(hamming_dis.__doc__)
    print(result)
