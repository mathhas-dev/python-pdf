import PyPDF2


def teste():
    try:
        # Especifica os arquivos
        pdf_file = "input_document.pdf"
        footer = "footer.pdf"
        merged_file = "merged_document.pdf"

        # Abre os pdf's
        input_file = open(pdf_file, 'rb')
        input_pdf = PyPDF2.PdfFileReader(input_file)

        footer_file = open(footer, 'rb')
        footer_pdf = PyPDF2.PdfFileReader(footer_file)

        # Prepara o arquivo de saida
        output = PyPDF2.PdfFileWriter()

        page_count = input_pdf.getNumPages()

        for page_number in range(page_count):
            print(f"Adicionando footer: {page_number} de {page_count}")

            # Pega a página do pdf
            pdf_page = input_pdf.getPage(page_number)

            # mescla o footer com a página do pdf
            pdf_page.mergePage(footer_pdf.getPage(0))

            # adiciona a página mesclada ao documento de saida
            output.addPage(pdf_page)

        merged_file = open(merged_file, 'wb')

        output.write(merged_file)

        merged_file.close()
        footer_file.close()
        input_file.close()

    except Exception as e:
        print(f'Erro ao adicionar footer:\n\n{e}\n\n')


teste()
