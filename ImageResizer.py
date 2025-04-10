import cv2
import os


def resize_and_save_image(src, dest, scale):

    try:
        # read the Image
        image = cv2.imread(src, cv2.IMREAD_UNCHANGED)

        print()
        print("Configuration of input Image: ")
        print("Height:", image.shape[0], "Width:", image.shape[1])

        # Calculate new width and height of Image
        new_width = int(image.shape[1] * scale / 100)
        new_height = int(image.shape[0] * scale / 100)

        # resize the image
        resized_image = cv2.resize(image, (new_width, new_height))
        cv2.imwrite(dest, resized_image)

        print()
        print("Configuration of resized Image: ")
        print("Height:", resized_image.shape[0], "Width:", resized_image.shape[1])

        return True

    except ValueError:
        print("scalePercent : Input Mismatch Error")
        return False

    except cv2.error as e:
        print(f"OpenCVError : {e}")
        print("Error in reading or processing the Image, Please try again.")
        return False

    except FileNotFoundError:
        print("Error: Destination Path is invalid, Please provide a valid path.")
        return False


if __name__ == "__main__":
    flag = 0

    while flag == 0:
        source = input("Enter the source of Image: ")

        if source.lower() == "q":
            break

        if os.path.exists(source):
            destination = input("Enter the destination of Image: ")
            try:
                scalePercent = int(input("Enter the scale percentage of Image: "))

                success = resize_and_save_image(source, destination, scalePercent)

                if success:
                    flag = 1
                    cv2.destroyAllWindows()

            except ValueError:
                print("scalePercent : Invalid input, Please a valid input.")

        else:
            print("Error in accessing the file, Please try again.")
