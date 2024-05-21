import xml.etree.ElementTree as ET
from lxml import etree
from pprint import pprint

PERSON_XML = "person_with_xml.xml"
PERSON_LXML = "person_with_lxml.xml"
# Create a dictionary representing the complex object
data = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    }
}


class WithXML:
    def __init__(self):
        self.file_name = "with_xml.xml"
        self.tree = ET.parse(PERSON_XML)
        self.root = self.tree.getroot()

    def write(self):
        # Create the root element
        root = ET.Element("data")

        # Create child elements
        item1 = ET.SubElement(root, "item")
        item1.text = "item1"

        item2 = ET.SubElement(root, "item")
        item2.text = "item2"

        # Create the XML tree
        tree = ET.ElementTree(root)

        # Write the tree to a file
        tree.write(self.file_name)
        print("XML file created successfully!")

    def read(self):
        # Parse the XML file
        tree = ET.parse(self.file_name)

        # Get the root element
        root = tree.getroot()

        # Iterate over child elements
        for child in root:
            print(child.tag, child.text)

    # Function to convert dictionary to XML
    def dict_to_xml(self, tag, d):
        elem = ET.Element(tag)
        for key, val in d.items():
            child = ET.Element(key)
            child.text = str(val)
            elem.append(child)
        return elem

    # Function to convert XML element to dictionary
    def xml_to_dict(self, elem):
        d = {}
        for child in elem:
            if len(child) == 0:
                d[child.tag] = child.text
            else:
                d[child.tag] = self.xml_to_dict(child)
        return d


class WithLXML:
    def __init__(self):
        self.file_name = "with_lxml.xml"
        # Parse the XML file
        self.tree = etree.parse(PERSON_LXML)
        self.root = self.tree.getroot()

    def write(self):
        # Create the root element
        root = etree.Element("data")

        # Create child elements
        item1 = etree.SubElement(root, "item")
        item1.text = "item1"

        item2 = etree.SubElement(root, "item")
        item2.text = "item2"

        # Create the XML tree
        tree = etree.ElementTree(root)

        # Write the tree to a file
        tree.write(self.file_name, pretty_print=True)

    def read(self):
        # Parse the XML file
        tree = etree.parse(self.file_name)

        # Get the root element
        root = tree.getroot()

        # Iterate over child elements
        for child in root:
            print(child.tag, child.text)

    # Function to convert dictionary to XML
    def dict_to_xml(self, d):
        root = etree.Element('person')
        for key, val in d.items():
            if isinstance(val, dict):
                child = etree.SubElement(root, key)
                for k, v in val.items():
                    sub_child = etree.SubElement(child, k)
                    sub_child.text = str(v)
            else:
                child = etree.SubElement(root, key)
                child.text = str(val)
        return root

    # Function to convert XML element to dictionary
    def xml_to_dict(self, elem):
        d = {}
        for child in elem:
            if len(child) == 0:
                d[child.tag] = child.text
            else:
                d[child.tag] = self.xml_to_dict(child)
        return d


if __name__ == "__main__":
    with_xml = WithXML()
    with_xml.write()
    with_xml.read()

    with_lxml = WithLXML()
    with_lxml.write()
    with_lxml.read()

    # Convert dictionary to XML element
    root = with_xml.dict_to_xml('person', data)

    # Create XML tree
    tree = ET.ElementTree(root)

    # Write XML tree to file
    tree.write(PERSON_XML)

    # Convert dictionary to XML element
    root = with_lxml.dict_to_xml(data)

    # Create XML tree
    tree = etree.ElementTree(root)

    # Write XML tree to file
    tree.write(PERSON_LXML, pretty_print=True)

    # Convert XML element to dictionary
    data = with_xml.xml_to_dict(root)

    # Print the dictionary
    pprint(data)

    # Convert XML element to dictionary
    data = with_lxml.xml_to_dict(root)

    # Print the dictionary
    pprint(data)
