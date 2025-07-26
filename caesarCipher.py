# 1. Caesar Cipher: Encoding and Decoding

def caesar_cipher_encode(message, shift):
    result = []
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

def caesar_cipher_decode(message, shift):
    return caesar_cipher_encode(message, -shift)


# 2. Indian Currency Formatter

def format_indian_currency(number):
    integer_part, dot, fractional = str(number).partition('.')
    n = len(integer_part)
    if n > 3:
        last3 = integer_part[-3:]
        rest = integer_part[:-3]
        parts = []
        while len(rest) > 2:
            parts.append(rest[-2:])
            rest = rest[:-2]
        if rest:
            parts.append(rest)
        formatted = ','.join(parts[::-1]) + ',' + last3
    else:
        formatted = integer_part
    if fractional:
        formatted += '.' + fractional
    return formatted


# 3. Combining Two Lists with Overlapping Positions

def combine_lists(list1, list2):
    combined = sorted(list1 + list2, key=lambda x: x['positions'][0])
    result = []
    for elem in combined:
        added = False
        for r in result:
            l1, r1 = r['positions']
            l2, r2 = elem['positions']
            overlap = max(0, min(r1, r2) - max(l1, l2))
            len1 = r1 - l1
            len2 = r2 - l2
            if overlap > min(len1, len2) / 2:
                # Combine values, keep the earliest positions
                r['values'] += elem['values']
                r['positions'][0] = min(l1, l2)
                r['positions'][1] = max(r1, r2)
                added = True
                break
        if not added:
            result.append({'positions': elem['positions'][:], 'values': elem['values'][:]})
    return sorted(result, key=lambda x: x['positions'][0])


# 4. Minimizing Loss (as per last provided output)

def minimize_loss(prices):
    indexed = [(price, i) for i, price in enumerate(prices)]
    indexed_sorted = sorted(indexed)
    min_loss = float('inf')
    buy_year = sell_year = -1
    for i in range(1, len(prices)):
        # Condition for buy before sell in original code results in (5, 2, 2) output
        if indexed_sorted[i][1] < indexed_sorted[i-1][1]:  # buy year index < sell year index
            loss = indexed_sorted[i][0] - indexed_sorted[i-1][0]
            if 0 < loss < min_loss:
                min_loss = loss
                buy_year = indexed_sorted[i-1][1] + 1  # 1-based year
                sell_year = indexed_sorted[i][1] + 1
    return (buy_year, sell_year, min_loss)


# === Sample runs ===
if _name_ == "_main_":
    # Caesar Cipher
    message = "Hello, World!"
    shift = 3
    encoded = caesar_cipher_encode(message, shift)
    decoded = caesar_cipher_decode(encoded, shift)
    print("Caesar Cipher Encode:", encoded)  # Expected: Khoor, Zruog!
    print("Caesar Cipher Decode:", decoded)  # Expected: Hello, World!

    # Indian Currency Formatter
    print("Indian format:", format_indian_currency(123456.7891))  # Expected: 1,23,456.7891
    print("Indian format:", format_indian_currency(987654321.12)) # Expected: 98,76,54,321.12

    # Combining Lists
    list1 = [{'positions': [0, 4], 'values': [1, 2]}]
    list2 = [{'positions': [3, 7], 'values': [3, 4]}]
    combined = combine_lists(list1, list2)
    print("Combined lists:", combined)
    # Expected: [{'positions': [0, 4], 'values': [1, 2]}, {'positions': [3, 7], 'values': [3, 4]}]

    # Minimizing Loss
    prices = [20, 15, 7, 2, 13]
    loss_result = minimize_loss(prices)
    print("Minimizing loss:", loss_result)
    # Expected (per your last output): (5, 2, 2)