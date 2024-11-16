# S-боксы
S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ]
]

KEY_EXP = {
    0: 15,
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 3,
    7: 4,
    8: 5,
    9: 6,
    10: 7,
    11: 8,
    12: 7,
    13: 8,
    14: 9,
    15: 10,
    16: 11,
    17: 12,
    18: 11,
    19: 12,
    20: 13,
    21: 14,
    22: 15,
    23: 0,
}

# IP и IP-обратные
IP = [
    26, 18, 10, 2, 28, 20, 12, 4,
    30, 22, 14, 6, 32, 24, 16, 8,
    25, 17, 9, 1, 27, 19, 11, 3,
    29, 21, 13, 5, 31, 23, 15, 7
]

IP_INV = [
    20, 4, 24, 8, 28, 12, 32, 16,
    19, 3, 23, 7, 27, 11, 31, 15,
    18, 2, 22, 6, 26, 10, 30, 14,
    17, 1, 21, 5, 25, 9, 29, 13
]

P = [16, 7, 12, 13, 1, 5, 15, 10, 2, 8, 3, 9, 14, 6, 4, 11]


# Функция преобразования 16-ричной строки в двоичную
def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(32)


# Функция преобразования 16-ричной строки в двоичную (для ключа)
def hex_to_bin_key(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(24)


# Функция IP-перестановки
def initial_permutation(data):
    return ''.join(data[i - 1] for i in IP)


def initial_permutation_inv(data):
    return ''.join(data[i - 1] for i in IP_INV)


# Функция побитового сложения с ключом
def xor(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Arrays must be of the same length.")
    result = []
    for a, b in zip(array1, array2):
        result.append(int(a) ^ int(b))  # Применяем XOR и добавляем результат в список
    return result


class Des:
    def __init__(self):
        self.steps = []

    # Функция расширения и перестановки
    def expansion_permutation(self, right_half_list):
        right_half = list(map(int, right_half_list))
        new_right_half = []
        # Вывод правой части
        formatted_right_half = [right_half[i:i + 4] for i in range(0, len(right_half), 4)]
        self.steps.append("Правая часть:")
        cur_steps = []
        for line in formatted_right_half:
            cur_steps.append(f"{''.join(map(str, line))} ")
        self.steps.append(''.join(cur_steps))
        self.steps.append("")
        # Само расширение ключа
        j = 0

        for key, value in KEY_EXP.items():
            new_right_half.append(right_half[value])

        return new_right_half

    # Функция применения S-боксов
    def s_box_lookup(self, expanded_half):
        s_output = []
        self.steps.append(f"Строки и столбцы для S-box:")
        cur_steps = []
        for i in [0, 6, 12, 18]:
            x1 = str(expanded_half[i])
            x2 = str(expanded_half[i + 1])
            x3 = str(expanded_half[i + 2])
            x4 = str(expanded_half[i + 3])
            x5 = str(expanded_half[i + 4])
            x6 = str(expanded_half[i + 5])
            rowstr = x1 + x6
            colstr = x2 + x3 + x4 + x5
            row = int(rowstr, 2)
            col = int(colstr, 2)
            cur_steps.append(f"[{row}, {col}] ")
            s_output.append(S_BOXES[(i // 6) % 4][row][col])

        self.steps.append(''.join(cur_steps))
        self.steps.append("")
        return s_output

    # Функция P-перестановки
    def p_permutation(self, s_output):
        p_output = []
        s_output_bin = []
        for i in [0, 1, 2, 3]:
            s_output_bin.append((bin(s_output[i])[2:]).zfill(4))
        # Вывод двоичной формы результата s-бокса
        formatted_s_output_bin = [s_output_bin[i:i + 4] for i in range(0, len(s_output_bin), 4)]
        self.steps.append("Двоичная форма результата s-бокса:")
        cur_steps = []
        for line in s_output_bin:
            cur_steps.append(f"{''.join(map(str, line))} ")
        self.steps.append(''.join(cur_steps))
        self.steps.append("")

        s_binary_string = ''.join(s_output_bin)
        s_binary_list = list(s_binary_string)
        for i in range(16):
            koef = P[i] - 1
            p_output.append(s_binary_string[koef])
        return p_output

    # Основная функция шифрования
    def encrypt(self, data: str, key: str):
        # Преобразование входных данных
        binary_data = hex_to_bin(data)
        binary_key = hex_to_bin_key(key)

        # Применение IP-перестановки
        permuted_data = initial_permutation(binary_data)

        # Двоичное введенное
        formatted_binary_data = [binary_data[i:i + 8] for i in range(0, len(binary_data), 8)]
        self.steps.append("Входные данные:")
        for line in formatted_binary_data:
            self.steps.append(f"{line}")

        self.steps.append("")

        formatted_binary_key = [binary_key[i:i + 8] for i in range(0, len(binary_key), 8)]
        formatted_binary_key2 = [binary_key[i:i + 6] for i in range(0, len(binary_key), 6)]

        self.steps.append("Входной ключ:")
        # sum_key_ui.insert(tk.END, "Входной ключ:\n")
        for line in formatted_binary_key:
            self.steps.append(f"{line}")

        self.steps.append("")
        # for line in formatted_binary_key2:
        #     sum_key_ui.insert(tk.END, f"{line} ")

        # Данные после IP перестановки
        formatted_permuted_data = [permuted_data[i:i + 8] for i in range(0, len(permuted_data), 8)]
        self.steps.append("После IP-перестановки:")
        for line in formatted_permuted_data:
            self.steps.append(f"{line}")
        self.steps.append("")

        # Расширение правой половины
        expanded_half = self.expansion_permutation(permuted_data[16:])
        formatted_expanded_half = [expanded_half[i:i + 6] for i in range(0, len(expanded_half), 6)]
        self.steps.append("Результат расширения правой части:")
        cur_steps = []
        for line in formatted_expanded_half:
            cur_steps.append(f"{''.join(map(str, line))}")

        self.steps.append(' '.join(cur_steps))
        self.steps.append("")

        # Сложение с ключом
        summed_half = xor(expanded_half, list(binary_key))
        formatted_summed_half = [summed_half[i:i + 6] for i in range(0, len(summed_half), 6)]
        self.steps.append("Результат сложения с ключом:")
        cur_steps = []
        for line in formatted_summed_half:
            cur_steps.append(f"{''.join(map(str, line))}")
        self.steps.append(' '.join(cur_steps))
        self.steps.append("")

        # S-боксы
        s_output = self.s_box_lookup(summed_half)
        s_output_str = str(s_output)
        self.steps.append(f"Результат s-бокса:\n{s_output_str}")
        self.steps.append("")

        # P - перестановка
        # Отображение результата P-перестановки в текстовое поле
        p_output = self.p_permutation(s_output)
        self.steps.append(
            f"Результат P-перестановки:\n{''.join(p_output[:4])} {''.join(p_output[4:8])} {''.join(p_output[8:12])} {''.join(p_output[12:])}")
        self.steps.append("")
        # Xor с L0
        left_half_new = permuted_data[:16]
        self.steps.append(f"L0 = {' '.join(left_half_new[i:i + 4] for i in range(0, len(left_half_new), 4))}")
        self.steps.append("")
        right_half_new = xor(list(left_half_new), p_output)
        right_half_new_str = ''.join(str(num) for num in right_half_new)
        self.steps.append(
            f"Правая часть после ксора:\n{' '.join(right_half_new_str[i:i + 4] for i in range(0, len(right_half_new_str), 4))}")
        self.steps.append("")
        # Вывод новой таблицы до Ip-inv
        right_half_ip = list(permuted_data[16:])
        binary_data_new = (right_half_ip + right_half_new)
        binary_data_new_str = ''.join(str(num) for num in binary_data_new)
        binary_data_new_grouped = '\n'.join(binary_data_new_str[i:i + 8] for i in range(0, len(binary_data_new_str), 8))
        self.steps.append(f"Таблица до Ip^-1:\n{binary_data_new_grouped}\n")

        # Ip-inv
        binary_data_new = ''.join(str(bit) for bit in binary_data_new)
        inv_permuted_data = initial_permutation_inv(binary_data_new)

        # Данные после IP_INV перестановки
        formatted_inv_permuted_data = [inv_permuted_data[i:i + 8] for i in range(0, len(inv_permuted_data), 8)]
        self.steps.append("После IP_INV-перестановки:\n")
        cur_steps = []
        for line in formatted_inv_permuted_data:
            cur_steps.append(f"{line} = {hex(int(line, 2))[2:].zfill(2).upper()}\n")
        self.steps.append(''.join(cur_steps))
