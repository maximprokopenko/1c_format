import yaml


def parse(file_path):
    trash_string = ('1CClientBankExchange', 'КонецФайла')
    content = []
    indent_count = 0

    with open(file_path) as f:
        lines = f.readlines()
        for line in lines:
            if [t for t in trash_string if t in line]:
                continue

            line = line.replace('=', ': ')

            if 'Секция' in line:
                if ':' in line:
                    name, value = line.split(': ')
                    line = name + ':\n'

                    if line not in content:
                        content.append('  ' * indent_count + line)

                    line = '  ' * (indent_count) + '- ' + value.replace('\n', ':\n')
                else:
                    line = line.replace('\n', ': \n')

                content.append('    ' * indent_count + line)
                indent_count += 1
            elif 'Конец' in line:
                indent_count -= 1
            else:
                content.append('  ' * indent_count + line)

    content_as_str = ''.join(content)
    return yaml.load(content_as_str, Loader=yaml.FullLoader)