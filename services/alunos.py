from firebase.firebase_config import db
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime

#region Contagem de alunos por turma
def count_alunos_turma_abraao():
    try:
        # Obter a referência do documento 'turmaAbraao' na coleção 'turmas'
        turma_abraao_ref = db.collection(u'turmas').document(u'turmaAbraão')
        
        # Consultar a coleção 'alunos' onde 'turma_associada' é igual à referência de 'turmaAbraao'
        alunos_ref = db.collection(u'alunos')
        query = alunos_ref.where(u'turma_associada', u'==', turma_abraao_ref)
        docs = query.stream()
        
        # Contar os documentos
        count = sum(1 for _ in docs)
        
        return count
    except Exception as e:
            raise Exception(f"Error counting alunos: {str(e)}")
    
    
def count_alunos_turma_amos():
    try:
        turma_amos_ref = db.collection(u'turmas').document(u'turmaAmós e Miriã')
        
        alunos_ref = db.collection(u'alunos')
        query = alunos_ref.where(u'turma_associada', u'==', turma_amos_ref)
        docs = query.stream()
        
        count = sum(1 for _ in docs)
        
        return count
    except Exception as e:
            raise Exception(f"Error counting alunos: {str(e)}")
    
    
def count_alunos_turma_samuel():
    try:
        turma_samuel_ref = db.collection(u'turmas').document(u'turmaSamuel')
        
        alunos_ref = db.collection(u'alunos')
        query = alunos_ref.where(u'turma_associada', u'==', turma_samuel_ref)
        docs = query.stream()
        
        count = sum(1 for _ in docs)
        
        return count
    except Exception as e:
            raise Exception(f"Error counting alunos: {str(e)}")

def count_alunos_turma_sarah():
    try:
        turma_sarah_ref = db.collection(u'turmas').document(u'turmaSarah')
        
        alunos_ref = db.collection(u'alunos')
        query = alunos_ref.where(u'turma_associada', u'==', turma_sarah_ref)
        docs = query.stream()
        
        count = sum(1 for _ in docs)
        
        return count
    except Exception as e:
            raise Exception(f"Error counting alunos: {str(e)}")

#endregion

#region Contagem de visitantes por turma

def get_visitantes_turma_abraao(date_str):
    try:
        turma_abraao_ref = db.collection(u'turmas').document(u'turmaAbraão')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_abraao_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()

        for doc in docs:
            visitantes = doc.to_dict().get('Visitantes', 0)
            return visitantes
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting visitantes: {str(e)}")


