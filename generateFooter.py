
from reportlab.pdfgen import canvas


def GeneratePDF():
    try:
        nome_pdf = input('Informe o nome do PDF: ')

        pdf = canvas.Canvas(f'{nome_pdf}.pdf')

        # Padrão A4
        xMax = 595.27
        yMax = 841.89

        sha256 = '3b8b1f0fa9f11b7dbfc397380312c727726218kc15f4176f1dd8c73f3a71c5263'
        url = 'http://localhost:3000/dashboard/visualizar-documento/01b1b3bc-6115-4eea-9a88-617e568aee91/'

        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 8)
        pdf.drawImage('./images/logo-lacoste.png',xMax-580, yMax-835, width=50, height=50, preserveAspectRatio=False)
        pdf.drawString(xMax-510, yMax-810, f'Hash SHA256 do documento: {sha256}')
        pdf.drawString(xMax-510, yMax-823, f'URI para visualização do documento: {url}')
        pdf.save()

        print(f'{nome_pdf}.pdf criado com sucesso!')
    except:
        print(f'Erro ao gerar {nome_pdf}.pdf')

GeneratePDF()
