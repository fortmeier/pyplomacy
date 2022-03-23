import xml.etree.ElementTree as ET
import maptools

tree = ET.parse('maps/images/standard02.svg')
root = tree.getroot()

for country in root.findall('.//{http://www.w3.org/2000/svg}g'):
	print("tag: " + str(country.tag))
	print("attr: " + str(country.attrib))
	print("text: " + str(country.text))
	g = country.findall('.//{http://www.w3.org/2000/svg}text')
	for t in g:
		print("g: " + str(t.text))
		country.set('short', t.text)

tree.write('maps/images/europe.svg')