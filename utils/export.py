from io import BytesIO

from xlsxwriter.workbook import Workbook


def export(values: list[dict]):
    buffer = BytesIO()
    workbook = Workbook(buffer, {'in_memory': True})
    worksheet = workbook.add_worksheet()
    if values:
        header = list(values[0].keys())
        for i, header_item in enumerate(header):
            worksheet.write(0, i, header_item)
        for i, row in enumerate(values):
            for j, header_item in enumerate(header):
                worksheet.write(i + 1, j, str(row[header_item]))
    workbook.close()
    buffer.seek(0)
    return buffer
