# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from docx import Document
from datetime import datetime
from services.alunos import count_alunos_turma_abraao
from services.criador_arquivos import MontaDocumento

app = FastAPI()

@app.get("/count_alunos_turmaAbraao/")
def get_count_alunos_turma_abraao():
    try:
        count = count_alunos_turma_abraao()
        return count
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/montar_doc/")
def fazerDoc():
    try:
        MontaDocumento('ata_template.docx', f'relatorio_concluido.docx')
        return 'relatorio_concluido.docx'
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.get("/download-docx/")
def download_docx():
    # Gerar o arquivo .docx
    doc_filename = fazerDoc()
    
    # Retornar o arquivo para download
    return FileResponse(doc_filename, media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document', filename='relatorio.docx')

# @app.get("/download_pdf/")
# def download_pdf():
#     try:
#         output_date = datetime.now().strftime(f"%d/%m/%Y, %H:%M:%S")
#         output_path = f"output_path_{output_date}.docx"
#         monta_docx('ata_template.docx', output_path)
#         return FileResponse(pdf_path, media_type='application/pdf', filename='report.pdf')
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


def monta_docx(template_path, output_path, data):
    document = Document(template_path)
    for paragraph in document.paragraphs:
        for key, value in data.items():
            if key in paragraph.text:
                for run in paragraph.runs:
                    run.text = run.text.replace(key, value)
                    
    document.save(output_path)




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
