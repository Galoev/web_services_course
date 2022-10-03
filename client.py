import numpy as np
import cv2
import click
import grpc

from protos.builds.services_pb2 import Image, Request
from protos.builds.services_pb2_grpc import WatermarkServiceStub


def pack_into_Image(img: np.ndarray) -> Image:
    """Wraps a numpy array into a type Image.

    Args:
        img (np.ndarray): wraparound array

    Returns:
        Image: collected object of type Image
    """
    h, w, c = img.shape
    return Image(height=h, width=w, channel=c, data=img.tobytes())


@click.command
@click.argument(
    "main_img_path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=True),
)
@click.argument(
    "logo_img_path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, resolve_path=True),
)
@click.argument("opacity", type=click.IntRange(min=0, max=100))
@click.argument(
    "dst",
    default=".",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, resolve_path=True),
)
def main(
    main_img_path: click.Path,
    logo_img_path: click.Path,
    opacity: click.IntRange,
    dst: click.Path,
):
    with grpc.insecure_channel("localhost:3000") as channel:
        stub = WatermarkServiceStub(channel)
        logo_img = cv2.imread(logo_img_path)
        main_img = cv2.imread(main_img_path)

        logo_img = pack_into_Image(logo_img)
        main_img = pack_into_Image(main_img)

        retquest = Request(logo_image=logo_img, main_imgae=main_img, opacity=opacity)
        img = stub.addImageWatermark(retquest)

        img_data = img
        img_bytes = img_data.data
        img = np.frombuffer(img_bytes, dtype="uint8")
        img = img.reshape(img_data.height, img_data.width, img_data.channel)

        cv2.imwrite(f"{dst}/new_image.jpg", img)


if __name__ == "__main__":
    main()
