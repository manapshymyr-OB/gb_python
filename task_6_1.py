filename = 'nginx_logs.txt'
"""1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt"""

def process_data(filename):
    with open(filename) as f:
        logs = f.read().splitlines()


    data = []

    for log in logs:
        # get ip
        ip_address, log_line = log.split(' - - ')
        date, log_line = log_line.split('] "')
        request_type, log_line = log_line.split(' HTTP')

        request_type, requested_resource = request_type.split(' ')

        data_tuple = (ip_address, request_type, requested_resource)

        data.append(data_tuple)


    return data

data = process_data(filename)
print(data)