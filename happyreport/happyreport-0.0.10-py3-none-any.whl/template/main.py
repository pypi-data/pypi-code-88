from happyreport import send_mail, excel_format, file_clean
import custom
import settings

if __name__ == "__main__":
    # 获取报表保存
    wb = custom.workbook()

    # 格式化本地文件
    excel_format(data_tuple=wb, filename=settings.ATTACHES[0])

    # 发送邮件
    try:
        send_mail(host=settings.HOST,
                  port=settings.PORT,
                  user=settings.USER,
                  password=settings.PASSWORD,
                  receivers=settings.RECEIVERS,
                  subject=settings.SUBJECT,
                  attaches=settings.ATTACHES, content=settings.CONTENT)
    except Exception as e:
        send_mail(host=settings.HOST,
                  port=settings.PORT,
                  user=settings.USER,
                  password=settings.PASSWORD,
                  receivers=settings.WARNING_USER,
                  subject="【警告】邮件发送失败",
                  content=f'"{settings.SUBJECT}"发送失败, 报错信息:\n{str(e)}')

    # 清除历史文件
    file_clean("result")
