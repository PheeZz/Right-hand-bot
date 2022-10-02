import aspose.words as aw


def convert_file(file_name: str, file_format: str) -> str:
    """converts file to specified format

    Args:
        filename (str): name of file to convert with
        file_format (str): format to convert to

    Returns:
        str: path to converted file
    """
    doc = aw.Document(f'data/{file_name}')
    doc.save(f'data\{file_name.split(".")[0]}.{file_format}')

    if file_format.lower() != 'pdf':
        # remove ads from converted file
        with open(f'data\{file_name.split(".")[0]}.{file_format}', 'r') as file:
            new_file = file.read()

        remove_list = [
            'Evaluation Only. Created with Aspose.Words. Copyright 2003-2022 Aspose Pty Ltd.',
            'Created with an evaluation copy of Aspose.Words. To discover the full versions of our APIs please visit: https://products.aspose.com/words/',
        ]
        for string in remove_list:
            if file_format == 'md':
                string = '**' + string + '**'
            new_file = new_file.replace(string, '')

        with open(f'data\{file_name.split(".")[0]}.{file_format}', 'w') as file:
            file.write(new_file)

    return f'data\{file_name.split(".")[0]}.{file_format}'
