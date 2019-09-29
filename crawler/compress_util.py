import gzip
import base64


class Compress:
    @staticmethod
    def compress_str(data) -> str:
        '''
        data是一个普通字符串
        '''
        if not data:
            return data
        compress_data = gzip.compress(data.encode('utf-8'))
        b64_data = base64.b64encode(compress_data)
        return str(b64_data, 'utf-8')

    @staticmethod
    def decompress_str(data) -> str:
        '''
        data 是一个base64格式的字符串
        '''
        if not data:
            return data
        compress_data = base64.b64decode(data.encode())
        decompress_data = gzip.decompress(compress_data)
        return str(decompress_data, 'utf-8')


if __name__ == "__main__":
    with open('d:/colorname_rgb.html', 'r', encoding='gb2312') as file:
        source = file.read()
    r1 = Compress.compress_str(source)
    print(len(r1))
    # r2 = Compress.decompress_str(r1)
    with open('./result.html', 'w', encoding='utf-8') as file:
        file.write(r1)
    print('finished....')
