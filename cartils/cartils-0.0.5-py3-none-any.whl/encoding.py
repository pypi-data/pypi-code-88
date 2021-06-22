"""
This class handles Run Length Encoding (RLE) encoding and decoding
"""
class RLE:
    """
    Encode a string with RLE
    Output is in alternating block of runs of spaces and direct copies in hex format
    """
    @staticmethod
    def encodes(data):
        arr = list(data)
        rle_mode = False

        index = 0
        rle_count = 0
        copy_buffer = ''
        out = []

        if arr[0] == ' ':
            rle_mode = True
        while index < len(arr):
            if rle_mode:
                if arr[index] == ' ':
                    rle_count += 1
                else:
                    out.append(str(rle_count))
                    rle_count = 0
                    rle_mode = False

                    hex_string = hex(ord(arr[index])).replace('0x', '')
                    if len(hex_string) < 2:
                        hex_string = '0' + hex_string
                    copy_buffer += hex_string
            else:
                if arr[index] != ' ':
                    hex_string = hex(ord(arr[index])).replace('0x', '')
                    if len(hex_string) < 2:
                        hex_string = '0' + hex_string
                    copy_buffer += hex_string
                else:
                    out.append(copy_buffer)
                    copy_buffer = ''
                    rle_mode = True
                    rle_count += 1
            index += 1
        if rle_mode:
            out.append(str(rle_count))
            out = ['1'] + out
        else:
            out.append(copy_buffer)
            out = ['0'] + out
        return '.'.join(out)

    """
    Decode a RLE string
    """
    @staticmethod
    def decodes(data):
        arr = data.split('.')
        out = ''

        if arr[0] == '1':
            rle_mode = True
        else:
            rle_mode = False

        for el in arr[1:]:
            if rle_mode:
                count = int(el)
                out += ' ' * count
            else:
                hex_chars = [el[i:i+2] for i in range(0, len(el), 2)]
                for char in hex_chars:
                    if char.startswith('0'):
                        char = char[1:]
                    out += chr(int('0x'+ char, 16))
            rle_mode = not rle_mode
        return out

    @staticmethod
    def encode(data, file_obj):
        encoded = RLE.encodes(data)
        file_obj.write(encoded)

    @staticmethod
    def decode(file_obj):
        data = file_obj.read()
        decoded = RLE.decodes(data)
        return decoded

if __name__ == '__main__':
    input_data = '     abc     abc  abc        '
    encoded = RLE.encodes(input_data)
    print(encoded)
    decoded = RLE.decodes(encoded)
    print(decoded)