from PIL import Image
from PIL.ExifTags import TAGS


class MetadataExtractor:

    def __init__(self, file_path):

        self.file_path = file_path

    def extract_image_metadata(self):

        metadata = {}

        try:

            image = Image.open(
                self.file_path
            )

            exif = image.getexif()

            for tag_id, value in exif.items():

                tag = TAGS.get(
                    tag_id,
                    tag_id
                )

                metadata[tag] = value

        except Exception as e:

            metadata["error"] = str(
                e
            )

        return metadata

    def run(self):

        return {

            "module":
                "metadata_extractor",

            "file":
                self.file_path,

            "metadata":
                self.extract_image_metadata()
        }