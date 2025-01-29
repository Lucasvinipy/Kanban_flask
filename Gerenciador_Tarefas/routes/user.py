from flask import Blueprint, render_template , request
from database.tarefa import Tarefa , db

user_route = Blueprint('user', __name__)

"""""
    
        -/user/ (post) - inserir tarefa no servidor 
        -/user/ (GET) - renderizar formulario para criar tarefa
        -/user/<id> - (GET) - mostrar detalhes das tarefas
        -/user/<id>/edit (get) - renderizar formulario para alterar tarefa
        -/user/<id>/update (put) - atualizar os dados da tarefa 
        -/user/<id>/delet (delete) - deletar tarefa uma por uma
        - /user/<id>/delet (delete) - deletar todas tarefas

    """""

@user_route.route('/')
def listar_tarefas():
    tarefas = Tarefa.query.all()
    return render_template('listar_tarefas.html' , tarefa=tarefas)

@user_route.route('/' , methods=['POST'])
def inserir_tarefa():
    data = request.json 


    nova_tarefa = Tarefa(
    titulo=data.get('titulo'),
    descricao=data.get('descricao'),
    status=data.get('status', 'INICIAR')  # Define um valor padrão para o status

    )

    db.session.add(nova_tarefa)
    db.session.commit()

      # Renderiza o template correspondente ao status da tarefa
    if nova_tarefa.status == 'INICIAR':
        return render_template('item_tarefa_iniciar.html', tarefa=nova_tarefa)
    elif nova_tarefa.status == 'INICIADA':
        return render_template('item_tarefa_iniciado.html', tarefa=nova_tarefa)
    else:
        return render_template('item_tarefa_finalizado.html', tarefa=nova_tarefa)

  

@user_route.route('/new')
def form_tarefa():
    
    return render_template('form_tarefa.html')

@user_route.route('/<int:tarefa_id>')
def detalhe_tarefa(tarefa_id):
    
    return render_template('detalhe_tarefa.html')


@user_route.route('/<int:tarefa_id>/edit')
def form_editar_tarefa(tarefa_id):

    tarefa = Tarefa.query.get(tarefa_id)
    
    return render_template('form_tarefa.html',tarefa = tarefa)


@user_route.route('/<int:tarefa_id>/update', methods=['PUT'])
def atualizar_tarefa(tarefa_id):
    data=request.json    

    tarefa_editada = Tarefa.query.get(tarefa_id)

    tarefa_editada.titulo = data.get('titulo', tarefa_editada.titulo)  
    tarefa_editada.descricao = data.get('descricao', tarefa_editada.descricao)  
    tarefa_editada.status = data.get('status', tarefa_editada.status) 

    if ['status'] == 'INICIAR':
        return render_template('item_tarefa_iniciar.html', tarefa=tarefa_editada)
    
    elif ['status'] == 'INICIADA':
        return render_template('item_tarefa_iniciado.html', tarefa=tarefa_editada)
    else:
        return render_template('item_tarefa_finalizado.html', tarefa=tarefa_editada)
        

@user_route.route('/<int:tarefa_id>/delete', methods=['DELETE'])
def deletar_tarefa(tarefa_id):
    
    tarefa = Tarefa.query.get(tarefa_id)

    db.session.delete(tarefa)
    db.session.commit()

    