def get_visitantes_turma_amos(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        
        turma_amos_ref = db.collection(u'turmas').document(u'turmaAmós e Miriã')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_amos_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()

        for doc in docs:
            visitantes = doc.to_dict().get('Visitantes', 0)
            return visitantes
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting visitantes: {str(e)}")


def get_visitantes_turma_samuel(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        
        turma_samuel_ref = db.collection(u'turmas').document(u'turmaSamuel')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_samuel_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()

        for doc in docs:
            visitantes = doc.to_dict().get('Visitantes', 0)
            return visitantes
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting visitantes: {str(e)}")


def get_visitantes_turma_sarah(date_str):
    try:

        turma_sarah_ref = db.collection(u'turmas').document(u'turmaSarah')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_sarah_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()
        
        # Assumindo que só pode haver um documento com essa combinação específica
        for doc in docs:
            visitantes = doc.to_dict().get('Visitantes', 0)
            return visitantes
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting visitantes: {str(e)}")

#endregion
     
#region Contagem de faltas por turma
def count_alunos_faltas_turma_abraao(date_str):
    try:
        turma_abraao_ref = db.collection(u'turmas').document(u'turmaAbraão')
        
        alunos_ref = db.collection(u'alunos')
        query = alunos_ref.where(u'turma_associada', u'==', turma_abraao_ref).where(u'faltas', u'array_contains', date_str)
        docs = query.stream()
        
        count = sum(1 for _ in docs)
        
        return count
    except Exception as e:
        raise Exception(f"Error counting alunos with specific faltas: {str(e)}")
    
    
def count_alunos_faltas_turma_amos(date_str):
    try:
        turma_amos_ref = db.collection(u'turmas').document(u'turmaAmós e Miriã')
        
        alunos_ref = db.collection(u'alunos')
        query = alunos_ref.where(u'turma_associada', u'==', turma_amos_ref).where(u'faltas', u'array_contains', date_str)
        docs = query.stream()
        
        count = sum(1 for _ in docs)
        
        return count
    except Exception as e:
        raise Exception(f"Error counting alunos with specific faltas: {str(e)}")
    

def count_alunos_faltas_turma_samuel(date_str):
    try:
        # Obter a referência do documento 'turmaSamuel' na coleção 'turmas'
        turma_samuel_ref = db.collection(u'turmas').document(u'turmaSamuel')
        
        # Consultar a coleção 'alunos' onde 'turma_associada' é igual à referência de 'turmaSamuel' e 'faltas' contém a data específica
        alunos_ref = db.collection(u'alunos')
        query = alunos_ref.where(u'turma_associada', u'==', turma_samuel_ref).where(u'faltas', u'array_contains', date_str)
        docs = query.stream()
        
        # Contar os documentos
        count = sum(1 for _ in docs)
        
        return count
    except Exception as e:
        raise Exception(f"Error counting alunos with specific faltas: {str(e)}")
    
    
def count_alunos_faltas_turma_sarah(date_str):
    try:
        turma_sarah_ref = db.collection(u'turmas').document(u'turmaSarah')
        
        alunos_ref = db.collection(u'alunos')
        query = alunos_ref.where(u'turma_associada', u'==', turma_sarah_ref).where(u'faltas', u'array_contains', date_str)
        docs = query.stream()
        
        count = sum(1 for _ in docs)
        
        return count
    except Exception as e:
        raise Exception(f"Error counting alunos with specific faltas: {str(e)}")
#endregion

#region Contagem de biblias por turma

def get_biblias_by_date_and_turma_abraao(date_str):
    try:
        turma_abraao_ref = db.collection(u'turmas').document(u'turmaAbraão')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_abraao_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()

        for doc in docs:
            biblias = doc.to_dict().get('Bíblias', 0)
            return biblias
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting biblias: {str(e)}")


def get_biblias_by_date_and_turma_amos(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        
        turma_amos_ref = db.collection(u'turmas').document(u'turmaAmós e Miriã')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_amos_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()

        for doc in docs:
            biblias = doc.to_dict().get('Bíblias', 0)
            return biblias
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting biblias: {str(e)}")


def get_biblias_by_date_and_turma_samuel(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        
        turma_samuel_ref = db.collection(u'turmas').document(u'turmaSamuel')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_samuel_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()

        for doc in docs:
            biblias = doc.to_dict().get('Bíblias', 0)
            return biblias
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting biblias: {str(e)}")


def get_biblias_by_date_and_turma_sarah(date_str):
    try:

        turma_sarah_ref = db.collection(u'turmas').document(u'turmaSarah')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_sarah_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()
        
        # Assumindo que só pode haver um documento com essa combinação específica
        for doc in docs:
            biblias = doc.to_dict().get('biblias', 0)
            return biblias
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting biblias: {str(e)}")

#endregion

#region Contagem de revistas por turma

def get_revistas_by_date_and_turma_abraao(date_str):
    try:
        turma_abraao_ref = db.collection(u'turmas').document(u'turmaAbraão')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_abraao_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()

        for doc in docs:
            revistas = doc.to_dict().get('Revistas', 0)
            return revistas
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting Revistas: {str(e)}")


def get_revistas_by_date_and_turma_amos(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        
        turma_amos_ref = db.collection(u'turmas').document(u'turmaAmós e Miriã')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_amos_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()

        for doc in docs:
            revistas = doc.to_dict().get('Revistas', 0)
            return revistas
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting revistas: {str(e)}")


def get_revistas_by_date_and_turma_samuel(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        
        turma_samuel_ref = db.collection(u'turmas').document(u'turmaSamuel')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_samuel_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()

        for doc in docs:
            revistas = doc.to_dict().get('Revistas', 0)
            return revistas
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting revistas: {str(e)}")


def get_revistas_by_date_and_turma_sarah(date_str):
    try:

        turma_sarah_ref = db.collection(u'turmas').document(u'turmaSarah')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_sarah_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()
        
        # Assumindo que só pode haver um documento com essa combinação específica
        for doc in docs:
            revistas = doc.to_dict().get('Revistas', 0)
            return revistas
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting revistas: {str(e)}")

#endregion

#region Contagem de retardatarios por turma

def get_retardatarios_by_date_and_turma_abraao(date_str):
    try:
        turma_abraao_ref = db.collection(u'turmas').document(u'turmaAbraão')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_abraao_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()

        for doc in docs:
            retardatarios = doc.to_dict().get('Retardatários', 0)
            return retardatarios
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting retardatarios: {str(e)}")


def get_retardatarios_by_date_and_turma_amos(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        
        turma_amos_ref = db.collection(u'turmas').document(u'turmaAmós e Miriã')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_amos_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()

        for doc in docs:
            retardatarios = doc.to_dict().get('Retardatários', 0)
            return retardatarios
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting retardatarios: {str(e)}")


def get_retardatarios_by_date_and_turma_samuel(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        
        turma_samuel_ref = db.collection(u'turmas').document(u'turmaSamuel')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_samuel_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()

        for doc in docs:
            retardatarios = doc.to_dict().get('Retardatários', 0)
            return retardatarios
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting retardatarios: {str(e)}")


def get_retardatarios_by_date_and_turma_sarah(date_str):
    try:

        turma_sarah_ref = db.collection(u'turmas').document(u'turmaSarah')
        
        dados_ref = db.collection(u'dados_obtained')
        query = dados_ref.where(u'turma_referente', u'==', turma_sarah_ref).where(u'dia_letivo', u'==', date_str)
        docs = query.stream()
        
        # Assumindo que só pode haver um documento com essa combinação específica
        for doc in docs:
            retardatarios = doc.to_dict().get('Retardatários', 0)
            return retardatarios
        
        return 0
    except Exception as e:
        raise Exception(f"Error getting retardatarios: {str(e)}")

#endregion
