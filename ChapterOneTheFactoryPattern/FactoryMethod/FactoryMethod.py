# ______________ The Factory Method Implementations ______________
import json
import xml.etree.ElementTree as ET


class JsonDataExtractor:
    """Class for extracting data from JSON files."""

    def __init__(self: object, filePath: str) -> None:
        self.data = dict()
        with open(filePath, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    @property
    def parsed_data(self: object) -> dict:
        return self.data


class XmlDataExtractor:
    """Class for extracting data from XML files."""

    def __init__(self: object, filePath: str) -> None:
        self.tree = ET.parse(filePath)

    @property
    def parsed_data(self: object) -> ET.ElementTree:
        return self.tree


def data_extraction_factory(filePath: str) -> object:
    """
    Factory Method for Data Extractors.
    Returns an instance of the appropriate class based on the file extension of the filePath.
    """
    if filePath.endswith(".xml"):
        extractor = XmlDataExtractor
    elif filePath.endswith(".json"):
        extractor = JsonDataExtractor
    else:
        raise ValueError(f"Cannot extract data from this file format {filePath}.")
    return extractor(filePath)


def extract_data_from(filePath: str) -> dict | ET.ElementTree:
    """Function to extract data from files."""
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(filePath)
    except ValueError as e:
        return e
    return factory_obj.parsed_data


def main():
    json_data = extract_data_from("employees.json")
    print(f"JSON Data: {json_data}")

    xml_data = extract_data_from("employees.xml")
    print(f"XML Data: {xml_data}")


if __name__ == "__main__":
    main()
