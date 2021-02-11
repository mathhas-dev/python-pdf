
from reportlab.pdfgen import canvas


def GeneratePDF():
    try:
        nome_pdf = input('Informe o nome do PDF: ')

        pdf = canvas.Canvas(f'{nome_pdf}.pdf')

        # Padrão A4
        xMax = 595.27
        yMax = 841.89

        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 18)
        pdf.drawString(220, 740, 'Testando Imagem')

        pdf.drawImage('./images/logo-lacoste.png',xMax-100, yMax-100, width=80, height=80, preserveAspectRatio=False)

        pdf.save()

        print(f'{nome_pdf}.pdf criado com sucesso!')
    except Exception as e:
        print(f'Erro ao gerar pdf com imagem: {e}')


GeneratePDF()
