import xml.etree.ElementTree as ET
import maptools

tree = ET.parse('maps/images/europe.svg')
root = tree.getroot()

print(root)


territories, borders, units, occupations = maptools.loadMapJSON('europe.json')

# for b in territories:
# 	print(b.short)
# 	for country in root.findall('.//{http://www.w3.org/2000/svg}g[@short="'+b.short+'"]'):
# 		print("tag: " + str(country.tag))
# 		print("attr: " + str(country.attrib))
# 		print("text: " + str(country.text))
# 		#print(b.)


for o in occupations:
	print("bla" + o + occupations[o])
	for country in root.findall('.//{http://www.w3.org/2000/svg}g[@short="'+o+'"]/{http://www.w3.org/2000/svg}polygon'):
		print("tag: " + str(country.tag))
		print("attr: " + str(country.attrib))
		print("text: " + str(country.text))
		country.set("class", occupations[o])

tree.write('output.svg')