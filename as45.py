while True:
    try:
        mp = int(input("How many megapixels does your camera take a photo at?:"))
        resolution = mp * 1000000
        photos = int(input("How many photos have you taken?"))
        filesize = photos * resolution
        filesize = filesize/1000000000
        print("Photos take up rougly", filesize,"gigabytes on your phone")
        break
    except ValueError:
        print("not a number")