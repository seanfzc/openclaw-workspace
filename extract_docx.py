#!/usr/bin/env python3
import zipfile
import xml.etree.ElementTree as ET
import sys

def extract_text_from_docx(docx_path):
    """Extract text from a .docx file."""
    text_parts = []
    
    try:
        # Open the docx file as a zip archive
        with zipfile.ZipFile(docx_path, 'r') as zip_ref:
            # Read document.xml from the archive
            if 'word/document.xml' in zip_ref.namelist():
                with zip_ref.open('word/document.xml') as xml_file:
                    content = xml_file.read()
                    
                    # Parse XML
                    try:
                        # Register namespace for Word documents
                        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
                        
                        # Parse the XML
                        root = ET.fromstring(content)
                        
                        # Find all text elements
                        for elem in root.iter():
                            # Check for text elements
                            if elem.tag.endswith('}t'):
                                if elem.text:
                                    text_parts.append(elem.text)
                            # Also check for text in run properties
                            elif elem.tag.endswith('}r'):
                                for child in elem:
                                    if child.tag.endswith('}t'):
                                        if child.text:
                                            text_parts.append(child.text)
                        
                    except ET.ParseError as e:
                        # Fallback: extract raw text from XML
                        text_content = content.decode('utf-8', errors='ignore')
                        # Simple extraction between > and <
                        import re
                        text_parts = re.findall(r'>([^<]+)<', text_content)
            
            # Also try to read core properties for metadata
            if 'docProps/core.xml' in zip_ref.namelist():
                with zip_ref.open('docProps/core.xml') as core_file:
                    core_content = core_file.read().decode('utf-8', errors='ignore')
                    text_parts.append("\n=== Document Properties ===\n")
                    text_parts.append(core_content[:500])
                    
    except Exception as e:
        text_parts.append(f"Error extracting text: {e}")
    
    return '\n'.join(text_parts)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        docx_path = sys.argv[1]
        text = extract_text_from_docx(docx_path)
        print(text)
    else:
        print("Usage: python extract_docx.py <docx_file>")