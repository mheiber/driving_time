import csv


def _write_row(row, out_file):
    print(row)
    with open(out_file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)


def persist(cur_time, duration, out_file):
    row = [cur_time, duration]
    _write_row(row, out_file)
