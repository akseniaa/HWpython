import re


def save_result(param: list):
    fs = open('Result.txt', 'w+', encoding='utf-8')

    for r in range(len(param)):
        fs.write(f"{r + 1} - {len(re.split('[^0-9А-я]', param[r])) - 1}, {len(param[r]) - 1}\n")
    fs.write(f"Итоговое количество строк: {len(param)}")
    fs.close()
    pass


with open("txt/text.txt", 'r', encoding='utf-8') as f:
    save_result(f.readlines())
    f.close()
