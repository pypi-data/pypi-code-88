from osef import parser


def save_osef_from_tcp(
    tcp_input,
    output_filename,
):
    with open(output_filename, "wb") as output:
        input = parser.open_osef(tcp_input)
        if not input:
            return
        bytes_written = 0

        while True:
            try:
                read = input.read()
                if read is None or len(read) == 0:
                    break
                output.write(read)
                bytes_written += len(read)
            except KeyboardInterrupt:
                break
        input.close()
        return bytes_written
