with open('/home/eddy-di/Downloads/code_raw_texts.txt', 'r', encoding='utf-8') as f, open('/home/eddy-di/Desktop/learning_python/stepik_examples/code_texts.txt', 'w') as output:
    data = f.readlines()
    data2 = []
    for line in data:
        if 'TEST_' in line:
            line = line.replace('# ', "print()\nprint('")
            line = line[:-1] + "')" + line[-1:]
        data2.append(line)

    for line in data2:
        output.write(line)

    print('Done!')