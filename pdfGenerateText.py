
from reportlab.pdfgen import canvas


def GeneratePDF(lista):
    try:
        nome_pdf = input('Informe o nome do PDF: ')

        pdf = canvas.Canvas(f'{nome_pdf}.pdf')

        # Padrão A4
        xMax = 595.27
        yMax = 841.89

        y = yMax-120

        for nome, idade in lista.items():
            y -= 20
            pdf.drawString(yMax-345, y, f'{nome} : {idade}')

        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245, 750, 'Lista de Convidados')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245, 724, 'Nome e idade')
        pdf.save()

        print(f'{nome_pdf}.pdf criado com sucesso!')
    except:
        print(f'Erro ao gerar {nome_pdf}.pdf')


lista = {'Aléxia': '22', 'Matheus': '22', 'Julio César': '45', 'Julio': '45',
         'Rosângela': '40', 'Mariana': '10', 'Jorge': '65', 'Vera': '60'}

GeneratePDF(lista)
