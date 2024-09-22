def create_xml(data):
    xml_output = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_output += '<gestion>\n'

    for row in data:
        if len(row) >= 9:  # Vérifiez que la ligne contient suffisamment d'éléments
            xml_output += '    <nom balise principale>\n'
            xml_output += f'    <name_balise>{row[0]}</name_balise>\n'

            xml_output += '    </nom balise principale>\n'


    xml_output += '</gestion>'
    return xml_output



def save_xml_to_file(xml_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(xml_data)

if __name__ == "__main__":
    fichier = 'nom '  # Spécifiez le chemin de votre fichier texte
    output_fichier = 'name.xml'  # Spécifiez le chemin de sortie pour le fichier XML

    data = []
    with open(fichier, 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split('\t')
            data.append(fields)

    xml_data = create_xml(data)
    save_xml_to_file(xml_data, output_fichier)
    print(f"Le fichier XML a été sauvegardé sous {output_fichier}")
